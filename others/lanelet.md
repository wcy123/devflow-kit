``` console
% cd ~/.local/
% export https_proxy=http://localhost:9181
% git clone https://github.com/fzi-forschungszentrum-informatik/Lanelet2.git
% cd ~/.local/Lanelet2/lanelet2_examples
% ls -l
% bat CMakeLists.txt
% source /opt/ros/foxy/setup.bash
% rosdep install -y -i --from-paths src
% colcon build --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_PREFIX_PATH=$HOME/.local/Ubuntu.20.04.x86_64.Debug -DCMAKE_BUILD_TYPE=Debug
% source install/setup.bash
% cp build/compile_commands.json .
% gdb build/lanelet2_examples/01_dealing_with_lanelet_primitives
```
