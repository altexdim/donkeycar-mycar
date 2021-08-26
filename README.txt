#############################################################

### https://docs.google.com/forms/d/e/1FAIpQLSeswIvCSXduiZs4rP4l-W49fxfyXS6nCyAWm_G-l3osLXTB8Q/viewform?edit2=2_ABaOnueOBswBkns2hiLE1WC0TN__xV7z1rYmu3w9WnMj5m3QcWVwj2e0ZzQntBB61XEdcNA

python train.py --model models/mypilot3.h5 --tubs=data
python train.py --model models/mypilot4.h5 --tubs=data/tub_2_21-06-25
python manage.py drive --model models/mypilot3.h5

####### generated GOOD ###########

python train.py --model models/mypilot_5.h5 --tubs=data/donkey-generated-track-v0-1
python manage.py drive --model models/mypilot_5.h5

python train.py --model models/mypilot_6.h5 --tubs=data/donkey-warehouse-v0-1
python manage.py drive --model models/mypilot_6.h5

python train.py --model models/mypilot_8.h5 --tubs=data/donkey-generated-roads-v0-2
python manage.py drive --model models/mypilot_8.h5

####### warehouse GOOD ###########

python train.py --model models/mypilot_9.h5 --tubs=data/donkey-warehouse-v0-2
python manage.py drive --model models/mypilot_9.h5

python train.py --model models/mypilot_11.h5 --tubs=data/donkey-generated-roads-v0-4
python manage.py drive --model models/mypilot_11.h5

python train.py --model models/mypilot_12.h5 --tubs=data/donkey-avc-sparkfun-v0-1
python manage.py drive --model models/mypilot_12.h5

####### roboracingleague GOOD MID ###########

python train.py --model models/mypilot_14.h5 --tubs=data/donkey-roboracingleague-track-v0-1  --type=categorical
python manage.py drive --model models/mypilot_14.h5  --type=categorical

# tensorflow models: (linear|categorical|behavior)

####### waveshare GOOD ###########

python train.py --model models/mypilot_18.h5 --tubs=data/donkey-waveshare-v0-1
python manage.py drive --model models/mypilot_18.h5

python train.py --model models/mypilot_19.h5 --tubs=data/donkey-minimonaco-track-v0-1
python manage.py drive --model models/mypilot_19.h5

python train.py --model models/mypilot_22.h5 --tubs=data/donkey-minimonaco-track-v0-2
python manage.py drive --model models/mypilot_22.h5

python train.py --model models/mypilot_23.h5 --tubs=data/donkey-warren-track-v0-1
python manage.py drive --model models/mypilot_23.h5

## tournament
python manage.py drive --model models/mypilot_23.h5 --myconfig=myconfig-trnm.py
python manage.py drive --model models/mypilot_24.h5 --myconfig=myconfig-trnm.py
python manage.py drive --model models/mypilot_31.h5 --myconfig=myconfig-trnm.py

python train.py --model models/mypilot_24.h5 --tubs=data/donkey-warren-track-v0-2
python manage.py drive --model models/mypilot_24.h5

python train.py --model models/mypilot_25.h5 --tubs=data/american_steel_adam_2,data/american_steel_oak_data3_adam,data/athena_rainer_bosch,data/aws_reinvient_adam,data/circuit_launch_adam_1,data/circuit_launch_ed_1,data/circuit_launch_ed_2,data/donkey-generated-track-v0-1,data/donkey-minimonaco-track-v0-1,data/donkey-minimonaco-track-v0-2,data/donkey-roboracingleague-track-v0-1,data/donkey-warehouse-v0-2,data/donkey-warren-track-v0-1,data/donkey-warren-track-v0-2,data/donkey-waveshare-v0-1,data/driveai_data3_adam,data/driveway_120fov_leftlane,data/google_io_adam_1,data/hive_cone_avoid,data/hive_cone_avoid_2,data/hive_cone_avoid_3,data/hive_fast_driving,data/hive_fast_driving_2,data/hive_imu_fast_racing,data/hive_imu_fast_racing_2,data/hive_imu_left_lane_in_traffic,data/hive_left_lane_driving,data/hive_ps3_cam,data/hive_right_lane_driving,data/hive_wandering_in_traffic,data/mapbox_locate_adam_1,data/san_mateo_maker_faire_adam,data/sd_history_center_llane_1,data/sd_history_center_llane_2,data/sd_history_center_llane_avoid,data/seattle_hackathon_adam,data/sim_gen_roads_pid_1_rl,data/sim_gen_roads_pid_2_rl,data/sim_warehouse_manual,data/ucsd_afternoon,data/ucsd_avg_drv,data/ucsd_fast_track,data/ucsd_mid_morn,data/ucsd_morn,data/ucsd_oscillate,data/ucsd_outdoor_track_1,data/ucsd_slow_driving

python train.py --model models/mypilot_28.h5 --tubs=data/sim_warehouse_manual
python manage.py drive --model models/mypilot_28.h5

python train.py --model models/mypilot_27.h5 --tubs=data/sim_gen_roads_pid_1_rl,data/sim_gen_roads_pid_2_rl
python manage.py drive --model models/mypilot_27.h5





python train.py --model models/mypilot_29.h5 --tubs=data/donkey-generated-track-v0-1,data/donkey-minimonaco-track-v0-1,data/donkey-minimonaco-track-v0-2,data/donkey-roboracingleague-track-v0-1,data/donkey-warehouse-v0-2,data/donkey-warren-track-v0-1,data/donkey-warren-track-v0-2,data/donkey-waveshare-v0-1
python train.py --model models/mypilot_30.h5 --tubs=data/donkey-warren-track-v0-1,data/donkey-warren-track-v0-2
python manage.py drive --model models/mypilot_30.h5


