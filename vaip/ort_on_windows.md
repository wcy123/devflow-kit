# on windows


random notes:

## my host name

```
C:\Users\chunywan>hostname
xcdvdiwin10-058
```


## how to map drive to linux directory.

``` console
% net use z: \\xcdswsvm2-lif2\dphi_software
```


## install open ssh

https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse#install-openssh-using-windows-settings

https://thesysadminchannel.com/solved-add-windowscapability-failed-error-code-0x800f0954-rsat-fix/

and enable proxy


```
(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)


Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'


# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
}


New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Program Files\Git\git-bash.exe" -PropertyType String -Force

echo hello
```

## install Anaconda


## connect to

```console
ls
% ssh xcdvdiwin10-058 # from XCD
% # start anaconda
> %windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Users\%USERNAME%\Anaconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\%USERNAME%\Anaconda3' "
% python --version
% conda config --add channels defaults
% conda config --remove channels conda-forge
% conda config --get channels
% conda create -n myenv3 cmake git ninja python vs2019_win-64 boost glog json-c libprotobuf
% conda activate myenv3
% mamba install -c conda-forge json-c
%
% net use z: \\xcdswsvm2-lif2\dphi_software
% function prompt {"$(Split-Path -leaf  -path (Get-Location)) % "}
% $Env:CONDA_PYTHON_EXE --version
% $Env:HTTP_PROXY = "http://127.0.0.1:9181"
% $Env:HTTPS_PROXY = "http://127.0.0.1:9181"
% cmd
% where protoc
% protoc --version
% %comspec% /k "C:\msvsn2019\VC\Auxiliary\Build\vcvars64.bat"
```

## build xrt

```console
% cd Z:\software\workspace\$Env:USERNAME\d\working\xdock-vitis-ai-sw\workspace\aisw\XRT-IPU
%
% $Env:SRC_DIR = "Z:\software\workspace\$Env:USERNAME\d\working\xdock-vitis-ai-sw\workspace\aisw\XRT-IPU"
% dir $Env:SRC_DIR
% cmd
% echo %HTTPS_PROXY%
% mkdir %SRC_DIR%\build-ext


% rmdir /s/q %SRC_DIR%\build-ext
% python %SRC_DIR%\src\runtime_src\tools\scripts\xrtdeps-win19.py --boost skip --icd --opencl --install_dir %CONDA_PREFIX%\Library --build_dir %SRC_DIR%\build-ext"
% c:
% xcopy %SRC_DIR%\build-ext\OpenCL-Headers\CL \include\CL /C/H/E/I/F/Y
% set BUILD_DIR=C:/build/xrt
% echo %SRC_DIR% %BUILD_DIR%
% rmdir /s/q c:\build\xrt
% cmake -G "Ninja" -DCMAKE_BUILD_TYPE=Release -S %SRC_DIR%/src -B C:/build/xrt -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=%CONDA_PREFIX%/Library -DCMAKE_INSTALL_PREFIX=%CONDA_PREFIX%/Library -DCMAKE_CXX_FLAGS="/DBOOST_ALL_NO_LIB /D_WINDOWS /EHsc"
% rmdir /s/q %CONDA_PREFIX%\Library\include\CL
% cmake --build %BUILD_DIR% --config Release --verbose -j 4
% cmake --install %BUILD_DIR% --config Release
% cmake --install %BUILD_DIR% --config Release --prefix %CONDA_PREFIX%/Library # xrt override


## build unilog

``` console
% set SRC_DIR=Z:\software\workspace\%USERNAME%\d\working\xdock-vitis-ai-sw\workspace\aisw\unilog
% set BUILD_DIR=C:/build/unilog
% dir %SRC_DIR%
% cmake -G "Ninja" -DCMAKE_BUILD_TYPE=Release -S %SRC_DIR% -B %BUILD_DIR% -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=%CONDA_PREFIX%/Library -DCMAKE_INSTALL_PREFIX=%CONDA_PREFIX%/Library
% cmake --build %BUILD_DIR% -j 4 --config Release
% cmake --install %BUILD_DIR% --config Release
```

## build xir

``` console
% set SRC_DIR=Z:\software\workspace\%USERNAME%\d\working\xdock-vitis-ai-sw\workspace\aisw\xir
% set BUILD_DIR=C:/build/xir
% dir %SRC_DIR%
% cmake -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=Release -S %SRC_DIR% -B %BUILD_DIR% -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=%CONDA_PREFIX%/Library -DCMAKE_INSTALL_PREFIX=%CONDA_PREFIX%/Library
% cmake --build %BUILD_DIR% -j 4 --config Release
% findstr protoc %BUILD_DIR%\CMakeCache.txt
% protoc --version
% where protoc
% cmake --install %BUILD_DIR% --config Release
```

## build target factory

``` console
% set SRC_DIR=Z:\software\workspace\%USERNAME%\d\working\xdock-vitis-ai-sw\workspace\aisw\target_factory
% set BUILD_DIR=C:/build/target_factory
% dir %SRC_DIR%
% cmake -G "Ninja" -DCMAKE_BUILD_TYPE=Release -S %SRC_DIR% -B %BUILD_DIR% -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=%CONDA_PREFIX%/Library -DCMAKE_INSTALL_PREFIX=%CONDA_PREFIX%/Library
% findstr protoc %BUILD_DIR%\CMakeCache.txt
% cmake --build %BUILD_DIR% -j 4 --config Release
% cmake --install %BUILD_DIR% --config Release
```

## build vart

``` console
% set SRC_DIR=Z:\software\workspace\%USERNAME%\d\working\xdock-vitis-ai-sw\workspace\aisw\vart
% set BUILD_DIR=C:/build/vart
% dir %SRC_DIR%
% rmdir /s/q c:\build\vart
% cmake -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=Release -S %SRC_DIR% -B %BUILD_DIR% -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=%CONDA_PREFIX%/Library -DCMAKE_INSTALL_PREFIX=%CONDA_PREFIX%/Library -DENABLE_DPU_RUNNER=true
% cmake --build %BUILD_DIR% -j 4 --config Release
% cmake --build %BUILD_DIR% -j 4 --config Release --target xrt-device-handle --verbose
% cmake --install %BUILD_DIR% --config Release

