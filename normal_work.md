# some ti



##

``` console
% cd $HOME/d/working/aisw
% for i in unilog target_factory xir vart Vitis-AI-Library ; do (git clone gits@xcdl190260:aisw/$i ); done
% for i in unilog target_factory xir vart Vitis-AI-Library ; do (echo $i; cd $i; git status ); done
% for i in unilog target_factory xir vart Vitis-AI-Library ; do (cd $i; git remote -v show ); done
% for i in unilog target_factory xir vart Vitis-AI-Library ; do (cd $i; git checkout dev ); done
% for i in unilog target_factory xir vart Vitis-AI-Library ; do (cd $i; git branch --set-upstream gits@xcdl190260:wangchunye/$i dev; ) done
% for type in debug release; do for i in unilog target_factory xir vart Vitis-AI-Library ; do (cd $i; bash -e ./cmake.sh --cm
```
