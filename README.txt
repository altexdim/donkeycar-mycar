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

for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_19_2.h5 --myconfig=myconfig-trnm-local.py --type=linear 2>&1 | grep -i 'lap_number\|Keras' ; done
>>> stable, not fastest, 0/10 CRASH, 0/10 BAD

INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.07 lap_time=30.07
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.47 lap_time=27.39
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.69 lap_time=27.22
|    KerasLinear     | 27.78 | 3.88 | 5.51 | 4.66 | 7.44 | 20.83 | 26.98 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.17 lap_time=30.17
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.65 lap_time=27.48
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.40 lap_time=27.75
|    KerasLinear     | 25.55 | 3.83 | 5.61 | 4.69 | 7.58 | 22.34 | 24.83 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.27 lap_time=29.27
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.93 lap_time=27.66
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.23 lap_time=27.30
|    KerasLinear     | 26.15 | 3.80 | 5.54 | 4.74 | 7.16 | 19.83 | 25.48 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.38 lap_time=30.38
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.90 lap_time=27.53
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.40 lap_time=27.50
|    KerasLinear     | 27.83 | 3.75 | 5.59 | 4.64 | 7.64 | 22.36 | 25.13 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.37 lap_time=29.37
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.69 lap_time=27.31
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.24 lap_time=27.55
|    KerasLinear     | 26.21 | 3.83 | 5.66 | 4.71 | 7.52 | 22.82 | 25.01 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.95 lap_time=29.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.98 lap_time=27.03
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.16 lap_time=27.18
|    KerasLinear     | 26.60 | 3.84 | 5.77 | 4.87 | 7.50 | 22.68 | 25.40 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.31 lap_time=29.31
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.19 lap_time=27.88
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.65 lap_time=27.46
|    KerasLinear     | 24.89 | 3.82 | 5.49 | 4.73 | 7.30 | 17.82 | 24.53 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.55 lap_time=29.55
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.99 lap_time=27.44
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.49 lap_time=27.50
|    KerasLinear     | 26.50 | 3.84 | 5.34 | 4.58 | 7.01 | 18.62 | 24.66 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.87 lap_time=29.87
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.55 lap_time=27.68
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.97 lap_time=27.42
|    KerasLinear     | 28.10 | 3.89 | 5.51 | 4.76 | 7.13 | 17.51 | 25.27 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_19_2.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.78 lap_time=29.78
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.08 lap_time=27.30
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.13 lap_time=27.05
|    KerasLinear     | 26.06 | 3.75 | 5.58 | 4.79 | 7.11 | 21.57 | 24.03 |


python manage.py drive --model models/mypilot_circuit_launch_19_2.h5 --myconfig=myconfig-trnm-local.py
    30:20 57:94 85:90
    29:52 57:80 85:18
    29:20 56:74 84:29

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


python manage.py drive --model models/mypilot_circuit_launch_19_2.h5 --myconfig=myconfig-trnm-local.py

----------------------------------------------------------------------------------------

20 Aug 2021
-----------

python manage.py drive
python train.py --model models/mypilot_circuit_launch_20.h5 --tubs=data/tub_70_fast
python manage.py drive --model models/mypilot_circuit_launch_20.h5 --myconfig=myconfig-trnm-local.py

#test blur
python train.py --model models/mypilot_circuit_launch_21.h5 --tubs=data/tub_70_fast --type=linear
#test 3d
python train.py --model models/mypilot_circuit_launch_22.h5 --tubs=data/tub_70_fast --type=3d
#test rnn
python train.py --model models/mypilot_circuit_launch_23.h5 --tubs=data/tub_70_fast --type=rnn


---------------------------------------------------------------------------------

#test memory
python train.py --model models/mypilot_circuit_launch_24.h5 --tubs=data/tub_70_fast --type=memory
python manage.py drive --model models/mypilot_circuit_launch_24.h5 --myconfig=myconfig-trnm-local.py --type=memory
    29:10 56:98 84:23
    29:26 56:75 84:45
    29:40 56:84 84:49 

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

python manage.py drive --model models/mypilot_circuit_launch_24.h5 --myconfig=myconfig-trnm-local.py --type=memory

for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_24.h5 --myconfig=myconfig-trnm-local.py --type=memory 2>&1 | grep -i 'lap_number\|Keras' ; done

>>> 1/10 Bad

INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.13 lap_time=29.13
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.78 lap_time=27.66
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.48 lap_time=26.70
|    KerasMemory     | 30.59 | 4.75 | 6.43 | 5.59 | 8.36 | 18.66 | 29.39 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.02 lap_time=29.02
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.26 lap_time=27.24
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.56 lap_time=27.29
|    KerasMemory     | 33.09 | 4.73 | 6.82 | 5.84 | 8.90 | 24.62 | 29.93 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.30 lap_time=29.30
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.13 lap_time=27.83
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.64 lap_time=27.51
|    KerasMemory     | 30.51 | 4.77 | 6.60 | 5.65 | 8.49 | 22.93 | 30.02 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.62 lap_time=29.62
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.02 lap_time=27.40
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.62 lap_time=27.59
|    KerasMemory     | 32.01 | 4.76 | 6.50 | 5.65 | 8.17 | 23.02 | 29.67 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.60 lap_time=29.60
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.05 lap_time=27.45
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.34 lap_time=27.28
|    KerasMemory     | 32.16 | 4.76 | 6.80 | 5.83 | 8.96 | 23.93 | 30.38 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.68 lap_time=29.68
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.93 lap_time=27.25
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.28 lap_time=27.35
|    KerasMemory     | 32.36 | 4.77 | 6.96 | 5.79 | 9.30 | 27.47 | 31.50 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.97 lap_time=28.97
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.21 lap_time=27.24
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.69 lap_time=27.49
|    KerasMemory     | 32.32 | 4.75 | 6.90 | 5.80 | 9.06 | 27.23 | 31.84 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=38.04 lap_time=38.04
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=65.76 lap_time=27.72
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=93.86 lap_time=28.10
|    KerasMemory     | 33.06 | 4.75 | 6.75 | 5.76 | 9.06 | 22.90 | 31.63 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.43 lap_time=29.43
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.13 lap_time=27.70
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.79 lap_time=27.67
|    KerasMemory     | 35.17 | 4.76 | 6.80 | 5.69 | 8.77 | 27.52 | 31.59 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_24.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.82 lap_time=29.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.38 lap_time=27.57
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.70 lap_time=27.32
|    KerasMemory     | 32.11 | 4.64 | 6.73 | 5.79 | 8.86 | 22.80 | 29.91 |


--------------------------------------------------------------------------------------

#memory with bad data 60hz
python train.py --model models/mypilot_circuit_launch_25.h5 --tubs=data/tub_10_fast_nolat,data/tub_11_fast_nolat --type=memory

python train.py --model models/mypilot_circuit_launch_27.h5 --tubs=data/tub_70_fast --type=rnn
python manage.py drive --model models/mypilot_circuit_launch_27.h5 --myconfig=myconfig-trnm-local.py --type=rnn

