## build adas.avp

``` console
% cd /workspace/aisw/ADAS.AVP
% source ~/.local/jianghui/AutowareAuto/install/setup.bash
% rm -fr {build,log,install}
% for i in build log install; do mkdir -p $HOME/build/adas_avp/$i; done
% for i in build log install; do ln -s $HOME/build/adas_avp/$i .; done
% ls -la
% colcon build --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON  -DCMAKE_PREFIX_PATH=$HOME/.local/Ubuntu.20.04.x86_64.Debug -DCMAKE_BUILD_TYPE=Debug
% PKG=off_map_obstacles_filter
% colcon build  --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Debug --packages-up-to=$PKG --allow-overriding $PKG
% colcon build --build-base /home/build/adas.avp/build --install-base /home/build/adas.avp/install --packages-up-to=$PKG --allow-overriding $PKG --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_PREFIX_PATH=$HOME/.local/Ubuntu.20.04.x86_64.Debug -DCMAKE_BUILD_TYPE=Debug
% ls -l /home/build/adas.avp/build
% cat /home/build/adas.avp/build/compile_commands.json | grep pybind
% cp /home/build/adas.avp/build/compile_commands.json /workspace/aisw/ADAS.AVP
```

## run adas.avp

``` console
% cd /workspace/aisw/ADAS.AVP
% source install/setup.bash
% ros2 run psdet psdet_exe --ros-args -r output/psdet:=/had_maps/free_space
```

send a image

``` console
% cd /workspace/aisw/ADAS.AVP
% source install/setup.bash
% ros2 launch avp_demos state1
% ros2  run send_img send_img_node_exe --ros-args -p filename:="/workspace/aisw/psdet/testdata/images/0003.jpg" -r sample_image:=/input
```





``` console
% ls -l /home/build/adas.avp/install/setup.bash
% ls -l /home/build/adas.avp/install/fpn/share/fpn
% source /home/build/adas.avp/install/setup.bash
% export ROS_DOMAIN_ID=1
% ros2 run rclcpp_components component_container &
%  ros2 component types
%  ros2 component list
%  ros2 component load /ComponentManager fpn autoware::perception::FpnNode
%  ros2 component unload /ComponentManager 1
%  ros2 component unload /ComponentManager 3
% ros2 topic list
% ros2 component standalone fpn autoware::perception::FpnNode
% ros2 topic list
% ros2 topic info -v /front_camera/image
```


``` console
% cd /workspace/aisw/AutowareAuto/
% source /opt/ros/foxy/setup.bash
% git checkout tags/1.0.0 -b release-1.0.0
:AutowareAuto chunywan % export https_proxy=http://localhost:9181
:AutowareAuto chunywan % export http_proxy=http://localhost:9181
% git clean -f -xfd
% git lfs --include='*' --exclude='' pull
% vcs import < autoware.auto.$ROS_DISTRO.repos
% rm -fr /opt/AutowareAuto
% mkdir -p /opt/AutowareAuto
% rm -fr /home/build/autoware.auto/build
% colcon build --allow-overriding rosapi rosbridge_library rosbridge_msgs rosbridge_server rosbridge_suite udp_driver \
               --packages-up-to autoware_demos \
               --build-base /home/build/autoware.auto/build \
               --install-base /opt/AutowareAuto \
               --symlink-install \
               --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Debug;


```


# problem udp_driver_node.hpp not found

https://answers.ros.org/question/389543/autowareauto-100-build-failed-with-xsens_nodes-and-euclidean_cluster/?answer=389825

``` console
% cd /workspace/aisw/AutowareAuto/src/drivers
% git clone https://github.com/ros-drivers/transport_drivers
% cd transport_drivers
% git checkout 0.0.6
```