####### WARREN GOOD ###########
python manage.py drive
python train.py --model models/mypilot_31.h5 --tubs=data/donkey-warren-track-v0-1,data/donkey-warren-track-v0-2,data/donkey-warren-track-v0-3,data/donkey-warren-track-v0-4,data/donkey-warren-track-v0-5,data/donkey-warren-track-v0-6
python manage.py drive --model models/mypilot_31.h5


####### MINIMONACO GOOD ###########
python manage.py drive
python train.py --model models/mypilot_32.h5 --tubs=data/donkey-minimonaco-track-v0-3,data/donkey-minimonaco-track-v0-4,data/donkey-minimonaco-track-v0-5
python manage.py drive --model models/mypilot_32.h5

####### thunderhill GOOD ###########
python manage.py drive
python train.py --model models/mypilot_33.h5 --tubs=data/donkey-thunderhill-track-v0-1,data/donkey-thunderhill-track-v0-2,data/donkey-thunderhill-track-v0-3
python manage.py drive --model models/mypilot_33.h5

####### WARREN + MINIMONACO GOOD MID ###########
python manage.py drive
python train.py --model models/mypilot_35.h5 --tubs=data/donkey-warren-track-v0-7,data/donkey-warren-track-v0-8,data/donkey-warren-track-v0-9
python manage.py drive --model models/mypilot_35.h5
python train.py --model models/mypilot_36.h5 --tubs=data/donkey-warren-track-v0-7,data/donkey-warren-track-v0-8,data/donkey-warren-track-v0-9,data/donkey-minimonaco-track-v0-3,data/donkey-minimonaco-track-v0-4,data/donkey-minimonaco-track-v0-5
python manage.py drive --model models/mypilot_36.h5

####### TOURNAMENT PROG ###########
# ??? # python manage.py drive --model models/mypilot_31.h5 --myconfig=myconfig-trnm.py
# ! GOOD # python manage.py drive --model models/mypilot_35.h5 --myconfig=myconfig-trnm.py
# GOOD # python manage.py drive --model models/mypilot_36.h5 --myconfig=myconfig-trnm.py
# OK # python manage.py drive --model models/mypilot_23.h5 --myconfig=myconfig-trnm.py
# BAD # python manage.py drive --model models/mypilot_24.h5 --myconfig=myconfig-trnm.py



####### donkey-roboracingleague-track-v0 good ###########
python manage.py drive
python train.py --model models/mypilot_37.h5 --tubs=data/donkey-roboracingleague-track-v0-2,data/donkey-roboracingleague-track-v0-3,data/donkey-roboracingleague-track-v0-4
python manage.py drive --model models/mypilot_37.h5

####### donkey-warehouse-v0 good ###########
python manage.py drive
python train.py --model models/mypilot_38.h5 --tubs=data/donkey-warehouse-v0-3,data/donkey-warehouse-v0-4,data/donkey-warehouse-v0-5
python manage.py drive --model models/mypilot_38.h5
















(donkey) C:\donkeycar\projects\mysim>python train.py --model models/mypilot.h5 --tubs=data
________             ______                   _________
___  __ \_______________  /___________  __    __  ____/_____ ________
__  / / /  __ \_  __ \_  //_/  _ \_  / / /    _  /    _  __ `/_  ___/
_  /_/ // /_/ /  / / /  ,<  /  __/  /_/ /     / /___  / /_/ /_  /
/_____/ \____//_/ /_//_/|_| \___/_\__, /      \____/  \__,_/ /_/
                                 /____/

using donkey v4.2.1 ...
2021-06-24 23:59:48.579703: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
2021-06-24 23:59:48.579786: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
loading config file: C:\donkeycar\projects\mysim\config.py
loading personal config over-rides from myconfig.py
"get_model_by_type" model Type is: linear
Created KerasLinear
2021-06-24 23:59:50.175920: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library nvcuda.dll
2021-06-24 23:59:50.208099: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1561] Found device 0 with properties:
pciBusID: 0000:01:00.0 name: NVIDIA GeForce RTX 2080 Ti computeCapability: 7.5
coreClock: 1.755GHz coreCount: 68 deviceMemorySize: 11.00GiB deviceMemoryBandwidth: 573.69GiB/s
2021-06-24 23:59:50.208718: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
2021-06-24 23:59:50.210512: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cublas64_10.dll'; dlerror: cublas64_10.dll not found
2021-06-24 23:59:50.213191: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cufft64_10.dll
2021-06-24 23:59:50.219856: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library curand64_10.dll
2021-06-24 23:59:50.226457: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cusolver64_10.dll
2021-06-24 23:59:50.227086: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cusparse64_10.dll'; dlerror: cusparse64_10.dll not found
2021-06-24 23:59:50.227673: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cudnn64_7.dll'; dlerror: cudnn64_7.dll not found
2021-06-24 23:59:50.228134: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1598] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2021-06-24 23:59:50.228666: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
2021-06-24 23:59:50.238902: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x28100e20990 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-06-24 23:59:50.238977: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2021-06-24 23:59:50.240001: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2021-06-24 23:59:50.240195: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]
Model: "model"



ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
tensorflow 2.2.0 requires gast==0.3.3, but you have gast 0.4.0 which is incompatible.
tensorflow 2.2.0 requires h5py<2.11.0,>=2.10.0, but you have h5py 3.1.0 which is incompatible.
tensorflow-gpu 2.2.0 requires gast==0.3.3, but you have gast 0.4.0 which is incompatible.
tensorflow-gpu 2.2.0 requires h5py<2.11.0,>=2.10.0, but you have h5py 3.1.0 which is incompatible.
pytorch-lightning 1.3.7 requires fsspec[http]!=2021.06.0,>=2021.05.0, but you have fsspec 2021.6.0 which is incompatible.