21 Aug 2021
-----------


22 Aug 2021
-----------

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

for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_31.h5 --myconfig=myconfig-trnm-local.py --type=memory 2>&1 | grep -i 'lap_number\|Keras' ; done

>>> not fastest, 1/10 CRASH

INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.89 lap_time=28.89
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.77 lap_time=26.89
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.96 lap_time=27.19
|    KerasMemory     | 32.73 | 4.74 | 6.68 | 5.75 | 8.59 | 22.58 | 30.20 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.08 lap_time=29.08
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.13 lap_time=27.05
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.77 lap_time=27.63
|    KerasMemory     | 31.86 | 4.71 | 6.79 | 5.63 | 8.83 | 28.11 | 31.14 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.77 lap_time=28.77
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.17 lap_time=27.40
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.76 lap_time=27.59
|    KerasMemory     | 31.85 | 4.74 | 6.45 | 5.56 | 8.18 | 21.88 | 30.22 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.62 lap_time=29.62
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.97 lap_time=27.35
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.18 lap_time=27.20
|    KerasMemory     | 31.23 | 4.67 | 6.51 | 5.46 | 8.42 | 25.67 | 30.92 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.84 lap_time=28.84
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.95 lap_time=28.11
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.14 lap_time=28.19
|    KerasMemory     | 31.45 | 4.77 | 6.44 | 5.53 | 7.82 | 24.42 | 30.45 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.14 lap_time=29.14
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.15 lap_time=28.01
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.04 lap_time=27.89
|    KerasMemory     | 30.04 | 4.78 | 5.88 | 5.44 | 6.28 | 18.87 | 29.48 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.61 lap_time=29.61
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.55 lap_time=27.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.51 lap_time=26.95
|    KerasMemory     | 30.88 | 4.68 | 6.30 | 5.47 | 7.45 | 23.06 | 30.56 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.26 lap_time=30.26
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.22 lap_time=26.96
|    KerasMemory     | 32.66 | 4.76 | 6.79 | 5.78 | 8.95 | 25.20 | 30.78 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.57 lap_time=29.57
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.94 lap_time=28.37
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.89 lap_time=26.95
|    KerasMemory     | 32.36 | 4.78 | 6.57 | 5.63 | 8.57 | 23.72 | 32.07 |
INFO:donkeycar.parts.keras:Creating memory model with length 3, depth 0
INFO:donkeycar.parts.keras:Created KerasMemory-L:3-D:0 with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_31.h5
INFO:donkeycar.parts.keras:Loaded memory model with mem length 3
INFO:donkeycar.vehicle:Adding part KerasMemory.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=27.64 lap_time=27.64
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.93 lap_time=27.29
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.79 lap_time=27.86
|    KerasMemory     | 29.80 | 4.69 | 6.58 | 5.57 | 8.80 | 20.90 | 29.43 |


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

python manage.py drive --model models/mypilot_circuit_launch_31.tflite --myconfig=myconfig-trnm-local.py --type=tflite_memory
>>> good
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.44 lap_time=29.44
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.21 lap_time=26.77
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.95 lap_time=26.74
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=110.69 lap_time=27.74
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=137.48 lap_time=26.79
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=164.25 lap_time=26.77
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=7 total_time=191.57 lap_time=27.32
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=8 total_time=218.47 lap_time=26.90
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=9 total_time=245.99 lap_time=27.52
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=10 total_time=272.71 lap_time=26.72
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=11 total_time=300.75 lap_time=28.04
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=12 total_time=328.03 lap_time=27.28
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=13 total_time=356.26 lap_time=28.23
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=14 total_time=384.06 lap_time=27.81
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=15 total_time=411.12 lap_time=27.05
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=16 total_time=438.17 lap_time=27.05
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=17 total_time=465.44 lap_time=27.27
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=18 total_time=493.22 lap_time=27.78
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=19 total_time=520.61 lap_time=27.39
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=20 total_time=549.36 lap_time=28.76
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=21 total_time=577.83 lap_time=28.47
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=22 total_time=604.95 lap_time=27.12
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=23 total_time=631.99 lap_time=27.04
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=24 total_time=658.82 lap_time=26.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=25 total_time=686.88 lap_time=28.07
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=26 total_time=714.27 lap_time=27.39
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=27 total_time=742.41 lap_time=28.14
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=28 total_time=769.64 lap_time=27.23
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=29 total_time=797.31 lap_time=27.67
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=30 total_time=825.09 lap_time=27.78
CRASH

^CINFO:donkeycar.vehicle:Shutting down vehicle and its parts...
INFO:donkeycar.vehicle:Part Profile Summary: (times in ms)
INFO:donkeycar.vehicle:
+--------------------+-------+------+------+------+------+-------+-------+
|        part        |  max  | min  | avg  | 50%  | 90%  |  99%  | 99.9% |
+--------------------+-------+------+------+------+------+-------+-------+
|    DonkeyGymEnv    |  0.34 | 0.01 | 0.02 | 0.01 | 0.05 |  0.07 |  0.08 |
| LocalWebController |  0.44 | 0.00 | 0.01 | 0.01 | 0.03 |  0.04 |  0.05 |
|   ThrottleFilter   |  0.11 | 0.00 | 0.01 | 0.00 | 0.01 |  0.02 |  0.03 |
|   PilotCondition   |  0.15 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
|   RecordTracker    |  0.35 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
|    FileWatcher     |  1.10 | 0.01 | 0.02 | 0.01 | 0.04 |  0.08 |  0.14 |
|    FileWatcher     |  1.15 | 0.00 | 0.01 | 0.00 | 0.02 |  0.04 |  0.08 |
|   DelayedTrigger   |  0.34 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
| TriggeredCallback  |  0.06 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.01 |
| ImageAugmentation  |  5.45 | 0.39 | 0.90 | 0.55 | 2.30 |  3.10 |  3.83 |
|    KerasMemory     | 15.33 | 1.40 | 3.04 | 2.13 | 7.57 | 10.72 | 11.63 |
|     DriveMode      |  0.53 | 0.01 | 0.02 | 0.02 | 0.06 |  0.09 |  0.11 |
|     AiCatapult     |  0.39 | 0.00 | 0.01 | 0.00 | 0.01 |  0.02 |  0.03 |
|   AiRunCondition   |  0.13 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
+--------------------+-------+------+------+------+------+-------+-------+


python manage.py drive --model models/mypilot_circuit_launch_31.h5 --myconfig=myconfig-trnm-local.py --type=memory
>>> okay

INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.67 lap_time=28.67
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.04 lap_time=26.37
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.99 lap_time=27.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=109.86 lap_time=26.87
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=136.67 lap_time=26.80
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=164.17 lap_time=27.50
CRASH
^CINFO:donkeycar.vehicle:Shutting down vehicle and its parts...
INFO:donkeycar.vehicle:Part Profile Summary: (times in ms)
INFO:donkeycar.vehicle:
+--------------------+-------+------+------+------+------+-------+-------+
|        part        |  max  | min  | avg  | 50%  | 90%  |  99%  | 99.9% |
+--------------------+-------+------+------+------+------+-------+-------+
|    DonkeyGymEnv    |  0.57 | 0.01 | 0.02 | 0.01 | 0.05 |  0.07 |  0.08 |
| LocalWebController |  0.17 | 0.00 | 0.01 | 0.01 | 0.02 |  0.04 |  0.05 |
|   ThrottleFilter   |  0.09 | 0.00 | 0.00 | 0.00 | 0.01 |  0.02 |  0.02 |
|   PilotCondition   |  0.03 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.01 |
|   RecordTracker    |  0.03 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.01 |
|    FileWatcher     |  0.56 | 0.01 | 0.02 | 0.01 | 0.03 |  0.06 |  0.14 |
|    FileWatcher     |  0.10 | 0.00 | 0.01 | 0.00 | 0.01 |  0.03 |  0.07 |
|   DelayedTrigger   |  0.04 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
| TriggeredCallback  |  0.05 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.01 |
| ImageAugmentation  |  5.00 | 0.42 | 0.76 | 0.54 | 1.18 |  2.80 |  3.59 |
|    KerasMemory     | 32.81 | 4.66 | 6.83 | 5.71 | 9.16 | 27.05 | 31.03 |
|     DriveMode      |  0.25 | 0.01 | 0.02 | 0.01 | 0.02 |  0.05 |  0.08 |
|     AiCatapult     |  0.07 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
|   AiRunCondition   |  0.02 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.01 |
+--------------------+-------+------+------+------+------+-------+-------+

INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=27.98 lap_time=27.98
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.71 lap_time=26.73
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.50 lap_time=27.79
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=111.15 lap_time=28.65
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=139.30 lap_time=28.15
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=166.15 lap_time=26.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=7 total_time=193.48 lap_time=27.33
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=8 total_time=220.72 lap_time=27.24
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=9 total_time=248.06 lap_time=27.34
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=10 total_time=276.16 lap_time=28.10
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=11 total_time=303.83 lap_time=27.67
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=12 total_time=330.65 lap_time=26.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=13 total_time=358.30 lap_time=27.65
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=14 total_time=385.46 lap_time=27.16
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=15 total_time=411.86 lap_time=26.40
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=16 total_time=439.01 lap_time=27.14
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=17 total_time=466.68 lap_time=27.68
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=18 total_time=493.56 lap_time=26.88
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=19 total_time=521.01 lap_time=27.45
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=20 total_time=548.01 lap_time=27.01
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=21 total_time=575.18 lap_time=27.17
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=22 total_time=602.38 lap_time=27.20
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=23 total_time=629.32 lap_time=26.93
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=24 total_time=656.04 lap_time=26.73
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=25 total_time=683.64 lap_time=27.60
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=26 total_time=711.14 lap_time=27.51
CRASH
^CINFO:donkeycar.vehicle:Shutting down vehicle and its parts...
INFO:donkeycar.vehicle:Part Profile Summary: (times in ms)
INFO:donkeycar.vehicle:
+--------------------+-------+------+------+------+------+-------+-------+
|        part        |  max  | min  | avg  | 50%  | 90%  |  99%  | 99.9% |
+--------------------+-------+------+------+------+------+-------+-------+
|    DonkeyGymEnv    |  0.29 | 0.01 | 0.02 | 0.01 | 0.05 |  0.07 |  0.08 |
| LocalWebController |  0.24 | 0.00 | 0.01 | 0.01 | 0.02 |  0.04 |  0.05 |
|   ThrottleFilter   |  0.19 | 0.00 | 0.00 | 0.00 | 0.01 |  0.02 |  0.02 |
|   PilotCondition   |  0.16 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.02 |
|   RecordTracker    |  0.04 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.01 |
|    FileWatcher     |  0.62 | 0.01 | 0.02 | 0.01 | 0.02 |  0.06 |  0.12 |
|    FileWatcher     |  1.14 | 0.00 | 0.01 | 0.00 | 0.01 |  0.03 |  0.08 |
|   DelayedTrigger   |  0.39 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.02 |
| TriggeredCallback  |  0.07 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.01 |
| ImageAugmentation  |  4.88 | 0.42 | 0.73 | 0.53 | 1.03 |  2.74 |  3.76 |
|    KerasMemory     | 33.97 | 4.65 | 6.66 | 5.68 | 8.82 | 23.67 | 30.47 |
|     DriveMode      |  0.22 | 0.01 | 0.02 | 0.01 | 0.02 |  0.04 |  0.08 |
|     AiCatapult     |  0.26 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
|   AiRunCondition   |  0.16 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.01 |
+--------------------+-------+------+------+------+------+-------+-------+


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
all data, linear, 5/.0005
-------------------------------

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
 

for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_52.h5 --myconfig=myconfig-trnm-local.py 2>&1 | grep -i 'lap_number\|Keras' ; done

>>> not good, 2/10 BAD

INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=36.07 lap_time=36.07
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=62.89 lap_time=26.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=90.36 lap_time=27.47
|    KerasLinear     | 25.31 | 3.77 | 5.29 | 4.51 | 6.79 | 19.52 | 24.33 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.29 lap_time=29.29
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.16 lap_time=26.87
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.46 lap_time=27.30
|    KerasLinear     | 28.09 | 3.84 | 5.08 | 4.46 | 6.21 | 18.66 | 23.64 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.31 lap_time=30.31
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.96 lap_time=27.66
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.00 lap_time=27.04
|    KerasLinear     | 26.04 | 3.74 | 5.28 | 4.47 | 6.80 | 21.38 | 23.78 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=35.69 lap_time=35.69
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=63.02 lap_time=27.34
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=89.79 lap_time=26.77
|    KerasLinear     | 25.76 | 3.80 | 5.50 | 4.65 | 7.33 | 21.45 | 24.67 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=31.13 lap_time=31.13
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=58.40 lap_time=27.27
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.61 lap_time=27.22
|    KerasLinear     | 27.53 | 3.87 | 5.69 | 4.77 | 7.88 | 21.54 | 26.13 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.93 lap_time=29.93
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.14 lap_time=27.22
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.49 lap_time=27.34
|    KerasLinear     | 26.41 | 3.82 | 5.73 | 4.75 | 7.56 | 23.41 | 25.12 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.48 lap_time=29.48
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.36 lap_time=27.88
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.37 lap_time=28.00
|    KerasLinear     | 25.93 | 3.80 | 5.50 | 4.70 | 7.27 | 19.59 | 25.52 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.02 lap_time=30.02
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.57 lap_time=27.55
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.34 lap_time=27.77
|    KerasLinear     | 27.00 | 3.83 | 5.48 | 4.72 | 7.13 | 19.10 | 26.54 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.59 lap_time=29.59
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.08 lap_time=27.49
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.23 lap_time=28.15
|    KerasLinear     | 26.63 | 3.83 | 5.63 | 4.75 | 7.31 | 22.97 | 26.00 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.87 lap_time=29.87
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.19 lap_time=27.32
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.88 lap_time=26.70
|    KerasLinear     | 25.69 | 3.78 | 5.43 | 4.62 | 7.27 | 19.10 | 24.58 |


