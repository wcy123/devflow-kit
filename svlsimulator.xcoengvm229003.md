# svglsimulator

https://www.svlsimulator.com/docs/installation-guide/build-instructions/

## prerequisite

``` console
% ssh xbjlabdpwstn05
% sudo apt install libvulkan1
```

## create tunel


## install


### install unity editor
``` console
% mkdir -p /home/build/$USER/Downloads
% cd -P /home/build/$USER/Downloads
% curl -L -o UnityHub.AppImage https://public-cdn.cloud.unity3d.com/hub/prod/UnityHub.AppImage
% chmod +x UnityHub.AppImage
% ./UnityHub.AppImage --appimage-extract
% env HOME=/home/build/$USER/  DISPLAY=127.0.0.1:17941 squashfs-root/AppRun unityhub --no-sandbox unityhub://2020.3.19f1/68f137dc9bbe
```


### build svl simulator from source code

``` console
% cd -P /home/build/$USER/
% git clone
% git clone https://github.com/lgsvl/simulator
% cd -P /home/build/$USER/simulator
% git lfs pull
% #  GUI  stuff
% cd -P /scratch/$USER/Downloads
% env HOME=/scratch/$USER/  DISPLAY=127.0.0.1:17941  HTTP_PROXY=http://localhost:9181 ./simulator
% ldd simulator
```
