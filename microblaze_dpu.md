# setup DPU on microblaze

## install sdk

``` console
% cd ~/build
% scp xcdl190253:/tmp/for_chunye_mb/sdk.sh mb_sdk.sh
% ./mb_sdk.sh -d /group/xbjlab/dphi_software/software/workspace/$USER/mb_sdk/ -y
```


## build them

``` console
% unset LD_LIBRARY_PATH;source /group/xbjlab/dphi_software/software/workspace/chunywan/mb_sdk/environment-setup-microblazeel-v11.0-bs-cmp-re-mh-div-xilinx-linux
% cd /group/xbjlab/dphi_software/software/workspace/chunywan/d/working/aisw/;
% cd unilog; ./cmake.sh
```