for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_52.h5 --myconfig=myconfig-trnm-local-0_9.py 2>&1 | grep -i 'lap_number\|Keras' ; done
>>> stable, good, not fastest, can recover???, 0/10 CRASH, 0/10 BAD

INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.95 lap_time=28.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.98 lap_time=28.03
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.97 lap_time=27.99
|    KerasLinear     | 26.44 | 3.85 | 5.62 | 4.79 | 7.23 | 22.96 | 25.41 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.68 lap_time=28.68
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.65 lap_time=27.98
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.53 lap_time=27.88
|    KerasLinear     | 25.67 | 3.88 | 5.59 | 4.63 | 7.77 | 21.13 | 25.02 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.60 lap_time=28.60
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.00 lap_time=28.40
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.91 lap_time=26.91
|    KerasLinear     | 26.07 | 3.82 | 5.70 | 4.77 | 7.34 | 22.18 | 24.23 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.63 lap_time=28.63
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.66 lap_time=28.03
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.49 lap_time=27.83
|    KerasLinear     | 25.90 | 3.83 | 5.65 | 4.73 | 7.47 | 22.59 | 24.56 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.80 lap_time=28.80
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.77 lap_time=27.97
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.62 lap_time=27.85
|    KerasLinear     | 25.34 | 3.90 | 5.46 | 4.75 | 7.08 | 18.67 | 24.84 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.47 lap_time=28.47
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.12 lap_time=27.65
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.67 lap_time=27.55
|    KerasLinear     | 25.58 | 3.79 | 5.57 | 4.65 | 7.42 | 21.70 | 25.12 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.45 lap_time=28.45
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.41 lap_time=27.96
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.05 lap_time=28.64
|    KerasLinear     | 30.56 | 3.77 | 5.65 | 4.66 | 7.57 | 23.22 | 25.77 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.22 lap_time=29.22
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.20 lap_time=27.98
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.50 lap_time=27.30
|    KerasLinear     | 26.80 | 3.86 | 5.53 | 4.69 | 7.38 | 17.52 | 26.58 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.76 lap_time=28.76
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.84 lap_time=28.08
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.52 lap_time=27.68
|    KerasLinear     | 26.89 | 3.85 | 5.68 | 4.69 | 7.67 | 22.56 | 25.83 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_52.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.82 lap_time=28.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.21 lap_time=27.39
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.47 lap_time=28.26
|    KerasLinear     | 25.51 | 3.83 | 5.62 | 4.78 | 7.25 | 22.18 | 24.30 |



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
best data, linear, 12/.0000001
-------------------------------

python train.py\
 --model models/mypilot_circuit_launch_54.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast

python manage.py drive --model models/mypilot_circuit_launch_54.h5 --myconfig=myconfig-trnm-local.py
>>> not fastest, not good enough, 1/10 CRASH, 1/10 BAD

for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_54.h5 --myconfig=myconfig-trnm-local.py 2>&1 | grep -i 'lap_number\|Keras' ; done

INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.08 lap_time=30.08
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.87 lap_time=26.79
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.72 lap_time=26.85
|    KerasLinear     | 27.10 | 3.80 | 5.72 | 4.80 | 7.65 | 18.74 | 25.16 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.30 lap_time=29.30
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.29 lap_time=26.99
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.57 lap_time=27.29
|    KerasLinear     | 26.57 | 3.85 | 5.86 | 4.84 | 8.02 | 22.70 | 24.64 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.82 lap_time=28.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.80 lap_time=26.98
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.98 lap_time=28.18
|    KerasLinear     | 27.58 | 3.80 | 5.80 | 4.81 | 7.72 | 23.14 | 25.51 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.30 lap_time=29.30
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.06 lap_time=27.76
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.39 lap_time=27.33
|    KerasLinear     | 28.78 | 3.81 | 5.53 | 4.58 | 7.41 | 22.25 | 24.83 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.00 lap_time=28.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.26 lap_time=27.26
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.21 lap_time=26.95
|    KerasLinear     | 26.88 | 3.86 | 5.25 | 4.39 | 6.69 | 22.66 | 25.65 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=27.43 lap_time=27.43
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.02 lap_time=27.59
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.42 lap_time=27.40
|    KerasLinear     | 26.44 | 3.79 | 5.12 | 4.34 | 6.52 | 17.37 | 24.91 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.73 lap_time=28.73
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.03 lap_time=27.31
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.57 lap_time=27.53
|    KerasLinear     | 26.27 | 3.83 | 5.58 | 4.61 | 7.42 | 22.31 | 25.87 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.18 lap_time=29.18
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.68 lap_time=27.50
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.18 lap_time=27.50
|    KerasLinear     | 26.63 | 3.79 | 5.34 | 4.47 | 7.01 | 22.42 | 24.29 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=27.56 lap_time=27.56
|    KerasLinear     | 25.68 | 3.82 | 5.49 | 4.51 | 7.46 | 21.89 | 24.39 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=34.85 lap_time=34.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=62.08 lap_time=27.24
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=89.47 lap_time=27.39
|    KerasLinear     | 26.70 | 3.78 | 5.54 | 4.64 | 7.33 | 21.55 | 24.69 |


python manage.py drive --model models/mypilot_circuit_launch_54.h5 --myconfig=myconfig-trnm-local-0_9.py
>>> very good, the fastest (one weakness - 2nd turn - slightly hit the wall on the right; 1/10 BAD)

for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_54.h5 --myconfig=myconfig-trnm-local-0_9.py 2>&1 | grep -i 'lap_number\|Keras' ; done
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.52 lap_time=28.52
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.18 lap_time=26.66
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=81.31 lap_time=26.13
|    KerasLinear     | 24.83 | 3.69 | 5.81 | 4.77 | 8.13 | 22.56 | 24.49 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=27.72 lap_time=27.72
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.08 lap_time=26.37
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=80.70 lap_time=26.62
|    KerasLinear     | 26.44 | 3.80 | 5.64 | 4.83 | 7.45 | 19.84 | 25.38 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.64 lap_time=28.64
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.41 lap_time=26.77
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=81.61 lap_time=26.20
|    KerasLinear     | 25.29 | 3.81 | 5.82 | 4.71 | 7.66 | 22.74 | 24.77 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.67 lap_time=28.67
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.23 lap_time=26.56
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=81.86 lap_time=26.62
|    KerasLinear     | 30.33 | 3.82 | 5.79 | 4.83 | 7.78 | 23.03 | 25.75 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.57 lap_time=28.57
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.89 lap_time=26.32
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=81.79 lap_time=26.90
|    KerasLinear     | 26.35 | 3.81 | 5.91 | 4.92 | 8.05 | 22.47 | 25.31 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=41.47 lap_time=41.47
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=68.14 lap_time=26.67
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=94.94 lap_time=26.80
|    KerasLinear     | 26.94 | 3.82 | 5.79 | 4.83 | 7.89 | 21.82 | 24.69 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.64 lap_time=28.64
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.58 lap_time=26.94
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.18 lap_time=26.60
|    KerasLinear     | 27.90 | 3.83 | 5.72 | 4.71 | 7.68 | 22.44 | 26.88 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.70 lap_time=28.70
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.91 lap_time=26.20
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=81.31 lap_time=26.40
|    KerasLinear     | 25.43 | 3.84 | 5.81 | 4.84 | 7.70 | 21.87 | 25.06 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.41 lap_time=29.41
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.85 lap_time=26.44
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.08 lap_time=26.24
|    KerasLinear     | 27.33 | 3.83 | 5.83 | 4.90 | 7.79 | 22.48 | 25.32 |
INFO:donkeycar.parts.keras:Created KerasLinear with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_54.h5
INFO:donkeycar.vehicle:Adding part KerasLinear.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.27 lap_time=29.27
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.24 lap_time=25.97
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=81.61 lap_time=26.38
|    KerasLinear     | 28.04 | 3.91 | 5.81 | 4.76 | 7.95 | 22.77 | 25.77 |