----------------

####### donkey-circuit-launch-track-v0 ###########
python manage.py drive

#all,first attempt
python train.py --model models/mypilot_circuit_launch.h5 --tubs=data/tub_1_21-07-26
python train.py --model models/mypilot_circuit_launch_2.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_4_edge_left_side_25pc,data/tub_5_drunk_25pc,data/tub_6_recover_25pc

# bad - drunk (oscillating)
python manage.py drive --model models/mypilot_circuit_launch_2.h5

# bad+ (tending outside the edge) - with recover
python train.py --model models/mypilot_circuit_launch_3.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_4_edge_left_side_25pc,data/tub_6_recover_25pc
python manage.py drive --model models/mypilot_circuit_launch_3.h5

# bad- (bad internal loop) - no edge
python train.py --model models/mypilot_circuit_launch_4.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_6_recover_25pc
python manage.py drive --model models/mypilot_circuit_launch_4.h5

# good? - no recover
python train.py --model models/mypilot_circuit_launch_5.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_4_edge_left_side_25pc
python manage.py drive --model models/mypilot_circuit_launch_5.h5

# good! - no edge, no recover, slow
python train.py --model models/mypilot_circuit_launch_6.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc
python manage.py drive --model models/mypilot_circuit_launch_6.h5

# race!
python manage.py drive --model models/mypilot_circuit_launch_6.h5 --myconfig=myconfig-trnm.py

# good+ - no edge, no recover, more data
python train.py --model models/mypilot_circuit_launch_7.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_7_manual_race_100pc
python manage.py drive --model models/mypilot_circuit_launch_7.h5
python manage.py drive --model models/mypilot_circuit_launch_7.h5 --myconfig=myconfig-trnm.py

# bad-- - all+more data
python train.py --model models/mypilot_circuit_launch_8.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_4_edge_left_side_25pc,data/tub_5_drunk_25pc,data/tub_6_recover_25pc,data/tub_7_manual_race_100pc
python manage.py drive --model models/mypilot_circuit_launch_8.h5

# good- - nodrunk+more data
python train.py --model models/mypilot_circuit_launch_9.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_4_edge_left_side_25pc,data/tub_6_recover_25pc,data/tub_7_manual_race_100pc
python manage.py drive --model models/mypilot_circuit_launch_9.h5

# bad+ - nodrunk,noedge+more data
python train.py --model models/mypilot_circuit_launch_10.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_6_recover_25pc,data/tub_7_manual_race_100pc
python manage.py drive --model models/mypilot_circuit_launch_10.h5

# good+ - nodrunk,noedge,noslow+more data+recover
python train.py --model models/mypilot_circuit_launch_11.h5 --tubs=data/tub_6_recover_25pc,data/tub_7_manual_race_100pc
python manage.py drive --model models/mypilot_circuit_launch_11.h5

# race2!
python manage.py drive --model models/mypilot_circuit_launch_11.h5 --myconfig=myconfig-trnm.py

# RISKY bad/good - as fast as possible, with collisions
python train.py --model models/mypilot_circuit_launch_12.h5 --tubs=data/tub_8_fast
python manage.py drive --model models/mypilot_circuit_launch_12.h5

# RISKY race3 + 10 seconds bools launch
python manage.py drive --model models/mypilot_circuit_launch_12.h5 --myconfig=myconfig-trnm.py

# bad - as fast as possible, with collisions, + some good data
python train.py --model models/mypilot_circuit_launch_13.h5 --tubs=data/tub_6_recover_25pc,data/tub_7_manual_race_100pc,data/tub_8_fast
python manage.py drive --model models/mypilot_circuit_launch_13.h5

# bad- - a lot data
python train.py --model models/mypilot_circuit_launch_14.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_4_edge_left_side_25pc,data/tub_5_drunk_25pc,data/tub_6_recover_25pc,data/tub_7_manual_race_100pc,data/tub_8_fast
python manage.py drive --model models/mypilot_circuit_launch_14.h5

# bad- - a lot data, no drunk
python train.py --model models/mypilot_circuit_launch_15.h5 --tubs=data/tub_1_right_side_25pc,data/tub_2_left_side_25pc,data/tub_3_mid_side_25pc,data/tub_4_edge_left_side_25pc,data/tub_6_recover_25pc,data/tub_7_manual_race_100pc,data/tub_8_fast
python manage.py drive --model models/mypilot_circuit_launch_15.h5

# good++ - 20ms/60hz, fast
python train.py --model models/mypilot_circuit_launch_16.h5 --tubs=data/tub_9_fast_ll
python manage.py drive --model models/mypilot_circuit_launch_16.h5
python manage.py drive --model models/mypilot_circuit_launch_16.h5 --myconfig=myconfig-trnm.py

### test in docker with local sim and custom config without saving in docker build
docker run -it --rm --network host -v "C:/donkeycar/projects/diyrobocar_docker_agent_pln/myrace":/root/myrace altexdim/donkeycar_race2:v1 bash -c "cd /root/myrace/ && python3 /root/myrace/manage.py drive --model /root/myrace/models/mypilot_circuit_launch_16.h5 --myconfig=myconfig-trnm-local.py"
docker-compose -f ./pln-docker-compose.yml up --build
docker-compose -f ./pln-docker-compose.yml up

