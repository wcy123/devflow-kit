# work env on xbjlabdpwstn05


```console
% ssh xbjlabdpwstn05
% ssh -R10260:localhost:10009  xbjlabdpwstn05
% vi ~/.ssh/config
% ssh -T gits@xcdl190260
% cd /group/xbjlab/dphi_software/software/workspace/$USER/d/working/aisw/xdock-vitis-ai-sw
% git pull
% make shutdown
% make run
localhost % ssh -R10022:
```