python manage.py drive --model models/mypilot_circuit_launch_54.h5 --myconfig=myconfig-trnm-local-0_9.py --type=linear
>>> good
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=27.92 lap_time=27.92
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=53.94 lap_time=26.01
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=80.37 lap_time=26.43
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=106.20 lap_time=25.83
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=132.90 lap_time=26.70
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=159.16 lap_time=26.26
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=7 total_time=185.72 lap_time=26.56
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=8 total_time=211.94 lap_time=26.22
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=9 total_time=238.62 lap_time=26.68
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=10 total_time=265.01 lap_time=26.39
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=11 total_time=291.51 lap_time=26.50
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=12 total_time=317.89 lap_time=26.39
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=13 total_time=344.39 lap_time=26.50
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=14 total_time=370.66 lap_time=26.27
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=15 total_time=396.94 lap_time=26.28
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=16 total_time=423.34 lap_time=26.40
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=17 total_time=449.19 lap_time=25.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=18 total_time=475.56 lap_time=26.37
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=19 total_time=501.99 lap_time=26.43
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=20 total_time=527.72 lap_time=25.74
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=21 total_time=553.66 lap_time=25.94
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=22 total_time=579.98 lap_time=26.32
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=23 total_time=606.00 lap_time=26.02
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=24 total_time=632.50 lap_time=26.50
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=25 total_time=658.44 lap_time=25.94
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=26 total_time=684.99 lap_time=26.56
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=27 total_time=711.84 lap_time=26.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=28 total_time=738.36 lap_time=26.52
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=29 total_time=764.49 lap_time=26.13
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=30 total_time=791.03 lap_time=26.53
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=31 total_time=817.53 lap_time=26.50
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=32 total_time=843.33 lap_time=25.80
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=33 total_time=869.22 lap_time=25.89
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=34 total_time=895.22 lap_time=26.01
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=35 total_time=921.49 lap_time=26.26
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=36 total_time=947.79 lap_time=26.30
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=37 total_time=974.44 lap_time=26.65
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=38 total_time=1000.78 lap_time=26.34
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=39 total_time=1027.46 lap_time=26.68
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=40 total_time=1053.61 lap_time=26.14
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=41 total_time=1079.35 lap_time=25.74
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=42 total_time=1106.29 lap_time=26.94
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=43 total_time=1132.84 lap_time=26.56
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=44 total_time=1159.37 lap_time=26.52
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=45 total_time=1185.35 lap_time=25.99
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=46 total_time=1211.71 lap_time=26.36
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=47 total_time=1238.24 lap_time=26.53
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=48 total_time=1264.33 lap_time=26.08
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=49 total_time=1290.37 lap_time=26.04
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=50 total_time=1317.17 lap_time=26.80
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=51 total_time=1342.99 lap_time=25.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=52 total_time=1369.54 lap_time=26.55
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=53 total_time=1395.77 lap_time=26.24
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=54 total_time=1422.37 lap_time=26.60
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=55 total_time=1448.57 lap_time=26.20
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=56 total_time=1475.26 lap_time=26.68
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=57 total_time=1501.62 lap_time=26.36
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=58 total_time=1527.88 lap_time=26.26
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=59 total_time=1553.92 lap_time=26.05
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=60 total_time=1579.99 lap_time=26.06
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=61 total_time=1606.76 lap_time=26.77
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=62 total_time=1633.30 lap_time=26.54
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=63 total_time=1659.88 lap_time=26.58
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=64 total_time=1686.12 lap_time=26.24
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=65 total_time=1712.47 lap_time=26.35
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=66 total_time=1738.98 lap_time=26.51
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=67 total_time=1765.47 lap_time=26.49
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=68 total_time=1791.65 lap_time=26.19
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=69 total_time=1818.11 lap_time=26.46
CRASH
^CINFO:donkeycar.vehicle:Shutting down vehicle and its parts...
INFO:donkeycar.vehicle:Part Profile Summary: (times in ms)
INFO:donkeycar.vehicle:
+--------------------+-------+------+------+------+------+-------+-------+
|        part        |  max  | min  | avg  | 50%  | 90%  |  99%  | 99.9% |
+--------------------+-------+------+------+------+------+-------+-------+
|    DonkeyGymEnv    |  0.59 | 0.01 | 0.02 | 0.01 | 0.05 |  0.07 |  0.08 |
| LocalWebController |  0.54 | 0.00 | 0.01 | 0.01 | 0.02 |  0.04 |  0.05 |
|   ThrottleFilter   |  0.47 | 0.00 | 0.00 | 0.00 | 0.01 |  0.02 |  0.02 |
|   PilotCondition   |  0.06 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
|   RecordTracker    |  0.14 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.01 |
|    FileWatcher     |  1.21 | 0.01 | 0.02 | 0.01 | 0.04 |  0.07 |  0.14 |
|    FileWatcher     |  1.10 | 0.00 | 0.01 | 0.00 | 0.01 |  0.03 |  0.08 |
|   DelayedTrigger   |  0.19 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
| TriggeredCallback  |  0.46 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.01 |
| ImageAugmentation  |  5.13 | 0.42 | 0.77 | 0.55 | 1.29 |  2.82 |  3.77 |
|    KerasLinear     | 28.61 | 3.76 | 5.75 | 4.75 | 7.81 | 22.63 | 25.27 |
|     DriveMode      |  0.26 | 0.01 | 0.02 | 0.01 | 0.02 |  0.07 |  0.09 |
|     AiCatapult     |  0.35 | 0.00 | 0.00 | 0.00 | 0.01 |  0.02 |  0.03 |
|   AiRunCondition   |  0.07 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.01 |
+--------------------+-------+------+------+------+------+-------+-------+

