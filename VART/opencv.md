# install opencv on xbjlabdpsvr15



```
mkdir -p /scratch/chunywan/build
cd /scratch/chunywan/build
curl -Lo opencv-3.4.3.tar.gz https://github.com/opencv/opencv/archive/3.4.3.tar.gz
tar xvf opencv-3.4.3.tar.gz
cd opencv-3.4.3
rm -fr build
mkdir -p build
cd build

sudo yum install epel-release git gcc gcc-c++  qt5-qtbase-devel \
    python python-devel python-pip cmake python-devel python34-numpy \
    gtk2-devel libpng-devel jasper-devel openexr-devel libwebp-devel \
    libjpeg-turbo-devel libtiff-devel libdc1394-devel tbb-devel numpy \
    eigen3-devel gstreamer-plugins-base-devel freeglut-devel mesa-libGL \
    mesa-libGL-devel boost boost-thread boost-devel libv4l-devel

cmake -DBUILD_PERF_TESTS=off -DBUILD_TESTS=off -DBUILD_DOCS=off -DBUILD_EXAMPLES=off -DBUILD_SHARED_LIBS=ON ..
make -j30
sudo make install
```
