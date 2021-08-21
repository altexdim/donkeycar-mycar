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
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.28 lap_time=29.28
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.70 lap_time=27.42
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.60 lap_time=27.90
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=112.43 lap_time=27.83
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=140.35 lap_time=27.92
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=168.03 lap_time=27.68


#memory with bad data 60hz
python train.py --model models/mypilot_circuit_launch_25.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat --type=memory

python train.py --model models/mypilot_circuit_launch_27.h5 --tubs=data/tub_70_fast --type=rnn
python manage.py drive --model models/mypilot_circuit_launch_27.h5 --myconfig=myconfig-trnm-local.py --type=rnn