python manage.py drive --model models/mypilot_circuit_launch_54.tflite --myconfig=myconfig-trnm-local-0_9.py --type=tflite_linear
>>> good
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=27.89 lap_time=27.89
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.54 lap_time=26.65
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=81.46 lap_time=26.92
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=107.68 lap_time=26.22
^CINFO:donkeycar.vehicle:Shutting down vehicle and its parts...
INFO:donkeycar.vehicle:Part Profile Summary: (times in ms)
INFO:donkeycar.vehicle:
+--------------------+-------+------+------+------+------+-------+-------+
|        part        |  max  | min  | avg  | 50%  | 90%  |  99%  | 99.9% |
+--------------------+-------+------+------+------+------+-------+-------+
|    DonkeyGymEnv    |  0.18 | 0.01 | 0.02 | 0.01 | 0.05 |  0.07 |  0.08 |
| LocalWebController |  0.04 | 0.00 | 0.01 | 0.01 | 0.02 |  0.03 |  0.04 |
|   ThrottleFilter   |  0.03 | 0.00 | 0.00 | 0.00 | 0.01 |  0.02 |  0.03 |
|   PilotCondition   |  0.02 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.01 |
|   RecordTracker    |  0.07 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
|    FileWatcher     |  0.61 | 0.01 | 0.02 | 0.01 | 0.04 |  0.08 |  0.27 |
|    FileWatcher     |  0.40 | 0.00 | 0.01 | 0.00 | 0.02 |  0.03 |  0.07 |
|   DelayedTrigger   |  0.03 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
| TriggeredCallback  |  0.02 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.01 |
| ImageAugmentation  |  4.28 | 0.40 | 0.84 | 0.52 | 2.28 |  2.83 |  3.70 |
|    KerasLinear     | 11.53 | 1.38 | 2.79 | 2.02 | 5.01 | 10.17 | 10.89 |
|     DriveMode      |  0.13 | 0.01 | 0.02 | 0.02 | 0.04 |  0.08 |  0.11 |
|     AiCatapult     |  0.11 | 0.00 | 0.01 | 0.00 | 0.01 |  0.02 |  0.04 |
|   AiRunCondition   |  0.04 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.02 |
+--------------------+-------+------+------+------+------+-------+-------+

INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.81 lap_time=28.81
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=54.76 lap_time=25.96
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=81.11 lap_time=26.34
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=4 total_time=107.24 lap_time=26.14
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=5 total_time=133.64 lap_time=26.40
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=6 total_time=160.11 lap_time=26.47
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=7 total_time=186.57 lap_time=26.46
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=8 total_time=212.66 lap_time=26.09
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=9 total_time=239.45 lap_time=26.79
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=10 total_time=265.76 lap_time=26.31
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=11 total_time=291.98 lap_time=26.22
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=12 total_time=318.06 lap_time=26.08
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=13 total_time=344.34 lap_time=26.29
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=14 total_time=370.50 lap_time=26.15
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=15 total_time=397.03 lap_time=26.54
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=16 total_time=423.45 lap_time=26.42
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=17 total_time=449.66 lap_time=26.21
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=18 total_time=476.47 lap_time=26.81
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=19 total_time=503.24 lap_time=26.77
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=20 total_time=529.68 lap_time=26.44
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=21 total_time=555.91 lap_time=26.22
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=22 total_time=581.88 lap_time=25.97
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=23 total_time=608.52 lap_time=26.64
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=24 total_time=634.80 lap_time=26.28
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=25 total_time=660.55 lap_time=25.76
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=26 total_time=686.65 lap_time=26.10
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=27 total_time=713.12 lap_time=26.46
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=28 total_time=739.54 lap_time=26.42
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=29 total_time=766.01 lap_time=26.47
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=30 total_time=792.11 lap_time=26.10
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=31 total_time=818.12 lap_time=26.01
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=32 total_time=844.69 lap_time=26.57
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=33 total_time=871.33 lap_time=26.64
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=34 total_time=897.92 lap_time=26.59
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=35 total_time=926.05 lap_time=28.14
CRASH
^CINFO:donkeycar.vehicle:Shutting down vehicle and its parts...
INFO:donkeycar.vehicle:Part Profile Summary: (times in ms)
INFO:donkeycar.vehicle:
+--------------------+-------+------+------+------+------+-------+-------+
|        part        |  max  | min  | avg  | 50%  | 90%  |  99%  | 99.9% |
+--------------------+-------+------+------+------+------+-------+-------+
|    DonkeyGymEnv    |  0.63 | 0.01 | 0.02 | 0.01 | 0.05 |  0.07 |  0.08 |
| LocalWebController |  0.13 | 0.00 | 0.01 | 0.01 | 0.03 |  0.04 |  0.05 |
|   ThrottleFilter   |  0.21 | 0.00 | 0.00 | 0.00 | 0.01 |  0.02 |  0.03 |
|   PilotCondition   |  0.05 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
|   RecordTracker    |  0.19 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
|    FileWatcher     |  1.05 | 0.01 | 0.02 | 0.01 | 0.04 |  0.08 |  0.13 |
|    FileWatcher     |  0.43 | 0.00 | 0.01 | 0.00 | 0.02 |  0.03 |  0.08 |
|   DelayedTrigger   |  0.05 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
| TriggeredCallback  |  0.04 | 0.00 | 0.00 | 0.00 | 0.00 |  0.01 |  0.01 |
| ImageAugmentation  |  5.18 | 0.39 | 0.87 | 0.54 | 2.29 |  3.05 |  3.81 |
|    KerasLinear     | 14.16 | 1.38 | 2.89 | 2.07 | 5.69 | 10.52 | 11.74 |
|     DriveMode      |  0.24 | 0.01 | 0.02 | 0.01 | 0.04 |  0.08 |  0.10 |
|     AiCatapult     |  0.05 | 0.00 | 0.01 | 0.00 | 0.01 |  0.02 |  0.03 |
|   AiRunCondition   |  0.05 | 0.00 | 0.00 | 0.00 | 0.01 |  0.01 |  0.02 |
+--------------------+-------+------+------+------+------+-------+-------+



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
lspci | grep VGA
ls -la /sys/bus/pci/devices/0000:01:00.0/numa_node
cat /sys/bus/pci/devices/0000:01:00.0/numa_node
echo 0 > /sys/bus/pci/devices/0000:01:00.0/numa_node
cat /sys/bus/pci/devices/0000:01:00.0/numa_node
---

python manage.py drive --model models/mypilot_circuit_launch_61.h5 --myconfig=myconfig-trnm-local.py --type=memory
>>> bad

# 5/.0005
python train.py --model models/mypilot_circuit_launch_62.h5 --tubs=data/tub_70_fast,data/tub_134_21-08-24_fast,data/tub_135_21-08-24_fast,data/tub_137_21-08-24_fast,data/tub_138_21-08-24_fast --type=memory

python manage.py drive --model models/mypilot_circuit_launch_62.h5 --myconfig=myconfig-trnm-local.py --type=memory
>>> bad



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



===============
27 Aug 2021
---------------

collect more data

