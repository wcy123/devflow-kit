# work log


<!-- ## build autoware.master -->

<!-- ``` console -->
<!-- % cd /home/chunywan/.local/ -->
<!-- % git clone https://gitlab.com/autowarefoundation/autoware.auto/AutowareAuto.git AutowareAuto.master -->
<!-- % cd /home/chunywan/.local/AutowareAuto.master -->
<!-- % git rev-parse HEAD -->
<!-- e3e26be1ab4b822996df60f261d031d7924f20ac -->
<!-- % # backup installed  file -->
<!-- % cp -av  /opt/AutowareAuto /opt/AutowareAuto ~/.local/AutowareAuto.install.master.bak -->
<!-- % ros2 launch lgsvl_simulation sim.launch.py simulation_params:=/home/local/test/Autoware.Auto/src/launch/autoware_demos/param/avp/lgsvl_simulation.param.yaml -->
<!-- % -->
<!-- ``` -->


<!-- ``` console -->
<!-- % find /home/chunywan/.local/AutowareAuto.master -type d -iname lgsvl_simulation -->
<!-- % find /home/chunywan/.local/AutowareAuto.master -type d -iname  autoware_testing -->
<!-- /home/chunywan/.local/AutowareAuto.master/src/drivers/lgsvl_simulation -->
<!-- ``` -->

<!-- ``` console -->
<!-- % find /home/local/test/Autoware.Auto -type d -iname lgsvl_simulation -->
<!-- ``` -->

<!-- ``` console -->
<!-- % cp -av /home/chunywan/.local/AutowareAuto.master/src/drivers/lgsvl_simulation /home/local/test/Autoware.Auto/src/drivers/ -->
<!-- % cp -av /home/chunywan/.local/AutowareAuto.master/src/tools/autoware_testing /home/local/test/Autoware.Auto/src/tools/ -->
<!-- ``` -->

<!-- 编译 autoware -->

<!-- ``` console -->
<!-- % cd /home/local/test/Autoware.Auto/ -->
<!-- % source /opt/ros/foxy/setup.bash -->
<!-- # 这里注意忽略一些模块 -->
<!-- % colcon build --symlink-install  --packages-skip xsens_nodes  ndt_mapping_nodes fpn point_cloud_mapping localization --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Debug -->
<!-- ``` -->

<!-- 简单的 `py_pub` 可以让车直线移动。 -->

<!-- 观察  `/vehicle/ackermann_vehicle_command` -->


<!-- 启动 lateral controller longitudinal controller and latlon muxer. -->

<!-- ``` console -->
<!-- % cd /home/chunywan/.local/AutowareAuto.master/src -->
<!-- % cp -av ./launch/autoware_demos/param/avp/lateral_controller.param.yaml ./launch/autoware_demos/param/avp/longitudinal_controller.param.yaml ./launch/autoware_demos/param/avp/latlon_muxer.param.yaml  /home/local/test/Autoware.Auto/src/launch/avp_demos/param/ -->
<!-- % ls -l /home/local/test/Autoware.Auto/src/launch/avp_demos/param/ -->
<!-- ``` -->


<!-- ``` console -->
<!-- % cp -av /home/chunywan/.local/AutowareAuto.master/src/drivers/lgsvl_simulation /home/local/test/Autoware.Auto/src/drivers -->
<!-- % cp -av /home/chunywan/.local/AutowareAuto.master/src/launch/autoware_demos/param/avp/lgsvl_simulation.param.yaml  /home/local/test/Autoware.Auto/src/launch/avp_demos/param/ -->
<!-- % cp -av /home/chunywan/.local/AutowareAuto.master/src/launch/autoware_demos/param/vehicle_characteristics.param.yaml /home/local/test/Autoware.Auto/src/launch/avp_demos/param/ -->
<!-- ``` -->


<!-- 运行 stage.2 -->

<!-- ``` console -->
<!-- % source /home/local/test/Autoware.Auto/install/setup.bash; ros2 launch avp_demos stage2.launch.py -->
<!-- ``` -->

<!-- 失败，这种方法似乎不行， master 分支和 1.1.0 分支变化太大。试图跑 ms3_sim.launch.py -->

``` console
% rm -fr ~/.ros/log; source /home/local/test/Autoware.Auto/install/setup.bash; ros2 launch autoware_auto_avp_demo ms3_sim.launch.py
```

找不到 LexusRX.obj

``` console
% cd /home/local/test/Autoware.Auto/
% find /home/local/test/Autoware.Auto/src/  -iname LexusRX.obj
% git remote add upstream https://gitlab.com/autowarefoundation/autoware.auto/AutowareAuto.git
% git lfs fetch upstream
```


