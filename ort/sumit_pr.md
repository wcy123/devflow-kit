
```
ssh -p 10022 localhost
cd /workspace/onnxruntime
git remote add wcy123 https://github.com/wcy123/onnxruntime.git
set_proxy http://localhost:9181
git fetch --algit p
git pull --rebase
git status
git branch -a | grep vitis
git checkout origin/br-vitis-ai-2.5-v4
# ccc9cb0a1f79cbe2b25c7c7e56bf7b5770f4c002
git checkout -b vitis-ai-3.5-v1
git remote -v show
git rebase upstream/main
git merge-base HEAD upstream/main
```


```
* commit 29ac95dc8e56bf03065964cb06abb4533efd3d89
| Author: Wang Chunye <chunywan@xilinx.com>
| Date:   Mon Oct 24 00:25:35 2022 -0600
|
|     update VitisAI EP to work with Vitis-AI 2.5

* commit c696392f0c709111ddf44b62024bfbd28c6651e8 (tag: vitis-ai-merge-point-3, origin/main)
| Author: Kyushick Lee <kyule@microsoft.com>
| Date:   Wed Mar 8 14:32:23 2023 +0900
|
|     Support external output tensors for DORT (#14516)
|
```


```
git rebase -i c696392f0c709111ddf44b62024bfbd28c6651e8
git rebase upstream/main # 3440d3a08e974aa9f7b586316220f7ae39202256
git show 3440d3a08e
git status
git rebase --continue
git log -- qonnxruntime/core/providers/vitisai/vitisai_execution_provider.cc
git show cf19c3697d126982acf45c040729269e53b5d9f4 --stat | grep vitis
# Run clang-format in CI (#15524)
git show cf19c3697d126982acf45c040729269e53b5d9f4 -- onnxruntime/core/providers/vitisai/vitisai_execution_provider.cc
git push -u origin vitis-ai-3.5-v1
```


```
git remote set-url wcy123 git@github.com:wcy123/onnxruntime.git
```

```
* commit aea7e1729691f212ba8cf0e5b59880f5cfe15398 (HEAD -> vitis-ai-3.5-v2, origin/vitis-ai-3.5-v2, vitis-ai-3.5-v1)
| Author: Wang Chunye <chunywan@xilinx.com>
| Date:   Mon Oct 24 00:25:35 2022 -0600
|
|     update VitisAI EP to work with Vitis-AI 3.5
|
* commit 3440d3a08e974aa9f7b586316220f7ae39202256 (wcy123/main, upstream/main, origin/main, main)
| Author: Yulong Wang <7679871+fs-eire@users.noreply.github.com>
| Date:   Mon Apr 24 18:43:32 2023 -0700
|
|     remove 'lib/' from .gitignore (#15613)
|
|     This will ignore source folder /js/web/lib/
|
|  .gitignore | 1 -
|  1 file changed, 1 deletion(-)
```


# lint runner

```
set_proxy http://localhost:9181
pip install --user lintrunner lintrunner-adapters
lintrung sner -a
git status
git push -u wcy123 vitis-ai-3.5-v2
```


# remove

```
cd /workspace/onnxruntime
git fetch --all
git status
git reset --hard wcy123/vitis-ai-3.5-v2
git log origin/vitis-ai-3.5-v2
git cherry-pick 35654946ce3274d886cb1b06efaa9bafeca9ffc5
for i in `find  onnxruntime/core/providers/vitisai -iname "*.cpp"`; do git mv $i ${i%.cpp}.cc; done
for i in `find  onnxruntime/core/providers/vitisai -iname "*.hpp"`; do git mv $i ${i%.hpp}.h; done
git status
lintrunner -a
git add .
git status
git commit -m 'rename *.cpp -> *.cc and *.hpp -> *.h'
git push

python /workspace/vai-rt/main.py --dev-mode --project onnxruntime
y
n
g c



```



```
 sudo rm -fr /usr/lib/x86_64-linux-gnu/libprotobuf.a
 sudo rm -fr /usr/bin/protoc
# sudo find /usr/share/  -iname '*protobuf*.cmake'
 sudo rm -fr /usr/include/google/protobuf/
 python /workspace/vai-rt/main.py --dev-mode --project onnxruntime
 python /workspace/vai-rt/main.py --dev-mode --project unilog target_factory xir xcompiler vaip --clean
 python /workspace/vai-rt/main.py  --dev-mode --exclude-project onnxruntimecat
```



```
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DBUILD_SHARED_LIBS=ON -DCMAKE_POSITION_INDEPENDENT_CODE=ON -DCMAKE_BUILD_TYPE=Debug -DCMAKE_INSTALL_PREFIX=/home/chunywan/.local/Ubuntu.20.04.x86_64.Debug -DCMAKE_PREFIX_PATH=/home/chunywan/.local/Ubuntu.20.04.x86_64.Debug -DBUILD_PYTHON=ON -DBUILD_TEST=ON -B /home/chunywan/build/build.Ubuntu.20.04.x86_64.Debug/vaip -S /workspace/vaip --debug-find-pkg=Protobuf
```
;;(local-set-key (kbd "C-b") tmux-cc-key-map)