% dir C:\build\vart\xrt-device-handle\xrt-device-handle.dir\Release\xrt_device_handle_imp.obj;
% dumpbin /ALL C:\build\vart\xrt-device-handle\xrt-device-handle.dir\Release\xrt_device_handle_imp.obj >c:\a.txt
% dumpbin /ALL C:\Users\chunywan\Anaconda3\envs\myenv3\Library\xrt\lib\xrt_core.lib >c:\b.txt
% dumpbin /ALL C:\Users\chunywan\Anaconda3\envs\myenv3\Library\xrt\lib\xrt_coreutil.lib >c:\b.txt
```

## build xcompiler

``` console
% set SRC_DIR=Z:\software\workspace\%USERNAME%\d\working\xdock-vitis-ai-sw\workspace\aisw\xcompiler
% set BUILD_DIR=C:/build/xcompiler
% dir %SRC_DIR%
% cmake -G "Visual Studio 16 2019" -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Release -S %SRC_DIR% -B %BUILD_DIR% -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=%CONDA_PREFIX%/Library -DCMAKE_INSTALL_PREFIX=%CONDA_PREFIX%/Library
% findstr protoc C:\build\xcompiler\CMakeCache.txt
% cmake --build %BUILD_DIR% -j 4 --config Release --verbose
% cmake --build %BUILD_DIR% -j 4 --config Release --verbose --target xcompiler 1>c:\temp\build.out 2>c:\temp\build.log
% cmake --install %BUILD_DIR% --config Release
% dumpbin /ALL C:\build\xcompiler\src\Release\xcompiler-core.lib >c:\temp\log.txt
% dumpbin /ALL C:\build\xcompiler\src\xcompiler.dir\Release\main.obj >c:\temp\main.txt
```

## build onnxruntime


```console
% z:
% cd Z:\software\workspace\%USERNAME%\d\working\xdock-vitis-ai-sw\workspace\aisw\onnxruntime
% type build.bat
% c:
% set BUILD_DIR=c:\build\onnxruntime\Release
% cd %BUILD_DIR%
% dir %BUILD_DIR%\*.sln
% rmdir /s/q c:\build\onnxruntime;
% python C:\Users\chunywan\Desktop\onnxruntime\tools\ci_build\build.py  --build_shared_lib  --skip_submodule_sync --config Release --parallel 4 --use_vitisai --build_dir c:\build\onnxruntime --cmake_extra_defines "CMAKE_INSTALL_PREFIX=%CONDA_PREFIX%/Library" --skip_tests