# good? - no ping, 60hz, fast
python manage.py drive
python train.py --model models/mypilot_circuit_launch_17.h5 --tubs=data/tub_10_fast_nolat
python manage.py drive --model models/mypilot_circuit_launch_17.h5 --myconfig=myconfig-trnm-local.py
python train.py --model models/mypilot_circuit_launch_18.h5 --tubs=data/tub_11_fast_nolat
python manage.py drive --model models/mypilot_circuit_launch_18.h5 --myconfig=myconfig-trnm-local.py
python train.py --model models/mypilot_circuit_launch_19.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat
python manage.py drive --model models/mypilot_circuit_launch_19.h5 --myconfig=myconfig-trnm-local.py

docker run -it --rm --network host -v "C:/donkeycar/projects/diyrobocar_docker_agent_pln/myrace":/root/myrace altexdim/donkeycar_race2:v2 bash -c "cd /root/myrace/ && python3 /root/myrace/manage.py drive --model /root/myrace/models/mypilot_circuit_launch_19.h5 --myconfig=myconfig-trnm-local.py"
docker run -it --rm --network host altexdim/donkeycar_race2:v3 bash -c "cd /root/myrace/ && python3 /root/myrace/manage.py drive --model /root/myrace/models/mypilot_circuit_launch_19.h5 --myconfig=myconfig-trnm-local.py"
docker run -it --rm --network host altexdim/donkeycar_race2:v2 bash -c "cd /root/myrace/ && python3 /root/myrace/manage.py drive --model /root/myrace/models/mypilot_circuit_launch_19.h5 --myconfig=myconfig-trnm-local.py"
docker push altexdim/donkeycar_race2:v2

docker run -it --rm --network host altexdim/donkeycar_race2:v2
docker run -it --rm --network host altexdim/donkeycar_race2:v2 bash -c "cd /root/myrace/ && python3 /root/myrace/manage.py drive --model /root/myrace/models/mypilot_circuit_launch_19.h5 --myconfig=myconfig-trnm.py"

docker pull altexdim/donkeycar_race2:v2


docker run -it --rm --network host -v "C:/donkeycar/projects/diyrobocar_docker_agent_pln/myrace":/root/myrace altexdim/donkeycar_race2:v3 bash -c "cd /root/myrace/ && python3 /root/myrace/test.py"

#  - no ping, 60hz, fast, DEV, 3D
python train.py --model models/mypilot_circuit_launch_20.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat --type=3d

python train.py --model models/mypilot_circuit_launch_21.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat
###donkey makemovie --tub=data/tub_10_fast_nolat --out=tub_movie.mp4 --model=models/mypilot_circuit_launch_21.h5 --type=linear --start=0 --end=10 --scale=5 --salient
python train.py --model models/mypilot_circuit_launch_22.h5 --tubs=data/tub_10_fast_nolat --type=3d

#############################################################

# movie with vector
donkey makemovie --tub=data/tub_1_21-07-26 --out=tub_movie.mp4 --model=models/mypilot_circuit_launch.h5
donkey makemovie --tub=data/tub_1_21-07-26 --out=tub_movie.mp4 --model=models/mypilot_circuit_launch.h5 --type=linear --start=0 --end=-1 --scale=2
donkey makemovie --tub=data/tub_1_21-07-26 --out=tub_movie.mp4 --model=models/mypilot_circuit_launch.h5 --type=linear --start=0 --end=10 --scale=2
donkey makemovie --tub=data/tub_1_21-07-26 --out=tub_movie.mp4 --model=models/mypilot_circuit_launch.h5 --type=linear --start=0 --end=10 --scale=5
# -- not working --
# donkey makemovie --tub=data/tub_1_21-07-26 --out=tub_movie.mp4 --model=models/mypilot_circuit_launch.h5 --type=linear --start=0 --end=10 --scale=5 --salient

# check cnn activations
donkey cnnactivations --model=models/mypilot_circuit_launch.h5 --image data/tub_1_21-07-26/images/8_cam_image_array_.jpg

15 Aug 2021
-----------
python train.py --model models/mypilot_circuit_launch_23.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat
python manage.py drive --model models/mypilot_circuit_launch_23.h5 --myconfig=myconfig-trnm-local.py
experimental_new_converter=False
python train.py --model models/mypilot_circuit_launch_24.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat --type=3d
donkey makemovie --tub=data/tub_10_fast_nolat --out=tub_movie.mp4 --model=models/mypilot_circuit_launch_23.h5 --type=linear --start=0 --end=10 --scale=2 --salient

# added AUG + TRANSFORM
python train.py --model models/mypilot_circuit_launch_26.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat
python manage.py drive --model models/mypilot_circuit_launch_26.h5
donkey makemovie --tub=data/tub_10_fast_nolat --out=tub_movie.mp4 --model=models/mypilot_circuit_launch_26.h5 --start=0 --end=1000 --scale=5 --salient
# added 3D
python train.py --model models/mypilot_circuit_launch_27.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat --type=3d
# python manage.py drive --model models/mypilot_circuit_launch_27.h5 --type=3d
# donkey makemovie --tub=data/tub_10_fast_nolat --out=tub_movie.mp4 --model=models/mypilot_circuit_launch_27.h5 --type=3d --start=0 --end=3000 --scale=5 --salient

16 Aug 2021
-----------
# RNN
python train.py --model models/mypilot_circuit_launch_28.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat --type=rnn
python manage.py drive --model models/mypilot_circuit_launch_26.h5 --myconfig=myconfig-trnm-local.py
python manage.py drive --model models/mypilot_circuit_launch_28.h5 --myconfig=myconfig-trnm-local.py --type=rnn
donkey makemovie --tub=data/tub_10_fast_nolat --out=tub_movie28.mp4 --model=models/mypilot_circuit_launch_28.h5 --type=rnn --start=0 --end=3000 --scale=5 --salient

