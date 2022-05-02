# svglsimulator

https://www.svlsimulator.com/docs/installation-guide/build-instructions/

## prerequisite

``` console
% ssh xbjlabdpwstn05
% sudo apt install libvulkan1
```

## create tunel

``` console
% ssh xcoengvm229033
% tmux attach
% vi ~/.ssh/config # xbjjmphost01
chunywan@xcoengvm229033:xdock-vitis-ai-sw% ssh -R10022:localhost:22  xbjlabdpwstn05
xbjlabdpwstn05% while sleep 1; do echo 'dont close this windows'; date; done;
```

``` console
% ssh xbjlabdpwstn05
% ssh-keygen -f "/home/chunywan/.ssh/known_hosts" -R "[localhost]:10022"
xbjlabdpwstn05% ssh -L9181:localhost:3128 -p 10022 localhost
xbjlabdpwstn05% while sleep 1; do echo '9181->3128 dont close this windows'; date; done;
```

```console
% ssh xbjlabdpwstn05
xbjlabdpwstn05% curl -v --proxy http://localhost:9181 https://www.svlsimulator.com
```

## install


### install unity editor

https://unity3d.com/get-unity/download/archive

``` console
% mkdir -p /scratch/$USER
% cd -P /scratch/$USER
% pwd
% curl --proxy http://localhost:9181 https://www.svlsimulator.com
% curl -Lo UnitySetup-2021.2.17f1 --proxy http://localhost:9181 https://download.unity3d.com/download_unity/efb8f635e7b1/UnitySetup-2021.2.17f1
% ls -l
% chmod +x UnitySetup-2021.2.17f1
% env DISPLAY=127.0.0.1:17941 xterm
% env DISPLAY=127.0.0.1:17941 ALL_PROXY=http://localhost:9181 HTTP_PROXY=http://localhost:9181 ./UnitySetup-2021.2.17f1
% # fix license issue
% /scratch/$USER/Unit-2021.2.17f1/Editor/Unity -batchmode -createManualActivationFile -logfile
% find /scratch/$USER/Unit-2021.2.17f1 -iname '*' # fail, no license
```

https://docs.unity3d.com/hub/manual/InstallHub.html#install-hub-linux

``` console
% sudo sh -c 'echo "deb https://hub.unity3d.com/linux/repos/deb stable main" > /etc/apt/sources.list.d/unityhub.list'
% curl -L --proxy http://localhost:9181 https://hub.unity3d.com/linux/keys/public | sudo apt-key add -
% sudo vim /etc/apt/apt.conf.d/70debconf
% oAcquire::http::proxy "http://localhost:9181"
% sudo apt update
% sudo apt-get install unityhub
% env HTTP_PROXY=http://localhost:9181 DISPLAY=127.0.0.1:17941 unityhub
```

fail again, critical error.

``` console
% sudo apt-get remove unityhub
```

``` console
% mkdir -p /scratch/$USER/Downloads
% cd -P /scratch/$USER/Downloads
% curl -L --proxy http://localhost:9181 -o UnityHub.AppImage https://public-cdn.cloud.unity3d.com/hub/prod/UnityHub.AppImage
% chmod +x UnityHub.AppImage
% env HOME=/scratch/$USER/  DISPLAY=127.0.0.1:17941  HTTP_PROXY=http://localhost:9181 ./UnityHub.AppImage unityhub://2020.3.3f1/76626098c1c4
```


### build svl simulator from source code

``` console

% cd -P /scratch/$USER
% env DISPLAY=127.0.0.1:17941 ALL_PROXY=http://localhost:9181 git clone https://github.com/lgsvl/simulator
% sudo apt install -y git-lfs
% cd -P /scratch/$USER/simulator
% cd -P /scratch/$USER/simulator/Assets/Materials/EnvironmentMaterials/
% #  GUI  stuff
% cd -P /scratch/$USER/Downloads
% env HOME=/scratch/$USER/  DISPLAY=127.0.0.1:17941  HTTP_PROXY=http://localhost:9181 ./simulator
% ldd simulator
```