% cmake --build %BUILD_DIR% --config Release --target onnxruntime
% cmake --build %BUILD_DIR% --config Release --target onnxruntime --verbose
% cmake --install %BUILD_DIR% --config Release
% dumpbin /ALL C:\Users\chunywan\Anaconda3\envs\myenv3\Library\lib\xir.lib >c:\a.txt
% dir C:\Users\chunywan\Anaconda3\envs\myenv3\Library\lib | findstr vitis
% dumpbin /ALL c:\build\onnxruntime\Release\onnxruntime_providers_vitisai.dir\Release\export_to_xir.obj >c:\b.txt
%
```

## build `test_onnx_runner`

``` console
% mkdir C:\Users\chunywan\Desktop\test_onnx_runner
% copy Z:\software\workspace\%USERNAME%\d\working\xdock-vitis-ai-sw\workspace\aisw\vaip\test\test_onnx_runner.cpp C:\Users\chunywan\Desktop\test_onnx_runner
% code C:\Users\chunywan\Desktop\test_onnx_runner\CMakeLists.txt
% set BUILD_DIR=c:\build\test_onnx_runner
% set SRC_DIR=C:\Users\chunywan\Desktop\test_onnx_runner
% cmake -G "Visual Studio 16 2019" -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Release -S %SRC_DIR% -B %BUILD_DIR% -DCMAKE_BUILD_TYPE=Debug -DCMAKE_PREFIX_PATH=%CONDA_PREFIX%/Library -DCMAKE_INSTALL_PREFIX=%CONDA_PREFIX%/Library
% cmake --build %BUILD_DIR% --config release --verbose
% dir C:\Users\chunywan\Anaconda3\envs\myenv3\Library\include
% cd C:\Users\chunywan\Anaconda3\envs\myenv3\Library\lib
% cd c:\build\onnxruntime
% dir C:\build\test_onnx_runner\Release\test_onnx_runner.exe
% cp -av
% set ENABLE_SAVE_GRAPH_TXT=1
% set XLNX_ENABLE_DUMP_XIR_MODEL=c:\temp\xir.xmodel
% set XLNX_ENABLE_DUMP_ONNX_MODEL=c:\temp\onnx.onnx
% set XLNX_ENABLE_DUMP_COMPILED_MODEL=c:\temp\compiled.xmodel
% set XLNX_ENABLE_DUMP_ONNX_GRAPH_TXT=c:\temp\onnx.txt
% set XLNX_TARGET_NAME=DPUCZDX8G_ISA1_B4096
% set XLNX_TARGET_NAME=DPUCAHX8L_ISA0
% set DUMMY_RUNNER_BATCH_SIZE=1
% set DEBUG_VITIS_AI_EP_DUMMY_RUNNER=1%
% set PATH=%PATH%;%CONDA_PREFIX%\Library\xrt\bin
% scp  -P 23762 xcdl190253:/home/public/zhaolin/pytorch/ENet_xilinx/quantize_result/ENet_int.onnx c:\temp
% C:\build\test_onnx_runner\Release\test_onnx_runner.exe  c:\temp\ENet_int.onnx

```


``` console
% xcopy -av c:
```

## too long file

``` console
% New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
% git config --system core.longpaths true
```