17 Aug 2021
-----------
python train.py --model models/mypilot_circuit_launch_29.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat --type=memory
python manage.py drive --model models/mypilot_circuit_launch_29.h5 --myconfig=myconfig-trnm-local.py --type=memory
python manage.py drive

18 Aug 2021
-----------
python manage.py drive
python train.py --model models/circuit_launch_30.h5 --tubs=data/tub_1_21-08-18
python manage.py drive --model models/circuit_launch_30.h5 --myconfig=myconfig-trnm-local.py

19 Aug 2021
-----------
python manage.py drive
python train.py --model models/mypilot_circuit_launch_19_2.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat
python manage.py drive --model models/mypilot_circuit_launch_19_2.h5 --myconfig=myconfig-trnm-local.py

20 Aug 2021
-----------
python manage.py drive --model models/mypilot_circuit_launch_19_2.h5 --myconfig=myconfig-trnm-local.py
    30:20 57:94 85:90
    29:52 57:80 85:18
    29:20 56:74 84:29

python manage.py drive
python train.py --model models/mypilot_circuit_launch_20.h5 --tubs=data/tub_70_fast
python manage.py drive --model models/mypilot_circuit_launch_20.h5 --myconfig=myconfig-trnm-local.py

#test blur
python train.py --model models/mypilot_circuit_launch_21.h5 --tubs=data/tub_70_fast --type=linear
#test 3d
python train.py --model models/mypilot_circuit_launch_22.h5 --tubs=data/tub_70_fast --type=3d
#test rnn
python train.py --model models/mypilot_circuit_launch_23.h5 --tubs=data/tub_70_fast --type=rnn
#test memory
python train.py --model models/mypilot_circuit_launch_24.h5 --tubs=data/tub_70_fast --type=memory
python manage.py drive --model models/mypilot_circuit_launch_24.h5 --myconfig=myconfig-trnm-local.py --type=memory
    29:10 56:98 84:23
    29:26 56:75 84:45
    29:40 56:84 84:49 

#memory with bad data 60hz
python train.py --model models/mypilot_circuit_launch_25.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat --type=memory

python train.py --model models/mypilot_circuit_launch_27.h5 --tubs=data/tub_70_fast --type=rnn
python manage.py drive --model models/mypilot_circuit_launch_27.h5 --myconfig=myconfig-trnm-local.py --type=rnn

21 Aug 2021
-----------
python manage.py drive --model models/mypilot_circuit_launch_24.h5 --myconfig=myconfig-trnm-local.py --type=memory
    lap_number=1 total_time=29.42 lap_time=29.42
    lap_number=2 total_time=57.15 lap_time=27.73
    lap_number=3 total_time=84.61 lap_time=27.45

    lap_number=1 total_time=30.41 lap_time=30.41
    lap_number=2 total_time=57.82 lap_time=27.41
    lap_number=3 total_time=85.53 lap_time=27.70

    lap_number=1 total_time=29.82 lap_time=29.82
    lap_number=2 total_time=57.24 lap_time=27.41
    lap_number=3 total_time=85.02 lap_time=27.78

python manage.py drive --model models/mypilot_circuit_launch_19_2.h5 --myconfig=myconfig-trnm-local.py
    lap_number=1 total_time=29.26 lap_time=29.26
    lap_number=2 total_time=57.06 lap_time=27.80
    lap_number=3 total_time=84.65 lap_time=27.59

    lap_number=1 total_time=29.86 lap_time=29.86
    lap_number=2 total_time=57.48 lap_time=27.62
    lap_number=3 total_time=85.95 lap_time=28.47

    lap_number=1 total_time=29.82 lap_time=29.82
    lap_number=2 total_time=57.64 lap_time=27.82
    lap_number=3 total_time=85.76 lap_time=28.12

22 Aug 2021
-----------
python manage.py drive --model models/mypilot_circuit_launch_19_2.h5 --myconfig=myconfig-trnm-local.py
python manage.py drive --model models/mypilot_circuit_launch_24.h5 --myconfig=myconfig-trnm-local.py --type=memory

23 Aug 2021
-----------
collect more data
python manage.py drive
- data/tub_134_21-08-24_fast

24 Aug 2021
-----------
altex@Altex-Home-PC:~$ cat /home/altex/.ssh/donkeysim_race_real.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIA1tKNEbrfMYNFA+mowibvS8g6CddWlX3QUtNg9KLREy d.ananyev@gmail.com

altexdim/donkeycar_race2

collect more data
python manage.py drive
- data/tub_135_21-08-24_fast
- data/tub_137_21-08-24_fast
- data/tub_138_21-08-24_fast

collect edge cases data - soft recovery
- data/tub_139_21-08-24_soft_recovery
- data/tub_140_21-08-24_soft_recovery

collect danger cases data - hard recovery
- data/tub_141_21-08-24_hard_recovery
- data/tub_142_21-08-24_hard_recovery
- data/tub_143_21-08-24_outline
- data/tub_144_21-08-24_hard_recovery


python train.py\
 --model models/mypilot_circuit_launch_30.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_139_21-08-24_soft_recovery,\
data/tub_140_21-08-24_soft_recovery,\
data/tub_141_21-08-24_hard_recovery,\
data/tub_142_21-08-24_hard_recovery,\
data/tub_143_21-08-24_outline,\
data/tub_144_21-08-24_hard_recovery\
 --type=memory

