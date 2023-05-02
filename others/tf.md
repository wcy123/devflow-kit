
``` console
%
```


``` console
% sudo apt-get install ros-foxy-turtle-tf2-py ros-foxy-tf2-tools ros-foxy-tf-transformations
% source /opt/ros/foxy/setup.bash
% sudo env all_proxy=http://localhost:9181 pip install transforms3d
% ros2 launch turtle_tf2_py turtle_tf2_demo.launch.py &
% ros2 run tf2_tools view_frames.py
% ros2 run tf2_ros tf2_echo turtle2 turtle1
% ros2 run rviz2 rviz2 -d $(ros2 pkg prefix --share turtle_tf2_py)/rviz/turtle_rviz.rviz &

```


``` console

% cd ~/.local/dev_ws/src
% export https_proxy=http://localhost:9181
% git clone https://github.com/ros/ros_tutorials.git
% cd ~/.local/dev_ws/src/ros_tutorials
% ls -la
% git branch -a
% git checkout foxy-devel
% git clone https://github.com/ros/geometry_tutorials
% cd ~/.local/dev_ws/
% ls -la
% source /opt/ros/foxy/setup.bash
% cd ~/.local/dev_ws/src/geometry_tutorials
% git checkout ros2
% cd ~/.local/dev_ws/
% rm -fr log build install
% tree -df src/geometry_tutorials/
% colcon build --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Debug
% cp -av build/compile_commands.json .
```

``` console
% ros2 run tf2_ros static_transform_publisher 2 0 0 0 0 1 0 "world" "turtle"
% ros2 topic echo --qos-reliability reliable --qos-durability transient_local /tf_static
```


``` console
% cd ~/.local/dev_ws/; source install/setup.bash
% ros2 run turtlesim turtlesim_node
```

``` console
% cd ~/.local/dev_ws/; source install/setup.bash
% ros2 run turtle_tf2_cpp turtle_tf2_broadcaster --ros-args -r __node:=broadcaster1 -p tutlename:=tutle1
```

``` console
% cd ~/.local/dev_ws/; source install/setup.bash
% ros2 run turtlesim turtle_teleop_key
```


``` console
% cd ~/.local/dev_ws/; source install/setup.bash
% ros2 run turtle_tf2_cpp  turtle_tf2_listener --ros-args -p target_frame:=world
```
