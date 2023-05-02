#

``` console
% ssh root@10.176.179.165
% ssh -XY b0
% cd /home/root/segs_and_roadline_and_pose_detect
% export DEMO_VIDEO_WRITER='appsrc ! videoconvert ! ximagesink'
% env LD_LIBRARY_PATH=/home/wcy/lib GST_DEBUG=2 DEBUG_DEMO=2 DEMO_USE_X=1 DEMO_VIDEO_WRITER_WIDTH=1664 DEMO_VIDEO_WRITER_HEIGHT=840 DEMO_USE_VIDEO_WRITER=1 ~/a.out -v  seg_512_288.avi -m multitask -v seg_512_288.avi -m multitask -v seg_512_288.avi -m multitask -v  seg_512_288.avi -m multitask  -v lane_640_480.avi -m roadline
% env LD_LIBRARY_PATH=/home/wcy/lib GST_DEBUG=2 DEBUG_DEMO=2 DEMO_USE_X=0 DEMO_VIDEO_WRITER_WIDTH=1664 DEMO_VIDEO_WRITER_HEIGHT=840 DEMO_USE_VIDEO_WRITER=1 ~/a.out -v  seg_512_288.avi -m multitask -v seg_512_288.avi -m multitask -v seg_512_288.avi -m multitask -v  seg_512_288.avi -m multitask  -v lane_640_480.avi -m roadline
% env LD_LIBRARY_PATH=/home/wcy/lib GST_DEBUG=2 DEBUG_DEMO=2 DEMO_USE_X=0 DEMO_VIDEO_WRITER_WIDTH=1664 DEMO_VIDEO_WRITER_HEIGHT=840 DEMO_USE_VIDEO_WRITER=1 ~/a.out -v  a.jpg -m multitask -v seg_512_288.avi -m multitask -v b.jpg -m multitask -v  seg_512_288.avi -m multitask  -v lane_640_480.avi -m roadline -v 3 -m pose
```