```
[ndt_map_publisher_exe-3] terminate called after throwing an instance of 'std::runtime_error'
[ndt_map_publisher_exe-3]   what():  Yaml file not found
[ndt_map_publisher_exe-3]
[lanelet2_map_provider_exe-12] [INFO] [1652754267.145133203] [had_maps.lanelet2_map_provider_node]: Waiting for earth to map transform - please start ndt_map_publisher
1652754267.1766241 [ERROR] [ndt_map_publisher_exe-3]: process has died [pid 1189228, exit code -6, cmd '/home/local/test/Autoware.Auto/install/ndt_nodes/lib/ndt_nodes/ndt_map_publisher_exe --ros-args -r __ns:=/localization --params-file /home/local/test/Autoware.Auto/install/autoware_auto_avp_demo/share/autoware_auto_avp_demo/param/map_publisher.param.yaml'].
```



``` console
% cat /home/local/test/Autoware.Auto/src/tools/autoware_auto_avp_demo/param/map_publisher.param.yaml
% git lfs checkout autonomoustuff_parking_lot.pcd
% mkdir -p /opt/AutowareAuto/share/autoware_auto_avp_demo/data/
% ln -s /home/local/test/Autoware.Auto/src/tools/autoware_auto_avp_demo/data/autonomoustuff_parking_lot.pcd /opt/AutowareAuto/share/autoware_auto_avp_demo/data/
% ln -s /home/local/test/Autoware.Auto/src/tools/autoware_auto_avp_demo/data/autonomoustuff_parking_lot_lgsvl.pcd /opt/AutowareAuto/share/autoware_auto_avp_demo/data/autonomoustuff_parking_lot_lgsvl.pcd
% ln -s /home/local/test/Autoware.Auto/src/tools/autoware_auto_avp_demo/data/autonomoustuff_parking_lot_lgsvl.yaml /opt/AutowareAuto/share/autoware_auto_avp_demo/data/
% ls -l /opt/AutowareAuto/share/autoware_auto_avp_demo/data/
```


```
[robot_state_publisher-1] [WARN] [1652755029.780740329] [robot_state_publisher]: No robot_description parameter, but command-line argument available.  Assuming argument is name of URDF file.  This backwards compatibility fallback will be removed in the future.
```


``` console
% ros2 run ndt_nodes ndt_map_publisher_exe    --ros-args -r __ns:=/localization --params-file /home/local/test/Autoware.Auto/install/autoware_auto_avp_demo/share/autoware_auto_avp_demo/param/map_publisher.param.yaml
```



```
[lanelet2_map_provider_exe-12]   what():  Could not find lanelet map under /opt/AutowareAuto/share/autoware_auto_avp_demo/data/autonomoustuff_parking_lot.osm
[rviz2-20] Parsing robot urdf xml string.
[ERROR] [lanelet2_map_provider_exe-12]: process has died [pid 1191851, exit code -6, cmd '/home/local/test/Autoware.Auto/install/lanelet2_map_provider/lib/lanelet2_map_provider/lanelet2_map_provider_exe --ros-args -r __node:=lanelet2_map_provider_node -r __node:=lanelet2_map_provider_node -r __ns:=/had_maps --param
s-file /home/local/test/Autoware.Auto/install/autoware_auto_avp_demo/share/autoware_auto_avp_demo/param/lanelet2_map_provider.param.yaml'].
[lane_planner_node_exe-15] [INFO] [1652755773.114418472] [planning.lane_planner_node]: Waiting for map service...
[parking_planner_node_exe-16] [INFO] [1652755773.122560681] [planning.parking_planner_node]: Waiting for map service...
[lanelet2_map_visualizer_exe-13] [INFO] [1652755773.135246098] [had_maps.lanelet2_map_visualizer_node]: Service not available, waiting again...
```


``` console
% ln -s /home/local/test/Autoware.Auto/src/tools/autoware_auto_avp_demo/data/autonomoustuff_parking_lot.osm /opt/AutowareAuto/share/autoware_auto_avp_demo/data/autonomoustuff_parking_lot.osm
% xxd /opt/AutowareAuto/share/autoware_auto_avp_demo/data/autonomoustuff_parking_lot.osm | head
% ls -l /opt/AutowareAuto/share/autoware_auto_avp_demo/data/autonomoustuff_parking_lot.osm
% head /opt/AutowareAuto/share/autoware_auto_avp_demo/data/autonomoustuff_parking_lot.osm
```


研究一下模块结构