python manage.py drive --model models/mypilot_circuit_launch_30.h5 --myconfig=myconfig-trnm-local.py --type=memory

---- very bad - unable to finish 1 lap

===================================================

python train.py --model models/mypilot_circuit_launch_31.h5 --tubs=data/tub_70_fast,data/tub_134_21-08-24_fast,data/tub_135_21-08-24_fast,data/tub_137_21-08-24_fast,data/tub_138_21-08-24_fast --type=memory

python manage.py drive --model models/mypilot_circuit_launch_31.h5 --myconfig=myconfig-trnm-local.py --type=memory

>>> very good - sometimes fails on the 2nd turn, but in general better than 24 memory model - because no doubleturns around internal cone

----------
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.56 lap_time=29.56
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.20 lap_time=27.64
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.49 lap_time=27.29
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=111.76 lap_time=27.27
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=138.98 lap_time=27.22
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=167.25 lap_time=28.27
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=7 total_time=195.48 lap_time=28.23
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=8 total_time=222.61 lap_time=27.13
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=9 total_time=251.59 lap_time=28.98
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=10 total_time=278.70 lap_time=27.11
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=11 total_time=305.96 lap_time=27.26
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=12 total_time=332.69 lap_time=26.73
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=13 total_time=359.79 lap_time=27.10
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=14 total_time=387.66 lap_time=27.87
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=15 total_time=415.26 lap_time=27.60
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=16 total_time=442.35 lap_time=27.09
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=17 total_time=469.60 lap_time=27.25
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=18 total_time=497.25 lap_time=27.65
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=19 total_time=524.69 lap_time=27.44
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=20 total_time=552.30 lap_time=27.61
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=21 total_time=579.23 lap_time=26.93
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=22 total_time=606.24 lap_time=27.01
CRASH ON 2nd turn
----------

------------------
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.66 lap_time=28.66
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.35 lap_time=26.69
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.33 lap_time=27.98
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=110.95 lap_time=27.62
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=137.28 lap_time=26.33
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=164.40 lap_time=27.12
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=7 total_time=192.34 lap_time=27.93
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=8 total_time=219.47 lap_time=27.13
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=9 total_time=247.32 lap_time=27.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=10 total_time=275.19 lap_time=27.86
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=11 total_time=301.90 lap_time=26.71
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=12 total_time=328.74 lap_time=26.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=13 total_time=356.42 lap_time=27.67
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=14 total_time=384.20 lap_time=27.79
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=15 total_time=411.24 lap_time=27.03
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=16 total_time=438.31 lap_time=27.07
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=17 total_time=465.51 lap_time=27.21
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=18 total_time=492.78 lap_time=27.26
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=19 total_time=520.00 lap_time=27.23
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=20 total_time=546.76 lap_time=26.76
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=21 total_time=574.08 lap_time=27.32
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=22 total_time=600.83 lap_time=26.75
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=23 total_time=627.63 lap_time=26.80
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=24 total_time=654.77 lap_time=27.14
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=25 total_time=682.28 lap_time=27.51
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=26 total_time=711.17 lap_time=28.89
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=27 total_time=738.11 lap_time=26.93
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=28 total_time=765.16 lap_time=27.05
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=29 total_time=793.10 lap_time=27.94
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=30 total_time=820.72 lap_time=27.62
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=31 total_time=847.66 lap_time=26.94
------------------

===================================================

---- lets train with 12/.0000001 batch 1280 ----

python train.py\
 --model models/mypilot_circuit_launch_32.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast\
 --type=memory

python manage.py drive --model models/mypilot_circuit_launch_32.h5 --myconfig=myconfig-trnm-local.py --type=memory

>>> failed to run a lap

===================================================

---- lets train with 12/.0000001 ----

python train.py\
 --model models/mypilot_circuit_launch_33.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast\
 --type=memory

python manage.py drive --model models/mypilot_circuit_launch_33.h5 --myconfig=myconfig-trnm-local.py --type=memory

>>> failed to run a lap

--- debug no cuda on inference ---
donkey tubplot --tub=data/tub_70_fast --model=models/mypilot_circuit_launch_33.h5 --type=memory
--- uses GPU

===============================
only soft recovery
---- lets train with 5/.0005 ----

python train.py\
 --model models/mypilot_circuit_launch_38.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_139_21-08-24_soft_recovery,\
data/tub_140_21-08-24_soft_recovery\
 --type=memory

python manage.py drive --model models/mypilot_circuit_launch_38.h5 --myconfig=myconfig-trnm-local.py --type=memory

>>> very bad, now even one lap

===============================
only hard recovery
---- lets train with 5/.0005 ----

python train.py\
 --model models/mypilot_circuit_launch_40.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_141_21-08-24_hard_recovery,\
data/tub_142_21-08-24_hard_recovery,\
data/tub_144_21-08-24_hard_recovery\
 --type=memory

python manage.py drive --model models/mypilot_circuit_launch_40.h5 --myconfig=myconfig-trnm-local.py --type=memory

>>> very bad, now even one lap

===============================
only outline
---- lets train with 5/.0005 ----

python train.py\
 --model models/mypilot_circuit_launch_45.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_143_21-08-24_outline\
 --type=memory

python manage.py drive --model models/mypilot_circuit_launch_45.h5 --myconfig=myconfig-trnm-local.py --type=memory

>>> very bad, slow, 2 laps and crash
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.95 lap_time=30.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=61.29 lap_time=30.34
CRASH

===============================
only good data
---- lets train with 5/.0005 ----

