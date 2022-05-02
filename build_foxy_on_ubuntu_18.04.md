# why

lg svl simulator  needs foxy.

# doc

https://docs.ros.org/en/foxy/Installation/Ubuntu-Development-Setup.html



``` console
% mkdir -p /scratch/$USER/foxy/src
% cd /scratch/$USER/foxy/
% ls -l
% export http_proxy=http://localhost:9181; export https_proxy=http://localhost:9181
% wget https://raw.githubusercontent.com/ros2/ros2/foxy/ros2.repos
% sudo -E env HOME=/home/root apt install -y python3-vcstool python3-rosdep
% vcs import src < ros2.repos
% cat ros2.repos
% ls -la
% sudo rosdep init
% rosdep update
% rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-5.3.1 urdfdom_headers"

```
