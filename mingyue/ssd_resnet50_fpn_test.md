ssh mingyue@xsjsda153
cd ~/d/working/mingyue/cloud_test
mkdir ssd_resnet50_v1_fpn_coco
cd ssd_resnet50_v1_fpn_coco
scp mingyue@xcdl190256:/group/dphi_builds/jenkins_ws/arch_js/workspace/arch_vitis_ai/models/ssd_resnet50_v1_fpn_coco_compiled.xmodel ./
scp -r mingyue@xcdl190256:/group/modelzoo/internal-cooperation-models/tensorflow_quantize/detection/ssd/ssd_resnet50_v1_fpn_coco/dump_results/dump_results_1 ./
scp -r mingyue@xcdl190256:/group/modelzoo/internal-cooperation-models/tensorflow_quantize/detection/ssd/ssd_resnet50_v1_fpn_coco/dump_results/dump_results_0 ./

ls
export LD_LIBRARY_PATH=/opt/xilinx/xrt/lib:/usr/local/lib:/usr/local/lib64:/home/mingyue/.local/RedHatEnterpriseWorkstation.7.4.x86_64.Release/lib
/home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/xir/test/xir_cat.bin ssd_resnet50_v1_fpn_coco_compiled.xmodel -txir_cat.txt

env XLNX_EBABLE_CLEAR=0 DEBUG_DPU_RUNNER=1 DEBUG_DPU_CONTROLLER=0 XLNX_ENABLE_DEBUG_MODE=0 XLNX_ENABLE_UPLOAD=0 XLNX_ENABLE_DUMP_PARAMTER=0 XLNX_CHECK_COMMIT_ID_ENABLE=0 XLNX_ENABLE_DUMP=1 XLNX_SHOW_DPU_COUNTER=1 /home/mingyue/build/build.RedHatEnterpriseWorkstation.7.4.x86_64.Release/vart/dpu-runner/test/test_dpu_runner ssd_resnet50_v1_fpn_coco_compiled.xmodel resnet50_v1_fpn_coco_0 dump_results_0/image_tensor_aquant.bin 1 1 2>a.log 1>&2



ls



end