python train.py\
 --model models/mypilot_circuit_launch_46.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast\
 --type=memory

python manage.py drive --model models/mypilot_circuit_launch_46.h5 --myconfig=myconfig-trnm-local.py --type=memory

>>> bad

===============================
all data
---- lets train with 12/.0000001 ----

python train.py\
 --model models/mypilot_circuit_launch_50.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_139_21-08-24_soft_recovery,\
data/tub_140_21-08-24_soft_recovery,\
data/tub_141_21-08-24_hard_recovery,\
data/tub_142_21-08-24_hard_recovery,\
data/tub_143_21-08-24_outline,\
data/tub_144_21-08-24_hard_recovery\
 --type=memory

>>> bad
 
===============================
all data, linear
---- lets train with 5/.0001 ----

python train.py\
 --model models/mypilot_circuit_launch_52.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_139_21-08-24_soft_recovery,\
data/tub_140_21-08-24_soft_recovery,\
data/tub_141_21-08-24_hard_recovery,\
data/tub_142_21-08-24_hard_recovery,\
data/tub_143_21-08-24_outline,\
data/tub_144_21-08-24_hard_recovery

python manage.py drive --model models/mypilot_circuit_launch_52.h5 --myconfig=myconfig-trnm-local.py

INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.59 lap_time=29.59
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.42 lap_time=26.83
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.79 lap_time=27.37
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=111.35 lap_time=27.55
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=145.25 lap_time=33.90
WEAK - 2 loops
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=173.02 lap_time=27.77
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=7 total_time=200.33 lap_time=27.31

> quite good; has weaknesses, fast, maybe needs more training; performas poorly without catapult
 
===============================
best data, linear
---- lets train with 5/.0005 ----

python train.py\
 --model models/mypilot_circuit_launch_53.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast
 

python manage.py drive --model models/mypilot_circuit_launch_53.h5 --myconfig=myconfig-trnm-local.py

INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.30 lap_time=29.30
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.78 lap_time=26.48
CRASH

> failed to finish 3 laps

donkey makemovie --tub=data/tub_10_fast_nolat --out=tub_movie53.mp4 --model=models/mypilot_circuit_launch_53.h5 --start=0 --end=1000 --scale=5 --salient

===============================
best data, linear
---- lets train with 12/.0000001 ----

python train.py\
 --model models/mypilot_circuit_launch_54.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast

python manage.py drive --model models/mypilot_circuit_launch_54.h5 --myconfig=myconfig-trnm-local.py

INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
AiLauncher is deactivated by duration 01:18:08.410553
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.65 lap_time=28.65
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.57 lap_time=26.93
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.49 lap_time=27.91
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=110.69 lap_time=27.20
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=137.64 lap_time=26.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=164.74 lap_time=27.10
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=7 total_time=191.71 lap_time=26.96
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=8 total_time=218.99 lap_time=27.28
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=9 total_time=245.81 lap_time=26.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=10 total_time=272.76 lap_time=26.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=11 total_time=300.06 lap_time=27.30
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=12 total_time=333.53 lap_time=33.47
LOOP?
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=13 total_time=361.08 lap_time=27.55
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=14 total_time=388.93 lap_time=27.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=15 total_time=415.80 lap_time=26.87
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=16 total_time=442.75 lap_time=26.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=17 total_time=469.80 lap_time=27.05
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=18 total_time=497.21 lap_time=27.40
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=19 total_time=524.48 lap_time=27.27
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=20 total_time=551.26 lap_time=26.78
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=21 total_time=578.41 lap_time=27.15
CRASH

---
AI_THROTTLE_MULT = 0.9
---

INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.42 lap_time=28.42
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.57 lap_time=26.15
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=80.75 lap_time=26.18
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=106.60 lap_time=25.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=132.25 lap_time=25.65
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=158.35 lap_time=26.10
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=7 total_time=184.54 lap_time=26.18
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=8 total_time=210.54 lap_time=26.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=9 total_time=237.06 lap_time=26.52
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=10 total_time=263.03 lap_time=25.97
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=11 total_time=289.62 lap_time=26.59
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=12 total_time=315.39 lap_time=25.77
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=13 total_time=341.89 lap_time=26.50
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=14 total_time=368.15 lap_time=26.25
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=15 total_time=393.91 lap_time=25.76
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=16 total_time=419.38 lap_time=25.47
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=17 total_time=445.32 lap_time=25.93
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=18 total_time=471.80 lap_time=26.48
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=19 total_time=498.06 lap_time=26.26
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=20 total_time=524.47 lap_time=26.41
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=21 total_time=550.32 lap_time=25.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=22 total_time=576.26 lap_time=25.93
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=23 total_time=602.39 lap_time=26.13
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=24 total_time=628.82 lap_time=26.43
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=25 total_time=655.51 lap_time=26.69
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=26 total_time=682.11 lap_time=26.60
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=27 total_time=708.78 lap_time=26.67
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=28 total_time=734.87 lap_time=26.09
CRASH on the S-cone

>>> very good, the fastest

===============================
-- TODO with soft recovery, linear
---- lets train with 5/.0005 ----

python train.py\
 --model models/mypilot_circuit_launch_55.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_139_21-08-24_soft_recovery,\
data/tub_140_21-08-24_soft_recovery

python manage.py drive --model models/mypilot_circuit_launch_55.h5 --myconfig=myconfig-trnm-local.py

===============================
with soft recovery, linear
---- lets train with 12/.0000001 ----

python train.py\
 --model models/mypilot_circuit_launch_56.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_139_21-08-24_soft_recovery,\
data/tub_140_21-08-24_soft_recovery