```
:~ chunywan % ros2 node list
/control/mpc_controller_node
/had_maps/lanelet2_map_provider_node
/had_maps/lanelet2_map_visualizer_node
/lidar_front/filter_transform_vlp16_front
/lidar_rear/filter_transform_vlp16_rear
/lidars/point_cloud_fusion_nodes
/lidars/voxel_grid_cloud_node
/localization/ndt_map_publisher_node
/localization/p2d_ndt_localizer_node
/perception/euclidean_cluster_cloud_node
/perception/off_map_obstacles_filter_node
/perception/ray_ground_classifier
/perception/transform_listener_impl_55c36064b790
/planning/behavior_planner_node
/planning/lane_planner_node
/planning/lanelet2_global_planner_node
/planning/object_collision_estimator_node
/planning/parking_planner_node
/robot_state_publisher
/rqt_gui_py_node_1193897
/rviz2
/transform_listener_impl_557f9bf563c0
/vehicle/lgsvl_interface_node
/vehicle/transform_listener_impl_55e55b19e580

:~ chunywan % ros2 node info /control/mpc_controller_node
/control/mpc_controller_node
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /planning/trajectory: autoware_auto_msgs/msg/Trajectory
    /tf: tf2_msgs/msg/TFMessage
    /tf_static: tf2_msgs/msg/TFMessage
    /vehicle/vehicle_kinematic_state: autoware_auto_msgs/msg/VehicleKinematicState
  Publishers:
    /control/control_diagnostic: autoware_auto_msgs/msg/ControlDiagnostic
    /control/mpc_debug_computed_trajectory: autoware_auto_msgs/msg/Trajectory
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /vehicle/vehicle_command: autoware_auto_msgs/msg/VehicleControlCommand
  Service Servers:
    /control/mpc_controller_node/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /control/mpc_controller_node/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /control/mpc_controller_node/get_parameters: rcl_interfaces/srv/GetParameters
    /control/mpc_controller_node/list_parameters: rcl_interfaces/srv/ListParameters
    /control/mpc_controller_node/set_parameters: rcl_interfaces/srv/SetParameters
    /control/mpc_controller_node/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:

  Action Clients:

:~ chunywan % ros2 node info /vehicle/lgsvl_interface_node
/vehicle/lgsvl_interface_node
  Subscribers:
    /lgsvl/gnss_odom: nav_msgs/msg/Odometry
    /lgsvl/state_report: lgsvl_msgs/msg/CanBusData
    /lgsvl/vehicle_odom: lgsvl_msgs/msg/VehicleOdometry
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /vehicle/state_command: autoware_auto_msgs/msg/VehicleStateCommand
    /vehicle/vehicle_command: autoware_auto_msgs/msg/VehicleControlCommand
  Publishers:
    /gnss/pose: geometry_msgs/msg/PoseWithCovarianceStamped
    /lgsvl/vehicle_control_cmd: lgsvl_msgs/msg/VehicleControlData
    /lgsvl/vehicle_state_cmd: lgsvl_msgs/msg/VehicleStateData
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /tf: tf2_msgs/msg/TFMessage
    /vehicle/odometry: autoware_auto_msgs/msg/VehicleOdometry
    /vehicle/state_report: autoware_auto_msgs/msg/VehicleStateReport
    /vehicle/vehicle_kinematic_state: autoware_auto_msgs/msg/VehicleKinematicState
  Service Servers:
    /vehicle/autonomy_mode: autoware_auto_msgs/srv/AutonomyModeChange
    /vehicle/lgsvl_interface_node/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /vehicle/lgsvl_interface_node/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /vehicle/lgsvl_interface_node/get_parameters: rcl_interfaces/srv/GetParameters
    /vehicle/lgsvl_interface_node/list_parameters: rcl_interfaces/srv/ListParameters
    /vehicle/lgsvl_interface_node/set_parameters: rcl_interfaces/srv/SetParameters
    /vehicle/lgsvl_interface_node/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:

  Action Clients:

```

1.1.0 里面采用的是 vehicle_command 格式。

start the simulation.


``` console
% echo $ROS_DOMAIN_ID
xbjlabdpwstn05% ssh localhost
xbjlabdpwstn05% source /opt/ros/foxy/setup.bash
xbjlabdpwstn05% export ROS_DOMAIN_ID=1
xbjlabdpwstn05% ros2 topic list # parameter_events and rosout are built-in topic
% SIMULATOR_ROOT=/scratch/$USER/Downloads/svlsimulator-linux64-2021.3
% env LD_LIBRARY_PATH=$SIMULATOR_ROOT/simulator_Data/Plugins:/opt/ros/foxy/lib ROS_DOMAIN_ID=1 HOME=/scratch/$USER/  DISPLAY=127.0.0.1:17941   http_proxy=http://localhost:9181   $SIMULATOR_ROOT/simulator
```



``` console
% find /home/local/test/Autoware.Auto/src/ -iname lgsvl_simulation.param.yaml
% source /home/local/test/Autoware.Auto/install/setup.bash
% ros2 launch lgsvl_simulation sim.launch.py simulation_params:=/home/local/test/Autoware.Auto/src/launch/avp_demos/param/lgsvl_simulation.param.yaml
% # no module lgsvl
% find /home/local/AutowareAuto.master/src -type d -iname lgsvl
% cd /home/local
% git clone https://github.com/lgsvl/PythonAPI.git
% cd PythonAPI
% python3 -m pip install -r requirements.txt --user .
```

``` console
% ros2 run tf2_tools view_frames.py
```

``` console
% ros2 topic pub -r 1 -t 1 /localization/initialpose \
geometry_msgs/msg/PoseWithCovarianceStamped  \
'{header: {stamp: {sec: 1652771953, nanosec: 274787965}, frame_id: map}, pose: {pose: {position: {x: -108.094, 'y': -2.0545, z: -28.905}, orientation: {x: 0, 'y': 0, z: 0.0, w: 1.0}}}}'
```
