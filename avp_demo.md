
``` console
% cd -P /scratch/$USER/Downloads
% env ROS_DOMAIN_ID=1 DISPLAY=127.0.0.1:17941 ./simulator
```


``` console
% export AUTOWARE_ROOT=/opt/AutowareAuto;export ROS_DOMAIN_ID=1;source $AUTOWARE_ROOT/setup.bash% cd $AUTOWARE_ROOT/
% colcon build --packages-select lgsvl_interface
% ros2 run lgsvl_interface lgsvl_interface_exe --ros-args --params-file $AUTOWARE_ROOT/lgsvl_interface/share/lgsvl_interface/param/lgsvl.param.yaml
```


``` console
% export AUTOWARE_ROOT=/opt/AutowareAuto;export ROS_DOMAIN_ID=1;source $AUTOWARE_ROOT/setup.bash
% rviz2
```

``` console
% export AUTOWARE_ROOT=/opt/AutowareAuto;export ROS_DOMAIN_ID=1;source $AUTOWARE_ROOT/setup.bash
% ros2 topic list
% ros2 launch autoware_auto_launch autoware_auto_visualization.launch.py
```

``` console
% export AUTOWARE_ROOT=/opt/AutowareAuto;export ROS_DOMAIN_ID=1;source $AUTOWARE_ROOT/setup.bash
% bat $AUTOWARE_ROOT/autoware_demos/share/autoware_demos/launch/avp_sim.launch.py
% lgsvl_bridge --port 9090 &
% ros2 launch autoware_demos avp_sim.launch.py
```


<!-- ## this does not work -->
<!-- ``` console -->
<!-- % export AUTOWARE_ROOT=/opt/AutowareAuto -->
<!-- % export ROS_DOMAIN_ID=1 -->
<!-- % source $AUTOWARE_ROOT/setup.bash -->
<!-- % ros2 launch rosbridge_server rosbridge_websocket_launch.xml -->
<!-- % netstat -tnap | grep 9090 -->
<!-- ``` -->


## demo 2

``` console
ade$ source /opt/AutowareAuto/setup.bash
ade$ ros2 launch autoware_demos avp_sim.launch.py
```

``` console
ade$ source /opt/AutowareAuto/setup.bash
ade$ lgsvl_bridge
```

``` console
% source /opt/AutowareAuto/setup.bash
% rviz2 -d /opt/AutowareAuto/share/autoware_auto_launch/config/avp.rviz

```


``` console
% mkdir -p  /scratch/$USER/Downloads/ros2_for_unity_svl_bridge
% cd  /scratch/$USER/Downloads/ros2_for_unity_svl_bridge
% curl --proxy http://localhost:9181 -Lo ubuntu_foxy_libs.zip https://github.com/RobotecAI/ROS2ForUnitySVLBridge/releases/download/svl-2021.3/ubuntu_foxy_libs.zip
% file ubuntu_foxy_libs.zip
% unzip ubuntu_foxy_libs.zip
% ls -l Plugins/Linux/x86_64/*
% SIMULATOR_ROOT=/scratch/$USER/Downloads/bbb/simulatorl
% SIMULATOR_ROOT=/scratch/$USER/Downloads/svlsimulator-linux64-2021.3
% ls -l $SIMULATOR_ROOT/simulator_Data/Plugins
% ls -l /scratch/$USER/Downloads/ros2_for_unity_svl_bridge/Plugins/Linux/x86_64
# libraries from Plugins/<OS_NAME>/x86_64/* put into simulator_Data/Plugins of svl simulator directory,
% cp -av  /scratch/$USER/Downloads/ros2_for_unity_svl_bridge/Plugins/Linux/x86_64/* $SIMULATOR_ROOT/simulator_Data/Plugins/
# libraries from Plugins/*.dll put into simulator_Data/Managed of svl simulator directory.
% ls -l /scratch/$USER/Downloads/ros2_for_unity_svl_bridge/Plugins/*.dll | wc
% ls -l $SIMULATOR_ROOT/simulator_Data/Managed | wc
% cp -av /scratch/$USER/Downloads/ros2_for_unity_svl_bridge/Plugins/*.dll $SIMULATOR_ROOT/simulator_Data/Managed/
% export LD_LIBRARY_PATH=$SIMULATOR_ROOT/simulator_Data/Plugins
```


``` console
% export LD_LIBRARY_PATH=$SIMULATOR_ROOT/simulator_Data/Plugins
% cd /scratch/$USER/Downloads/
% env LD_LIBRARY_PATH=$SIMULATOR_ROOT/simulator_Data/Plugins:/opt/ros/foxy/lib ROS_DOMAIN_ID=1 HOME=/scratch/$USER/  DISPLAY=127.0.0.1:17941   http_proxy=http://localhost:9181   $SIMULATOR_ROOT/simulator
```
