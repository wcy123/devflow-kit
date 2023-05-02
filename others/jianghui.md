
``` console
% rsync -avz --exclude build --exclude log --exclude install localhost:/group/xbjlab/users/jianghui/adehome/AutowareAuto ~/.local/jianghui/
% cd ~/.local/jianghui/AutowareAuto
% ls -la
% rm -fr {build,log,install}
% source /opt/ros/foxy/setup.bash
% cd src/drivers
% git clone https://github.com/ros-drivers/transport_drivers
% cd transport_drivers
% git checkout 0.0.6
% cd ~/.local/jianghui/AutowareAuto
% colcon build --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Debug
% PKG=off_map_obstacles_filter
% colcon build  --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Debug --packages-up-to=$PKG --allow-overriding $PKG

% # to suppress warning as error src/tools/autoware_auto_cmake/cmake/autoware_auto_cmake.cmake
% cp build/compile_commands.json .
% source install/setup.bash

% ros2 launch perception_map_provider perception_map_provider.launch.py
% ros2 launch dummy_perception dummy_perception.launch.py
% ros2 launch perception_map_provider perceptio_map_visualizer.launch.py
```


``` console
% tmux split-window
% cd ~/.local/jianghui/AutowareAuto
% source install/setup.bash
% ros2 run --prefix 'gdb --args' perception_map_provider perception_map_provider_node_exe --ros-args -r __ns:=/had_maps
% ros2 launch perception_map_provider perception_map_provider.launch.py
% ros2 launch dummy_perception dummy_perception.launch.py
% ros2 launch perception_map_provider perception_map_visualizer.launch.py
% ros2 launch autoware_auto_avp_demo ms3_sim.launch.py

```
