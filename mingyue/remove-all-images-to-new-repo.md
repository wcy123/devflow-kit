```
cd $HOME/d/working/mingyue/
ls
git clone gits@xcdl190260:aisw/vitis-ai-library-samples-res.git
cd ../Vitis-AI-Library
pwd
git checkout a8fbf93cd2c56db15b25669fa8352e0b7a6755ab
g ll
ls
cp -r overview/samples ../vitis-ai-library-samples-res/
cp -r overview/demo ../vitis-ai-library-samples-res/
cp -r overview/images ../vitis-ai-library-samples-res/
ls overview
cp overview/*.png ../vitis-ai-library-samples-res/
cp overview/*.dot ../vitis-ai-library-samples-res/
cp overview/*.jpg ../vitis-ai-library-samples-res/


find . -iname "*.jpg"
find . -iname "*.JPG"
find . -iname "*.jpeg"
find . -iname "*.JPEG"
find . -iname "*.png"
find . -iname "*.PNG"

cd ../vitis-ai-library-samples-res/
ls
cd demo
ls
```
for each all directory:
rm *.hpp *.cpp *.sh readme build.sh
