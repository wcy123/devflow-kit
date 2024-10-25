
#

```
cd $BUILD/loong
ninja -t targets all
ninja -t targets all | grep LoongOpsIncGen
ninja LoongOpsIncGen --verbose
```
