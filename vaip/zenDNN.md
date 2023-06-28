

```
emacs -nw ~/.ssh/config
ssh xcdw200210
export W=$HOME/workspace
cd $W
/c/Users/chunywan/AppData/Local/anaconda3/condabin/conda.bat activate zen
cd ZenDNN
export https_proxy=http://127.0.0.1:9181
cmd
set https_proxy=http://127.0.0.1:9181
set OMP_NUM_THREADS=1
echo %OMP_NUM_THREADS%

```


```
git checkout zenDNN_ep
git cherry-pick d35850c142925ad35214bb3cfe82de408fca6bf6 -n
d35850c142925ad35214bb3cfe82de408fca6bf6
```

```
call scripts\zendnn_ONNXRT_env_setup_win.bat
call  "C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Auxiliary\Build\vcvars64.bat"

set ZENDNN_BLIS_PATH=C:\temp\AOCL-Windows\amd-blis\
cd c:\Users\chunywan\workspace
python vai-rt\main.py --dev-mode --project  onnxruntime
set ZENDNN_BLIS_PATH=C:\Program Files\AMD\AOCL-Windows\amd-blis\
xcopy "C:\Program Files\AMD\AOCL-Windows" c:\temp
dir "%ZENDNN_BLIS_PATH%"
echo "%ZENDNN_BLIS_PATH%"

cd ..\ZenDNN_tools
call scripts\zendnn_onnxruntime_setup_win.bat

install LLVM into c:\Program Files\LLVM

ls
dir /?
dir /S AOCL-LibBlis-Win-MT-dll.lib'
```


```

git clone "ssh://chunywan@gerrit-git.amd.com:29418/amd/ec/ZenDNN_utils"
git clone "ssh://chunywan@gerrit-git.amd.com:29418/amd/ec/ZenDNN_tools"
git clone "ssh://chunywan@gerrit-git.amd.com:29418/amd/ec/ZenDNN"
```

```
cd $W/onnxruntime
git status
rm cmake/onnxruntime_mlas.cmake
rm cmake/onnxruntime_python.cmake
git clean -xfd
git checkout --force v1.13.1
```


```
find  /c/Users/chunywan/AppData/Local/anaconda3/ -iname 'conda'
export PATH=/mingw64/bin:/usr/bin:/c/Users/chunywan/bin:/c/Program Files (x86)/Microsoft Visual Studio/Shared/Python39_64/Scripts:/c/Program Files (x86)/Microsoft Visual Studio/Shared/Python39_64:/c/Windows/System32:/c/Windows:/c/Windows/System32/Wbem:/c/Windows/System32/WindowsPowerShell/v1.0:/cmd:/c/Program Files/Microsoft VS Code/bin:/c/Program Files/LLVM/bin:/c/Program Files/GitHub CLI:/c/Program Files/CMake/bin:/c/Users/chiouhon/AppData/Local/Microsoft/WindowsApps:/c/Program Files/OpenSSH:/c/Program Files/OpenSSH-Win64:/c/Users/chunywan/AppData/Local/Microsoft/WindowsApps:/c/Program Files (x86)/Midnight Commander:/c/Users/chunywan/AppData/
alias conda=_conda

/c/Users/chunywan/AppData/Local/anaconda3/condabin/conda.bat create -n zen
/c/Users/chunywan/AppData/Local/anaconda3/condabin/conda.bat activate zen

conda activate zen
echo %windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Users\%USERNAME%\Anaconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\%USERNAME%\Anaconda3' "

```