python manage.py drive

    tub_147_21-08-27_centerline
    tub_146_21-08-27_leftlane
    tub_145_21-08-27_rightlane

# all best + left/right/center + 12/.0000001
python train.py\
 --model models/mypilot_circuit_launch_70.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_147_21-08-27_centerline,\
data/tub_146_21-08-27_leftlane,\
data/tub_145_21-08-27_rightlane\
 --type=linear

seq = iaa.Sequential([
    iaa.Crop(percent=(0, 0.1)), # random crops
        # Small gaussian blur with random sigma between 0 and 0.5.
        # But we only blur about 50% of all images.
    iaa.Sometimes(0.5, iaa.GaussianBlur(sigma=(0, 1.5))),
        # Strengthen or weaken the contrast in each image.
    iaa.LinearContrast((0.75, 1.5)),
        # Add gaussian noise.
        # For 50% of all images, we sample the noise once per pixel.
        # For the other 50% of all images, we sample the noise per pixel AND
        # channel. This can change the color (not only brightness) of the
        # pixels.
    iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
        # Make some images brighter and some darker.
        # In 20% of all cases, we sample the multiplier once per channel,
        # which can end up changing the color of the images.
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
        # Apply affine transformations to each image.
        # Scale/zoom them, translate/move them, rotate them and shear them.
    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
        rotate=(-10, 10),
        shear=(-8, 8)
    ),
    # -------------------------------------------------
    iaa.SomeOf(3, [
            # Add values to the pixels of images with possibly different values for neighbouring pixels.
        iaa.AddElementwise((-40, 40), per_channel=0.5),
            # aug = iaa.AdditiveGaussianNoise(scale=0.2*255, per_channel=True)
            # aug = iaa.MultiplyElementwise((0.5, 1.5), per_channel=0.5)
        iaa.Multiply((0.5, 1.5), per_channel=0.5),
            # aug = iaa.Cutout(nb_iterations=(1, 5), size=0.1, squared=False)
            # aug = iaa.CoarseDropout(0.02, size_percent=0.15, per_channel=0.5)
        iaa.CoarseDropout((0.0, 0.05), size_percent=(0.02, 0.25)),
        iaa.Invert(0.25, per_channel=0.5),
            # aug = iaa.JpegCompression(compression=(70, 99))
        iaa.AddToHueAndSaturation((-50, 50), per_channel=True),
        iaa.ChangeColorTemperature((1100, 10000)),
            # aug = iaa.GammaContrast((0.5, 2.0))
        iaa.GammaContrast((0.5, 2.0), per_channel=True),
        iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 2.0)),    
        iaa.imgcorruptlike.GaussianNoise(severity=2),
        iaa.imgcorruptlike.Fog(severity=1)
    ])    
], random_order=True) # apply augmenters in random order

python manage.py drive --model models/mypilot_circuit_launch_70.h5 --myconfig=myconfig-trnm-local.py --type=linear

>>> bad

# all best + 5/.0005 + AUG
python train.py\
 --model models/mypilot_circuit_launch_71.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast\
 --type=linear

python manage.py drive --model models/mypilot_circuit_launch_71.h5 --myconfig=myconfig-trnm-local.py --type=linear
>>> bad

-------------------------------------------------------------------------------------------------------

# one best + 5/.0005 + AUG
python train.py\
 --model models/mypilot_circuit_launch_72.h5\
 --tubs=\
data/tub_70_fast\
 --type=linear


for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_72.h5 --myconfig=myconfig-trnm-local.py --type=linear 2>&1 | grep -i 'lap_number\|Keras' ; done
>>> bad

-------------------------------------------------------------------------------------------------------

python train.py --model models/mypilot_circuit_launch_75.h5 --tubs=data/tub_70_fast --type=linear

python manage.py drive --model models/mypilot_circuit_launch_75.h5 --myconfig=myconfig-trnm-local.py --type=linear
>>> bad

for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_75.h5 --myconfig=myconfig-trnm-local.py --type=linear 2>&1 | grep -i 'lap_number\|Keras' ; done

>>> bad

--------------------------------------------------------------------------------------------

# one best + 5/.0005 + AUG
python train.py\
 --model models/mypilot_circuit_launch_73.h5\
 --tubs=\
data/tub_70_fast\
 --type=memory

python manage.py drive --model models/mypilot_circuit_launch_73.h5 --myconfig=myconfig-trnm-local.py --type=memory

>>> bad

for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_73.h5 --myconfig=myconfig-trnm-local.py --type=memory 2>&1 | grep -i 'lap_number\|Keras' ; done

>>> bad


# all best + 5/.0005 + BLUR
python train.py\
 --model models/mypilot_circuit_launch_76.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast\
 --type=linear

python manage.py drive --model models/mypilot_circuit_launch_76.h5 --myconfig=myconfig-trnm-local.py --type=linear
>>> bad???

===============
28 Aug 2021
---------------

# the model which knows the speed, 5/.0005

python train.py\
 --model models/mypilot_circuit_launch_77.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast\
 --type=imu

python manage.py drive --model models/mypilot_circuit_launch_77.h5 --myconfig=myconfig-trnm-local.py --type=imu
>>> goood, very stable, not fastest,

for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_77.h5 --myconfig=myconfig-trnm-local.py --type=imu 2>&1 | grep -i 'lap_number\|Keras' ; done
>>> good, very stable, not fastest, 0/10 bad, 0/10 crash

INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.32 lap_time=29.32
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.87 lap_time=27.55
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.87 lap_time=27.00
|      KerasIMU      | 8.09 | 5.09 | 5.82 | 5.71 | 6.35 | 7.30 |  7.99 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.29 lap_time=29.29
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.72 lap_time=27.43
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.03 lap_time=27.31
|      KerasIMU      | 8.40 | 5.07 | 5.86 | 5.75 | 6.44 | 7.42 |  8.10 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.29 lap_time=30.29
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=58.76 lap_time=28.47
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.98 lap_time=27.22
|      KerasIMU      | 8.24 | 5.07 | 5.83 | 5.72 | 6.44 | 7.39 |  8.08 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.47 lap_time=29.47
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.32 lap_time=26.85
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.44 lap_time=27.12
|      KerasIMU      | 8.85 | 5.10 | 5.89 | 5.78 | 6.53 | 7.45 |  8.25 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.75 lap_time=29.75
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.69 lap_time=27.94
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.70 lap_time=27.01
|      KerasIMU      | 10.68 | 5.06 | 5.87 | 5.76 | 6.47 | 7.48 |  8.43 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=30.09 lap_time=30.09
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=58.40 lap_time=28.31
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=85.34 lap_time=26.94
|      KerasIMU      | 16.08 | 5.12 | 5.95 | 5.82 | 6.61 | 7.60 |  8.34 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.95 lap_time=29.95
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.20 lap_time=27.25
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.74 lap_time=27.54
|      KerasIMU      | 8.11 | 5.17 | 5.93 | 5.82 | 6.56 | 7.47 |  8.08 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.66 lap_time=29.66
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.85 lap_time=27.18
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.28 lap_time=26.43
|      KerasIMU      | 8.56 | 5.10 | 5.86 | 5.76 | 6.43 | 7.42 |  8.13 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.88 lap_time=28.88
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.14 lap_time=27.26
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.62 lap_time=27.48
|      KerasIMU      | 8.29 | 5.07 | 5.86 | 5.75 | 6.43 | 7.40 |  8.01 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.40 lap_time=29.40
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.87 lap_time=27.47
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.14 lap_time=27.27
|      KerasIMU      | 7.82 | 4.81 | 5.49 | 5.41 | 5.91 | 6.80 |  7.50 |


