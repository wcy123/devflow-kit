###Compile unilog&xir&vart&vitis-ai-library

```
ssh mingyue@xsjsda153
rm -rf /home/mingyue/.local/RedHatEnterpriseWorkstation.7.4.x86_64.Release
rm -rf /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release
```
```
cd /home/mingyue/d/working/mingyue/unilog
g p
./cmake.sh --type=release

cd /home/mingyue/d/working/mingyue/xir
g p
./cmake.sh --type=release

cd /home/mingyue/d/working/mingyue/vart
g p
./cmake.sh --cmake-options=-DENABLE_DPU_RUNNER=ON --cmake-options=-DENABLE_SIM_RUNNER=OFF --cmake-options=-DENABLE_CPU_RUNNER=OFF --type=release
```
```
cd /home/mingyue/d/working/mingyue/Vitis-AI-Library
g log
>  commit bf1b87061100a7bf1c3ef7a05098802bee812fa5
g stash
g p
./cmake.sh --type=release
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/local/lib:/usr/local/lib64:/home/mingyue/.local/RedHatEnterpriseWorkstation.7.4.x86_64.Release/lib
```
update test_classification_batch.cpp  http://xcdl190260/aisw/Vitis-AI-Library/commit/75519c045ec6b9fa141d4cdb2359a3e03d651074


### Perpare test directory
```
cd /home/mingyue/d/working/mingyue/cloud_test/classification
ls
```

> mingyue@xsjsda153:classification% tree /home/mingyue/d/working/mingyue/cloud_test/classification -L 1<br/>
> /home/mingyue/d/working/mingyue/cloud_test/classification<br/>
> ├── golden<br/>
> ├── images<br/>
> ├── resnet_v1_50_tf<br/>
> ├── sample_classification.jpg<br/>
> └── test_performance_classification.list<br/>
>  <br/>
> 3 directories, 2 files <br/>
> mingyue@xsjsda153:classification% tree /home/mingyue/d/working/mingyue/cloud_test/classification/resnet_v1_50_tf -L 1<br/>
> /home/mingyue/d/working/mingyue/cloud_test/classification/resnet_v1_50_tf<br/>
> ├── meta.json<br/>
> ├── resnet_v1_50_tf.prototxt<br/>
> └── resnet_v1_50.xmodel<br/>
>  <br/>
> 0 directories, 3 files

### Test core0 run 3 images
It's better to use different images
```
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch resnet_v1_50_tf images/001.JPEG images/002.JPEG images/003.JPEG
```

>mingyue@xsjsda153:classification% env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch resnet_v1_50_tf images/001.JPEG images/002.JPEG images/003.JPEG<br/>
> WARNING: Logging before InitGoogleLogging() is written to STDERR<br/>
> I0301 20:38:54.525404  9280 classification_imp.cpp:185] CLASSIFY_SET_IMG : 1763us<br/>
> I0301 20:38:54.525998  9280 dpu_runner_base_imp.cpp:453] subgraph name : subgraph_resnet_v1_50_logits_Conv2D_weights<br/>
> I0301 20:38:54.556119  9280 xrt_cu.cpp:190] XRT_RUN : 30066us<br/>
> I0301 20:38:54.567422  9280 dpu_control_xrt_cloud.cpp:139] core_idx = 0  LSTART 34253  LEND 34253  CSTART 9554  CEND 9554  SSTART 4217  SEND 4217 PSTART 5764  PEND 5764  CYCLE 2957096<br/>
> I0301 20:38:54.567654  9280 classification_imp.cpp:189] CLASSIFY_DPU : 42113us<br/>
> I0301 20:38:54.568022  9280 classification_imp.cpp:204] CLASSIFY_POST_ARM : 349us<br/>
> batch_index 0 image_name images/001.JPEG<br/>
> index 283 score 0.727553 text Persian cat,<br/>
> index 332 score 0.0984637 text Angora, Angora rabbit,<br/>
> index 154 score 0.0597212 text Pekinese, Pekingese, Peke,<br/>
> index 259 score 0.0282103 text Pomeranian,<br/>
> index 903 score 0.0219702 text wig,<br/>
>  <br/>
> batch_index 1 image_name images/002.JPEG<br/>
> index 109 score 0.992801 text brain coral,<br/>
> index 973 score 0.00405735 text coral reef,<br/>
> index 955 score 0.00246091 text jackfruit, jak, jack,<br/>
> index 397 score 0.000122521 text puffer, pufferfish, blowfish, globefish,<br/>
> index 390 score 9.54197e-05 text eel,<br/>
>  <br/>
> batch_index 2 image_name images/003.JPEG<br/>
> index 286 score 0.999784 text cougar, puma, catamount, mountain lion, painter, panther, Felis concolor,<br/>
> index 290 score 7.48357e-05 text jaguar, panther, Panthera onca, Felis onca,<br/>
> index 287 score 5.82821e-05 text lynx, catamount,<br/>
> index 291 score 4.53901e-05 text lion, king of beasts, Panthera leo, <br/>
> index 292 score 1.66981e-05 text tiger, Panthera tigris, <br/>



