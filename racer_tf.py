"""
Script to drive a keras TF model with the Virtual Race Environment.

Usage:
    racer.py (--model=<model>) (--host=<ip_address>) (--name=<car_name>)
    
Options:
    -h --help        Show this screen.
"""

import os
import numpy as np
import json
import time
from io import BytesIO
import base64
import re
import socket
import select
from threading import Thread

from docopt import docopt
import tensorflow.python.keras as keras
from PIL import Image

# Server port
PORT = 9091
IMG_NORM_SCALE = 1.0 / 255.0

def replace_float_notation(string):
    """
    Replace unity float notation for languages like
    French or German that use comma instead of dot.
    This convert the json sent by Unity to a valid one.
    Ex: "test": 1,2, "key": 2 -> "test": 1.2, "key": 2

    :param string: (str) The incorrect json string
    :return: (str) Valid JSON string
    """
    regex_french_notation = r'"[a-zA-Z_]+":(?P<num>[0-9,E-]+),'
    regex_end = r'"[a-zA-Z_]+":(?P<num>[0-9,E-]+)}'

    for regex in [regex_french_notation, regex_end]:
        matches = re.finditer(regex, string, re.MULTILINE)

        for match in matches:
            num = match.group('num').replace(',', '.')
            string = string.replace(match.group('num'), num)
    return string


class SDClient:
    def __init__(self, host, port, poll_socket_sleep_time=0.05):
        self.msg = None
        self.host = host
        self.port = port
        self.poll_socket_sleep_sec = poll_socket_sleep_time

        # the aborted flag will be set when we have detected a problem with the socket
        # that we can't recover from.
        self.aborted = False
        self.connect()


    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connecting to the server 
        print("connecting to", self.host, self.port)
        self.s.connect((self.host, self.port))

        # time.sleep(pause_on_create)
        self.do_process_msgs = True
        self.th = Thread(target=self.proc_msg, args=(self.s,))
        self.th.start()        


    def send(self, m):
        self.msg = m

    def send_now(self, msg):
        print("sending now:", msg)
        self.s.sendall(msg.encode("utf-8"))

    def on_msg_recv(self, j):
        # print("got:", j['msg_type'])
        # we will always have a 'msg_type' and will always get a json obj
        pass


    def stop(self):
        # signal proc_msg loop to stop, then wait for thread to finish
        # close socket
        self.do_process_msgs = False
        self.th.join()
        self.s.close()


    def proc_msg(self, sock):
        '''
        This is the thread message loop to process messages.
        We will send any message that is queued via the self.msg variable
        when our socket is in a writable state. 
        And we will read any messages when it's in a readable state and then
        call self.on_msg_recv with the json object message.
        '''
        sock.setblocking(0)
        inputs = [ sock ]
        outputs = [ sock ]
        partial = []

        while self.do_process_msgs:
            # without this sleep, I was getting very consistent socket errors
            # on Windows. Perhaps we don't need this sleep on other platforms.
            time.sleep(self.poll_socket_sleep_sec)

            if True: #try:
                # test our socket for readable, writable states.
                readable, writable, exceptional = select.select(inputs, outputs, inputs)

                for s in readable:
                    # print("waiting to recv")
                    try:
                        data = s.recv(1024 * 64)
                    except ConnectionAbortedError:
                        print("socket connection aborted")
                        self.do_process_msgs = False
                        break
                    
                    # we don't technically need to convert from bytes to string
                    # for json.loads, but we do need a string in order to do
                    # the split by \n newline char. This seperates each json msg.
                    data = data.decode("utf-8")
                    msgs = data.split("\n")

                    for m in msgs:
                        if len(m) < 2:
                            continue
                        last_char = m[-1]
                        first_char = m[0]
                        # check first and last char for a valid json terminator
                        # if not, then add to our partial packets list and see
                        # if we get the rest of the packet on our next go around.                
                        if first_char == "{" and last_char == '}':
                            # Replace comma with dots for floats
                            # useful when using unity in a language different from English
                            m = replace_float_notation(m)
                            j = json.loads(m)
                            self.on_msg_recv(j)
                        else:
                            partial.append(m)
                            if last_char == '}':
                                if partial[0][0] == "{":
                                    assembled_packet = "".join(partial)
                                    assembled_packet = replace_float_notation(assembled_packet)
                                    j = json.loads(assembled_packet)
                                    self.on_msg_recv(j)
                                else:
                                    print("failed packet.")
                                partial.clear()
                        
                for s in writable:
                    if self.msg != None:
                        # print("sending", self.msg)
                        s.sendall(self.msg.encode("utf-8"))
                        self.msg = None
                if len(exceptional) > 0:
                    print("problems w sockets!")

            #except Exception as e:
            #    print("Exception:", e)
            #    self.aborted = True
            #    self.on_msg_recv({"msg_type" : "aborted"})
            #    break


