

``` console
:workspace chunywan % rsync -avz localhost:/group/dphi_algo/chenchen/semanticfpn_new /tmp/ # on xcdl190252
:workspace chunywan % /group/dphi_algo/chenchen/Woodscape/WoodScape_ICCV19/previous_images
chunywan@xcdl190252:~% rsync -avz /tmp/semanticfpn_new xbjlabdpwstn05:/scratch/chunywan/
:workspace chunywan % rsync -avz  xbjlabdpwstn05:/scratch/chunywan/semanticfpn_new /opt/workspace/ # on xbjlabdpwstn05
```


``` console
% mkdir -p /workspace/aisw/semanticfpn_new
% cd /workspace/aisw/semanticfpn_new
% ls -l
% export http_proxy=http://localhost:9181;export https_proxy=http://localhost:9181
% pip install -r requirements.txt
```


copy images

``` console
% IMG=08102_MVR.png
% IMG=05438_MVR.png
% rsync localhost:/group/dphi_algo/chenchen/Woodscape/WoodScape_ICCV19/rgb_images/$IMG  /tmp/
% rsync localhost:/group/dphi_algo/chenchen/Woodscape/WoodScape_ICCV19/semantic_annotations/semantic_annotations/gtLabels/$IMG  /tmp/
% rsync /tmp/$IMG  xbjlabdpwstn05:/scratch/chunywan/
% mkdir -p /workspace/aisw/semanticfpn_new/images/rgb_images
% rsync localhost:/scratch/chunywan/$IMG /workspace/aisw/semanticfpn_new/images/rgb_images
%
% mkdir -p /workspace/aisw/semanticfpn_new/images/gtLabels
% rsync localhost:/scratch/chunywan/$IMG /workspace/aisw/semanticfpn_new/images/gtLabels
%
```