### Test core1 run 3 images
```
env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch resnet_v1_50_tf images/001.JPEG images/002.JPEG images/003.JPEG

```
> mingyue@xsjsda153:classification% env XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_SHOW_DPU_COUNTER=1 DEEPHI_PROFILING=1 DEBUG_DPU_CORE_ID=0 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/Vitis-AI-Library/classification/test_classification_batch resnet_v1_50_tf images/001.JPEG images/002.JPEG images/003.JPEG<br/>
> WARNING: Logging before InitGoogleLogging() is written to STDERR<br/>
> I0301 20:41:14.793553  9634 classification_imp.cpp:185] CLASSIFY_SET_IMG : 1760us<br/>
> I0301 20:41:14.794163  9634 dpu_runner_base_imp.cpp:453] subgraph name : subgraph_resnet_v1_50_logits_Conv2D_weights<br/>
> I0301 20:41:14.824293  9634 xrt_cu.cpp:190] XRT_RUN : 30045us<br/>
> I0301 20:41:14.834386  9634 dpu_control_xrt_cloud.cpp:139] core_idx = 0  LSTART 34253  LEND 34253  CSTART 9554  CEND 9554  SSTART 4217  SEND 4217 PSTART 5764  PEND 5764  CYCLE 2956840<br/>
> I0301 20:41:14.834640  9634 classification_imp.cpp:189] CLASSIFY_DPU : 40937us<br/>
> I0301 20:41:14.835124  9634 classification_imp.cpp:204] CLASSIFY_POST_ARM : 462us<br/>
> batch_index 0 image_name images/001.JPEG<br/>
> index 283 score 0.727553 text Persian cat,<br/>
> index 332 score 0.0984637 text Angora, Angora rabbit,<br/>
> index 154 score 0.0597212 text Pekinese, Pekingese, Peke,<br/>
> index 259 score 0.0282103 text Pome、fsranian,<br/>
> index 903 score 0.0219702 text wig,<br/>
>  <br/>
> batch_index 1 image_name images/002.JPEG<br/>
> index 109 score 0.992801 text brain coral,<br/>
> index 973 score 0.00405735 text coral reef,<br/>
> index 955 score 0.00246091 text jackfruit, jak, jack,<br/>
> index 397 score 0.000122521 text puffer, pufferfish, blowfish, globefish,<br/>
> index 259 score 0.0282103 text Pomeranian,<br/>
> index 903 score 0.0219702 text wig,<br/>
>  <br/>
> batch_index 1 image_name images/002.JPEG<br/>
> index 109 score 0.992801 text brain coral,<br/>
> index 973 score 0.00405735 text coral reef,<br/>
> index 955 score 0.00246091 text jackfruit, jak, jack,<br/>
> index 397 score 0.000122521 text puffer, pufferfish, blowfish, globefish,<br/>
> index 390 score 9.54197e-05 text eel,<br/>
>  <br/>
> batch_index 2 image_name images/003.JPEG<br/>
> index 286 score 0.999784 text cougar, puma, catamount, mountain lion, painter, panther, Felis concolor,<br/>
> index 290 score 7.48357e-05 text jaguar, panther, Panthera onca, Felis onca,<br/>
> index 287 score 5.82821e-05 text lynx, catamount, <br/>
> index 291 score 4.53901e-05 text lion, king of beasts, Panthera leo, <br/>
> index 292 score 1.66981e-05 text tiger, Panthera tigris, <br/>


end