class RaceClient(SDClient):
    

    def __init__(self, model, address, conf, poll_socket_sleep_time=0.01):
        super().__init__(*address, poll_socket_sleep_time=poll_socket_sleep_time)
        self.last_image = None
        self.car_loaded = False
        self.model = model
        self.conf = conf

    def on_msg_recv(self, json_packet):
        #print("got", json_packet['msg_type'])

        if not json_packet.get('msg_type', ''):
            json_packet['msg_type'] = ''

        if json_packet['msg_type'] == "need_car_config":
            self.send_config(self.conf)

        if json_packet['msg_type'] == "car_loaded":
            self.car_loaded = True
        
        if json_packet['msg_type'] == "telemetry":
            imgString = json_packet["image"]
            image = Image.open(BytesIO(base64.b64decode(imgString)))
            self.last_image = np.asarray(image).astype(np.float32) * IMG_NORM_SCALE
            ### print("got a new image")

    def extract_keys(self, dct, lst):
        ret_dct = {}
        for key in lst:
            if key in dct:
                ret_dct[key] = dct[key]
        return ret_dct

    def send_controls(self, steering, throttle):
        print("sending controls", steering, throttle)
        p = { "msg_type" : "control",
                "steering" : steering.__str__(),
                "throttle" : throttle.__str__(),
                "brake" : "0.0" }
        msg = json.dumps(p)
        self.send(msg)

    def send_config(self, conf):
        self.set_car_config(conf)
        self.set_racer_bio(conf)
        cam_config = self.extract_keys(conf, ["img_w", "img_h", "img_d", "img_enc", "fov", "fish_eye_x", "fish_eye_y", "offset_x", "offset_y", "offset_z", "rot_x"])
        self.send_cam_config(**cam_config)

    def set_car_config(self, conf):
        if "body_style" in conf :
            self.send_car_config(conf["body_style"], conf["body_rgb"], conf["car_name"], conf["font_size"])

    def set_racer_bio(self, conf):
        self.conf = conf
        if "bio" in conf :
            self.send_racer_bio(conf["racer_name"], conf["car_name"], conf["bio"], conf["country"])

    def send_car_config(self, body_style, body_rgb, car_name, font_size):
        """
        # body_style = "donkey" | "bare" | "car01" choice of string
        # body_rgb  = (128, 128, 128) tuple of ints
        # car_name = "string less than 64 char"
        """
        msg = {'msg_type': 'car_config',
            'body_style': body_style,
            'body_r' : body_rgb[0].__str__(),
            'body_g' : body_rgb[1].__str__(),
            'body_b' : body_rgb[2].__str__(),
            'car_name': car_name,
            'font_size' : font_size.__str__() }
        self.blocking_send(msg)
        time.sleep(0.1)

    def send_racer_bio(self, racer_name, car_name, bio, country):
        # body_style = "donkey" | "bare" | "car01" choice of string
        # body_rgb  = (128, 128, 128) tuple of ints
        # car_name = "string less than 64 char"
        msg = {'msg_type': 'racer_info',
            'racer_name': racer_name,
            'car_name' : car_name,
            'bio' : bio,
            'country' : country }
        self.blocking_send(msg)
        time.sleep(0.1)

    def send_cam_config(self, img_w=0, img_h=0, img_d=0, img_enc=0, fov=0, fish_eye_x=0, fish_eye_y=0, offset_x=0, offset_y=0, offset_z=0, rot_x=0):
        """ Camera config
            set any field to Zero to get the default camera setting.
            offset_x moves camera left/right
            offset_y moves camera up/down
            offset_z moves camera forward/back
            rot_x will rotate the camera
            with fish_eye_x/y == 0.0 then you get no distortion
            img_enc can be one of JPG|PNG|TGA
        """
        msg = {"msg_type" : "cam_config",
               "fov" : str(fov),
               "fish_eye_x" : str(fish_eye_x),
               "fish_eye_y" : str(fish_eye_y),
               "img_w" : str(img_w),
               "img_h" : str(img_h),
               "img_d" : str(img_d),
               "img_enc" : str(img_enc),
               "offset_x" : str(offset_x),
               "offset_y" : str(offset_y),
               "offset_z" : str(offset_z),
               "rot_x" : str(rot_x) }
        self.blocking_send(msg)
        time.sleep(0.1)

    def blocking_send(self, p):
        msg = json.dumps(p)
        self.send_now(msg)

    def update(self):
        if self.last_image is not None:
            outputs = self.model.predict(self.last_image[None, :, :, :])
            steering = outputs[0][0][0]
            throttle = outputs[1][0][0]
            self.send_controls(steering, throttle)


def race(model_path, host, name):

    # Load keras model
    model = keras.models.load_model(model_path)

    conf = { "body_style" : "donkey", 
        "body_rgb" : (64, 64, 64),
        "car_name" : name,
        "racer_name" : "Your Name",
        "country" : "Mars",
        "bio" : "I race robots!",
        "font_size" : "100"
        }

    # Create client
    client = RaceClient(model, address=(host, PORT), conf=conf)

    # load scene
    msg = '{ "msg_type" : "load_scene", "scene_name" : "mountain_track" }'
    client.send(msg)
    time.sleep(1.0)

    # Car config
    
    client.send(msg)
    time.sleep(0.2)
    
    try:
        while True:
            client.update()
            time.sleep(0.01)

    except KeyboardInterrupt:
        pass

    client.stop()

if __name__ == '__main__':
    import tensorflow
    config = tensorflow.compat.v1.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tensorflow.compat.v1.Session(config=config)
    sess.as_default()

    args = docopt(__doc__)
    race(model_path = args['--model'], host = args['--host'], name = args['--name'])