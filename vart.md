## work with vart


```
cd $HOME/d/working/aisw/vart
git status --untracked-files
git pull --rebase
fd  meta.json .

git clean -fd

rsync -av dpu-runner/samples/adas_detection/model_dir_for_zcu102/ dpu-runner/samples/adas_detection/model_dir_for_zcu104
rsync -av dpu-runner/samples/inception_v1_mt_py/model_dir_for_zcu102/ dpu-runner/samples/inception_v1_mt_py/model_dir_for_zcu104
rsync -av dpu-runner/samples/pose_detection/model_dir_for_zcu102/ dpu-runner/samples/pose_detection/model_dir_for_zcu104
rsync -av dpu-runner/samples/resnet50/model_dir_for_zcu102/ dpu-runner/samples/resnet50/model_dir_for_zcu104
rsync -av dpu-runner/samples/segmentation/model_dir_for_zcu102/ dpu-runner/samples/segmentation/model_dir_for_zcu104
rsync -av dpu-runner/samples/video_analysis/model_dir_for_zcu102/ dpu-runner/samples/video_analysis/model_dir_for_zcu104

git status --untracked-files
git add -A
emacs -nw dpu-runner/samples/adas_detection/model_dir_for_zcu102
```
