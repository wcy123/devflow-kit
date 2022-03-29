##

# install ros

```
% lsl
% sudo apt update && sudo apt install curl gnupg2 lsb-release
% sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
% echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

## install from deb pacakges.


```
% sudo apt update
% sudo apt install -y ros-foxy-desktop
```

## verify installation

```
% source /opt/ros/foxy/setup.bash
% ros2 run demo_nodes_cpp talker
```

start another terminal

```
% source /opt/ros/foxy/setup.bash
% ros2 run demo_nodes_py listener
```

## verify rviz

```
% source /opt/ros/foxy/setup.bash
% rviz2
```

# cannot open `libQt5Core.so.5`

https://stackoverflow.com/questions/70815369/ros-problem-libqt5core-so-5-cannot-open-shared-object-file-no-such-file-or-di


```
% sudo apt-get install libqt5gui5
% whereis libQt5Core.so.5
% sudo strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
```

#

```
% source /opt/ros/foxy/setup.bash
% ros2 run turtlesim turtlesim_node
```

start another


```
% source /opt/ros/foxy/setup.bash
% ros2 run turtlesim turtle_teleop_key
```


```
% ros2 node list
% ros2 topic list
% ros2 service list
% ros2 action list
``

```
% sudo apt install ~nros-foxy-rqt*
```

# remap

```
% ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
```

```
% ros2 node -h
% ros2 node list
% ros2 node list -a
% ros2 node info /my_turtle
% ros2 node info /teleop_turtle
```


```
% ros2 topic list
% ros2 topic list -t
% ros2 topic echo /turtle1/cmd_vel
% ros2 topic info /turtle1/cmd_vel
```


```
% ros2 interface show geometry_msgs/msg/Twist
```


```
% ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
% ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
% ros2 topic hz /turtle1/pose
% ros2 topic hz /turtle1/cmd_vel
```


```
% ros2 service list -t
% ros2 service type /kill
% ros2 service type /clear
% ros2 service find std_srvs/srv/Empty
% ros2 interface show turtlesim/srv/Kill
% ros2 interface show turtlesim/srv/Spawn
% ros2 service call /clear std_srvs/srv/Empty

% ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: 'tom'}"


```



```
% ros2 param list
% ros2 param get /turtlesim background_b
% ros2 param get /turtlesim background_r
% ros2 param get /turtlesim background_g
% ros2 param set /turtlesim background_b 130
% ros2 param set /turtlesim background_r 120
% ros2 param set /turtlesim background_g 110
% ros2 param dump  /turtlesim
% cat ./turtlesim.yaml
% ros2 param load  /turtlesim ./turtlesim.yaml
```


```
% ros2 action list -t
% ros2 action info /turtle1/rotate_absolute
% ros2 action info /tom/rotate_absolute
% ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: -1.57}"
% ros2 action send_goal /tom/rotate_absolute turtlesim/action/RotateAbsolute "{theta: -1.57}"
% ros2 action send_goal /tom/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}" --feedback
% ros2 interface show turtlesim/action/RotateAbsolute
```


```
% ros2 run turtlesim turtlesim_node
```

```
% ros2 run turtlesim turtle_teleop_key
```

```
% cd ~/build
% mkdir bag_files
% cd bag_files
% ros2 topic list
% ros2 topic echo /turtle1/cmd_vel
```


```
% ros2 bag record /turtle1/cmd_vel
% ros2 bag info rosbag2_2022_03_20-23_52_25
% ros2 bag play rosbag2_2022_03_20-23_52_25
```




```
% mkdir -p /workspace/dev_ws/src
% cd /workspace/dev_ws/src
% git clone https://github.com/ros/ros_tutorials.git -b foxy-devel
% ls -l
% tree
% cd /workspace/dev_ws/; rosdep install -i --from-path src --rosdistro foxy -y
% cat src/package.xml
% find . -iname package.xml
% cat ./src/ros_tutorials/turtlesim/package.xml
% cd /workspace/dev_ws/; colcon build
% ls -la /workspace/dev_ws/;
% ls -la /workspace/dev_ws/install
% cat /workspace/dev_ws/install/.colcon_install_layout
% cat /workspace/dev_ws/install/setup.bash

% ls -la /workspace/dev_ws/build/
% ls -la /workspace/dev_ws/build/turtlesim
```


```
% source /workspace/dev_ws/install/setup.bash
% ros2 pkg executables turtlesim --full-path
% ros2 run turtlesim turtlesim_node
```


```
% cd /workspace/dev_ws/
% ros2 pkg create --build-type ament_cmake --node-name my_node my_package
% tree my_package -f
% ls my_package/include/my_package
% cat my_package/package.xml
% bat my_package/CMakeLists.txt
% colcon build
% ros2 pkg executables my_package --full-path
% ros2 run my_package my_node
```


```
% ros2 pkg create --build-type ament_cmake cpp_pubsub
```


```
% rosdep install -i --from-path src --rosdistro foxy -y
% cd /workspace/dev_ws/src/
% ros2 pkg create --build-type ament_cmake cpp_srvcli
% emacs -nw cpp_srvcli/src/add_two_ints_server.cpp
```


```
% cd /workspace/dev_ws/src/
% ros2 pkg create --build-type ament_python py_srvcli --dependencies rclpy example_interfaces
```


```
% cd /workspace/dev_ws/src/
% ros2 pkg create --build-type ament_cmake tutorial_interfaces

% cd /workspace/dev_ws/src/tutorial_interfaces; mkdir {msg,srv}
%
```



```
% cd /workspace/dev_ws/src/
% ros2 pkg create --build-type ament_cmake more_interfaces
% mkdir -p more_interfaces/msg//
% emacs -nw more_interfaces/msg/AddressBook.msg
% emacs -nw more_interfaces/package.xml
% emacs -nw more_interfaces/CMakeLists.txt
% emacs -nw more_interfaces/src/publish_address_book.cpp
% bat more_interfaces/src/publish_address_book.cpp
% emacs -nw more_interfaces/CMakeLists.txt
% cd /workspace/dev_ws/;colcon build --packages-up-to more_interfaces
% . install/local_setup.bash;
% ros2 run more_interfaces publish_address_book
```


```
% . install/setup.bash
% ros2 topic echo /address_book
```


```
% ros2 component types
% ros2 run rclcpp_components component_container
```

```
%  ros2 component list
%  ros2 component load /ComponentManager composition composition::Talker
%  ros2 component load /ComponentManager composition composition::Listener
%  ros2 component list
```

```
% ros2 component load /ComponentManager composition composition::Server
% ros2 component load /ComponentManager composition composition::Client
% ros2 component list
```


```
% ros2 run composition manual_composition
% ros2 component list
```

```
% echo ros2 run composition dlopen_composition `ros2 pkg prefix composition`/lib/libtalker_component.so `ros2 pkg prefix composition`/lib/liblistener_component.so
% ros2 run composition dlopen_composition `ros2 pkg prefix composition`/lib/libtalker_component.so `ros2 pkg prefix composition`/lib/liblistener_component.so
```



```
% ros2 launch composition composition_demo.launch.py
```

```
% ros2 run rclcpp_components component_container
```


```
% ros2 component list
% ros2 component unload /ComponentManager 2
% ros2 component unload /ComponentManager 3
```

```
% ros2 run rclcpp_components component_container --ros-args -r __node:=MyContainer -r __ns:=/ns
```