for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_77.h5 --myconfig=myconfig-trnm-local.py --type=imu 2>&1 | grep -i 'lap_number\|Keras' ; done
>>> stable, not fastest, 0/10 bad, 0/10 crash

INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.19 lap_time=29.19
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.87 lap_time=26.68
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.64 lap_time=27.77
|      KerasIMU      | 31.65 | 5.01 | 7.00 | 5.93 | 9.57 | 22.61 | 30.53 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.11 lap_time=29.11
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.56 lap_time=27.45
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.83 lap_time=27.27
|      KerasIMU      | 32.00 | 4.93 | 7.16 | 6.02 | 9.61 | 26.65 | 31.13 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.89 lap_time=28.89
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.93 lap_time=27.04
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=82.83 lap_time=26.90
|      KerasIMU      | 34.51 | 4.91 | 7.17 | 5.91 | 9.49 | 27.62 | 32.03 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.19 lap_time=29.19
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.26 lap_time=27.07
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.75 lap_time=27.48
|      KerasIMU      | 33.60 | 4.92 | 7.02 | 5.93 | 9.08 | 28.52 | 32.56 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.64 lap_time=29.64
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.31 lap_time=27.67
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.51 lap_time=27.20
|      KerasIMU      | 32.23 | 4.89 | 7.01 | 6.04 | 9.19 | 20.48 | 31.55 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.88 lap_time=28.88
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=55.70 lap_time=26.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.19 lap_time=27.49
|      KerasIMU      | 35.51 | 4.91 | 7.16 | 6.05 | 9.56 | 28.59 | 32.88 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.18 lap_time=29.18
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.90 lap_time=27.72
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.85 lap_time=26.95
|      KerasIMU      | 33.40 | 4.91 | 7.01 | 5.87 | 9.48 | 28.64 | 31.21 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=28.92 lap_time=28.92
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.24 lap_time=27.32
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=83.71 lap_time=27.47
|      KerasIMU      | 32.59 | 5.00 | 7.22 | 6.00 | 9.68 | 25.22 | 30.95 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.89 lap_time=29.89
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=56.81 lap_time=26.92
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.59 lap_time=27.79
|      KerasIMU      | 32.31 | 5.00 | 7.22 | 6.10 | 9.78 | 26.90 | 31.25 |
INFO:donkeycar.parts.keras:Created KerasIMU with interpreter: KerasInterpreter
INFO:donkeycar.parts.keras:Loading model models/mypilot_circuit_launch_77.h5
INFO:donkeycar.vehicle:Adding part KerasIMU.
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=0 total_time=0.00 lap_time=0.00
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=1 total_time=29.58 lap_time=29.58
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=2 total_time=57.40 lap_time=27.82
INFO:gym_donkeycar.envs.donkey_sim:CollisionWithStartingLine: lap_number=3 total_time=84.99 lap_time=27.59
|      KerasIMU      | 32.83 | 4.90 | 7.02 | 5.96 | 9.51 | 24.83 | 31.72 |


DONKEYCAR_CFG_MAX_LOOPS=66000 python manage.py drive --model models/mypilot_circuit_launch_77.h5 --myconfig=myconfig-trnm-local.py --type=imu 2>&1 | grep -i 'lap_number\|Keras'

-----------------------------------------------------------------------------------

#train with soft recovery data

python train.py\
 --model models/mypilot_circuit_launch_78.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast,\
data/tub_139_21-08-24_soft_recovery,\
data/tub_140_21-08-24_soft_recovery\
 --type=imu

python manage.py drive --model models/mypilot_circuit_launch_78.h5 --myconfig=myconfig-trnm-local.py --type=imu

# train with a heavy AUG, best data only, speed aware imu, 5/.0005

python train.py\
 --model models/mypilot_circuit_launch_79.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast\
 --type=imu

python manage.py drive --model models/mypilot_circuit_launch_79.h5 --myconfig=myconfig-trnm-local.py --type=imu
>>> very bad

# train with a less heavy AUG, best data only, speed aware imu, 5/.0005

python train.py\
 --model models/mypilot_circuit_launch_80.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast\
 --type=imu

python manage.py drive --model models/mypilot_circuit_launch_80.h5 --myconfig=myconfig-trnm-local.py --type=imu
>>> very bad

# train with a less heavy AUG without heavy color changes, best data only, speed aware imu, 5/.0005

python train.py\
 --model models/mypilot_circuit_launch_81.h5\
 --tubs=\
data/tub_70_fast,\
data/tub_134_21-08-24_fast,\
data/tub_135_21-08-24_fast,\
data/tub_137_21-08-24_fast,\
data/tub_138_21-08-24_fast\
 --type=imu

### python manage.py drive --model models/mypilot_circuit_launch_81.h5 --myconfig=myconfig-trnm-local.py --type=imu
>>> bad

================================================================================================================
TODO
----------------------------------------------------------------------------------------------------------------

~~~~TODO~~~~
- best data - 5/.0005 linear
- best data - 5/.0005 linear, throttle 0.9
- best data - 12/.0000001 linear
- best data - 12/.0000001 linear, throttle 0.9
- best data - 5/.0005 memory
- drive 1 line + 2 line + mid line, then transfer model to race dataset

~~~~IDEAS~~~~
- try inference with GPU acceleration
- try rt model for inference
- drive backward from a cone helps for linear model only
- blur helps for linear but model performs slower, worth trying with throttle 1.1, worth trying with memory
- 12/.0000001 overfits memory model, 5/.0005 is better
- try different augmentations, not only blur/brightness
- to check that model is stable enough - bash script
   # for ((i=1;i<=10;i++)); do DONKEYCAR_CFG_MAX_LOOPS=2000 python manage.py drive --model models/mypilot_circuit_launch_77.h5 --myconfig=myconfig-trnm-local.py --type=imu 2>&1 | grep -i 'lap_number\|KerasIMU' ; done
- to check that model is stable enough - bash script
   # DONKEYCAR_CFG_MAX_LOOPS=66000 python manage.py drive | grep -i 'lap_number\|KerasIMU'

~~~~LEARNINGS~~~~
- tflite is faster for inference, not accurate (2x faster on AVG)
- memory model can handle first turn on lower speed
- aug slows down everything, but improve training loss function and validation loss funtion

~~~~BUGS~~~~
- video is not working with CROP
- inference is not using GPU
- simulation sometimes runs slow - slowing down PC, restart of simulation helps
