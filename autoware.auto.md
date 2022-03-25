

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
