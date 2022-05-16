# work log


``` console
% source /home/local/test/Autoware.Auto/install/setup.bash
% /home/local/test/Autoware.Auto/install/setup.bash
% ros2 launch lgsvl_simulation sim.launch.py simulation_params:=/home/local/test/Autoware.Auto/src/launch/autoware_demos/param/avp/lgsvl_simulation.param.yaml
```


## build autoware.master

``` console
% cd /home/chunywan/.local/
% git clone https://gitlab.com/autowarefoundation/autoware.auto/AutowareAuto.git AutowareAuto.master
% cd /home/chunywan/.local/AutowareAuto.master
% git rev-parse HEAD
e3e26be1ab4b822996df60f261d031d7924f20ac
% # backup installed  file
% cp -av  /opt/AutowareAuto /opt/AutowareAuto ~/.local/AutowareAuto.install.master.bak
% ros2 launch lgsvl_simulation sim.launch.py simulation_params:=/home/local/test/Autoware.Auto/src/launch/autoware_demos/param/avp/lgsvl_simulation.param.yaml
%
```


``` console
% find /home/chunywan/.local/AutowareAuto.master -type d -iname lgsvl_simulation
/home/chunywan/.local/AutowareAuto.master/src/drivers/lgsvl_simulation
```

``` console
% find /home/local/test/Autoware.Auto -type d -iname lgsvl_simulation
```

``` console
% cp -av /home/chunywan/.local/AutowareAuto.master/src/drivers/lgsvl_simulation /home/local/test/Autoware.Auto/src/drivers/
```

``` console
% cd /home/local/test/Autoware.Auto/
% source /opt/ros/foxy/setup.bash
%
```
