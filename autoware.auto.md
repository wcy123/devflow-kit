

```
% git clone https://gitlab.com/ApexAI/autowareclass2020.git /workspace/aisw/autowareclass2020
```


```
ade$ ls /home/build/data/route_small_loop_rw-127.0.0.1.pcap
ade$ udpreplay -r -1 /home/build/data/route_small_loop_rw-127.0.0.1.pcap
ade$ source /workspace/aisw/AutowareAuto/install/setup.bash
ade$ rviz2 -d /workspace/aisw/autowareclass2020/autowareclass2020/code/src/01_DevelopmentEnvironment/aw_class2020.rviz
ade$ cd /workspace/aisw/AutowareAuto;
ade$ source /workspace/aisw/AutowareAuto/install/setup.bash
ade$ ros2 run velodyne_nodes velodyne_cloud_node_exe --ros-args -r __ns:=/lidar_front --params-file /workspace/aisw/autowareclass2020/code/src/01_DevelopmentEnvironment/velodyne_node.param.yaml
ade$ ros2 run robot_state_publisher robot_state_publisher ./src/urdf/lexus_rx_450h_description/urdf/lexus_rx_450h.urdf

ade$ source /workspace/aisw/AutowareAuto/install/setup.bash
ade$ cd /workspace/aisw/AutowareAuto;
ade$ ros2 run point_cloud_filter_transform_nodes  point_cloud_filter_transform_node_exe --ros-args --remap __ns:=/lidar_front --params-file ./src/perception/filters/point_cloud_filter_transform_nodes/param/vlp16_sim_lexus_filter_transform.param.yaml --remap  __node:=filter_transform_vlp16_front --remap points_filtered:=/perception/points_in

ade$ source /workspace/aisw/AutowareAuto/install/setup.bash
ade$ cd /workspace/aisw/AutowareAuto;
ade$ ros2 run ray_ground_classifier_nodes ray_ground_classifier_cloud_node_exe --ros-args -r __ns:=/perception --params-file ./src/launch/autoware_auto_launch/param/ray_ground_classifier.param.yaml


ade$ source /workspace/aisw/AutowareAuto/install/setup.bash
ade$ cd /workspace/aisw/AutowareAuto;
ade$ ros2 run  euclidean_cluster_nodes euclidean_cluster_node_exe --ros-args -r __ns:=/perception --params-file ./src/launch/autoware_auto_launch/param/euclidean_cluster.param.yaml
```



# in docker environment

```
% sudo pip install --proxy=http://localhost:9181  -U colcon-common-extensions vcstool
% source /opt/ros/foxy/setup.bash
% cd /workspace/aisw/
% export http_proxy=http://localhost:9181
% export https_proxy=http://localhost:9181
% git clone https://gitlab.com/autowarefoundation/autoware.auto/AutowareAuto.git
```

## prerequisites

``` console
% cd /workspace/aisw/AutowareAuto
% source /opt/ros/foxy/setup.bash
% vcs import < autoware.auto.$ROS_DISTRO.repos
$ echo $ROS_VERSION
% sudo -E rosdep init
% rosdep update
% rm install build 2>/dev/null
% for i in build install ; do   mkdir -p /home/build/autoware.$i; ln -sf /home/build/autoware.$i $i; done
% ls -l
% # sudo -E apt-get install -y liblbfgsb0 python3-decorator ros-foxy-osrf-testing-tools-cpp ros-foxy-nav2-costmap-2d ros-foxy-ros-testing ros-foxy-octomap
% sudo vim # update rosdep to use proxy sudo -H -E
% rosdep install -y -i --from-paths src
```


## build

``` console
% source /opt/ros/foxy/setup.bash
% cd /workspace/aisw/AutowareAuto
% export http_proxy=http://localhost:9181; export https_proxy=http://localhost:9181 # fix benchmark_tools problem
% curl -v http://www.google.com
% sudo chmod 777 /opt
% rm -fr /opt/AutowareAuto
% colcon build --build-base /home/build/autoware.build2 --install-base /opt/AutowareAuto --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
% colcon build --build-base /home/build/autoware.build2 --install-base /opt/AutowareAuto  --packages-select image_visualizer --allow-overriding image_visualizer  --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
% find /home/build/autoware.build2  -iname compile_commands.json | grep imag
% cp -av /home/build/autoware.build2/image_visualizer/compile_commands.json /workspace/aisw/AutowareAuto/src/tools/image_visualizer/
% colcon build --build-base /home/build/autoware.build2 --install-base /opt/AutowareAuto
% colcon build --build-base /home/build/autoware.build2 --install-base /opt/AutowareAuto  --packages-select ndt_mapping_nodes  --allow-overriding ndt_mapping_nodes
% colcon build --build-base /home/build/autoware.build2 --install-base /opt/AutowareAuto  --packages-select ndt --allow-overriding ndt
% colcon build --build-base /home/build/autoware.build2 --install-base /opt/AutowareAuto  --packages-select ndt_nodes --allow-overriding ndt_nodes
% colcon build --build-base /home/build/autoware.build2 --install-base /opt/AutowareAuto  --packages-select autoware_demos --allow-overriding autoware_demos
% ls -l /opt/AutowareAuto/autoware_demos/share/autoware_demos/data/autonomoustuff_parking_lot_lgsvl.pcd
% ros2 run costmap_generator_nodes costmap_generator_node_exe -ros-args -r __node:=costmap_generator_node -r __ns:=/planning --params-file /opt/AutowareAuto/autoware_auto_launch/share/autoware_auto_launch/param/costmap_generator.param.yaml -r ~/client/HAD_Map_Service:=/had_maps/HAD_Map_Service


% colcon build --build-base /home/build/autoware.build2 --install-base /opt/AutowareAuto  --packages-up-to autoware_demos --allow-overriding autoware_demos

```

``` console
xbjlabdpwstn05% ssh localhost
xbjlabdpwstn05% source /opt/ros/foxy/setup.bash
xbjlabdpwstn05% export ROS_DOMAIN_ID=1
xbjlabdpwstn05% ros2 topic list # parameter_events and rosout are built-in topic
% SIMULATOR_ROOT=/scratch/$USER/Downloads/svlsimulator-linux64-2021.3
% env LD_LIBRARY_PATH=$SIMULATOR_ROOT/simulator_Data/Plugins:/opt/ros/foxy/lib ROS_DOMAIN_ID=1 HOME=/scratch/$USER/  DISPLAY=127.0.0.1:17941   http_proxy=http://localhost:9181   $SIMULATOR_ROOT/simulator
```