python manage.py drive --model models/mypilot_circuit_launch_56.h5 --myconfig=myconfig-trnm-local.py

>>> bad

===============
26 Aug 2021
---------------

-------------------------------------
only best data, memory, 12/.0000001
-------------------------------------
python train.py --model models/mypilot_circuit_launch_57.h5 --tubs=data/tub_70_fast,data/tub_134_21-08-24_fast,data/tub_135_21-08-24_fast,data/tub_137_21-08-24_fast,data/tub_138_21-08-24_fast --type=memory

python manage.py drive --model models/mypilot_circuit_launch_57.h5 --myconfig=myconfig-trnm-local.py --type=memory
python manage.py drive --model models/mypilot_circuit_launch_57.tflite --myconfig=myconfig-trnm-local.py --type=tflite_memory

>> bad

python train.py --model models/mypilot_circuit_launch_58.h5  --tubs=data/tub_70_fast --type=memory
python manage.py drive --model models/mypilot_circuit_launch_58.tflite --myconfig=myconfig-trnm-local.py --type=tflite_memory

>> bad

# 12/.0000001
python train.py --model models/mypilot_circuit_launch_59.h5 --tubs=data/tub_70_fast,data/tub_134_21-08-24_fast,data/tub_135_21-08-24_fast,data/tub_137_21-08-24_fast,data/tub_138_21-08-24_fast --type=memory

python manage.py drive --model models/mypilot_circuit_launch_59.h5 --myconfig=myconfig-trnm-local.py --type=memory

python train.py --model models/mypilot_circuit_launch_60.h5 --tubs=data/tub_70_fast,data/tub_134_21-08-24_fast,data/tub_135_21-08-24_fast,data/tub_137_21-08-24_fast,data/tub_138_21-08-24_fast --type=memory

python manage.py drive --model models/mypilot_circuit_launch_60.h5 --myconfig=myconfig-trnm-local.py --type=memory

# 12/.0000001
python train.py --model models/mypilot_circuit_launch_61.h5 --tubs=data/tub_70_fast,data/tub_134_21-08-24_fast,data/tub_135_21-08-24_fast,data/tub_137_21-08-24_fast,data/tub_138_21-08-24_fast --type=memory

# 12/.0005
python train.py --model models/mypilot_circuit_launch_61.h5 --tubs=data/tub_70_fast,data/tub_134_21-08-24_fast,data/tub_135_21-08-24_fast,data/tub_137_21-08-24_fast,data/tub_138_21-08-24_fast --type=memory

---
 1193  lspci | grep VGA
 1194  ls -la /sys/bus/pci/devices/*/numa_node
 1195  ls -la /sys/bus/pci/devices/0000:01:00.0/numa_node
 1197  echo 0 |  sudo tee -a  /sys/bus/pci/devices/0000:01:00.0/numa_node
---

python manage.py drive --model models/mypilot_circuit_launch_61.h5 --myconfig=myconfig-trnm-local.py --type=memory
>>> bad

# 5/.0005
python train.py --model models/mypilot_circuit_launch_62.h5 --tubs=data/tub_70_fast,data/tub_134_21-08-24_fast,data/tub_135_21-08-24_fast,data/tub_137_21-08-24_fast,data/tub_138_21-08-24_fast --type=memory

python manage.py drive --model models/mypilot_circuit_launch_62.h5 --myconfig=myconfig-trnm-local.py --type=memory
>>> bad



python manage.py drive --model models/mypilot_circuit_launch_31.h5 --myconfig=myconfig-trnm-local.py --type=memory
>>> good
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.99 lap_time=29.99
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.17 lap_time=27.19
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.96 lap_time=26.79

python convert.py --h5=models/mypilot_circuit_launch_31.h5 --tflite=models/mypilot_circuit_launch_31.tflite
python manage.py drive --model models/mypilot_circuit_launch_31.tflite --myconfig=myconfig-trnm-local.py --type=tflite_memory
>>> good
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.50 lap_time=29.50
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.17 lap_time=27.67
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.20 lap_time=27.03

python manage.py drive --model models/mypilot_circuit_launch_54.h5 --myconfig=myconfig-trnm-local-0_9.py
>>> good, smoother than tflite, but I dont like how it hits the right wall on 2nd turn on 1 lap
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.84 lap_time=28.84
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.79 lap_time=25.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=81.29 lap_time=26.50

python manage.py drive --model models/mypilot_circuit_launch_54.tflite --myconfig=myconfig-trnm-local-0_9.py --type=tflite_linear
>>> good, even faster, faster driving, faster inferense
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=27.74 lap_time=27.74
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.14 lap_time=26.40
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=80.35 lap_time=26.21


~~~~TODO/IDEAS/LEARNINGS/BUGS~~~~
- best data - 5/.0005 linear
- best data - 5/.0005 linear, throttle 0.9
- best data - 12/.0000001 linear
- best data - 12/.0000001 linear, throttle 0.9
- best data - 5/.0005 memory
- drive 1 line + 2 line + mid line, then transfer model to race dataset
-- try inference with GPU acceleration
-- try rt model for inference
-- drive backward from a cone helps for linear model only
-- blur helps for linear but model performs slower, worth trying with throttle 1.1, worth trying with memory
-- 12/.0000001 overfits memory model, 5/.0005 is better
-- try different augmentations, not only blur/brightness
--- tflite is faster for inference, not accurate (2x faster on AVG)
--- memory model can handle first turn on lower speed
---- video is not working with CROP
---- inference is not using GPU
---- simulation sometimes runs slow - slowing down PC, restart of simulation helps
