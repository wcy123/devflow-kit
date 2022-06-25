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


## connect to

``` console
% ssh-copy-id -o ProxyJump=localhost:10022 xcdvdiwin10-058
% ssh -J localhost:10022 xcdvdiwin10-058
```

``` console
> %windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Users\chunywan\Anaconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\chunywan\Anaconda3' "

% conda config --set proxy_servers.https http://127.0.0.1:9181
% conda config --set proxy_servers.http http://127.0.0.1:9181
% conda create --name myenv git cmake python vs2019_win-64
% conda activate myenv
% conda list
% python --version
% git --version
% net use z:
% Get-PSDrive
% net use z: \\xcdswsvm2-lif2\dphi_software # ok
% Get-Location
% powershell
% function prompt {"$(Split-Path -leaf  -path (Get-Location)) % "}
% pwd
% cd Z:\software\workspace\chunywan\d\working\xdock-vitis-ai-sw\workspace\aisw
% cd \\xcdswsvm2-lif2\dphi_software\software\workspace\chunywan\d\working\xdock-vitis-ai-sw\workspace\aisw
% ls
% pwd
% Split-Path -leaf  -path (Get-Location)
% git clone gits@xcdl190260:vitis/conda-feedstock.git
% cd \\xcdswsvm2-lif2\dphi_software\software\workspace\chunywan\d\working\xdock-vitis-ai-sw\workspace\aisw\conda-feedstock
% Get-PSDriver
% Set-PSDrive Z
% Set-Location -Path "Z:\"
% cd Z:\software\workspace\chunywan\d\working\xdock-vitis-ai-sw\workspace\aisw\conda-feedstock
% ls
% type build_all.sh
% conda install vs2019_win-64
% conda build  --channel conda-forge  xrt-feedstock
% conda debug --channel conda-forge  xrt-feedstock
% conda purge --channel conda-forge  xrt-feedstock
% $ENV:PATH
% $Env:HTTP_PROXY = "http://127.0.0.1:9181"
% $Env:HTTPS_PROXY = "http://127.0.0.1:9181"
% conda activate myenv1
% conda list
% conda config --help
% conda config --get channels
% conda config --remove channels conda-forge
% mamba config --get channels
% conda config --add channels conda-forge
% conda config --get default
% conda search vs2019
```

``` console
% conda install conda-tree
% conda build  --channel conda-forge  --override-channels  xrt-feedstock
% conda-inspect channels conda-forge
% conda install --channel conda-forge compilers
# https://stackoverflow.com/questions/62288835/how-to-interpret-conda-package-conflicts
% conda install -n base -c conda-forge mamba
% mamba build xrt-feedstock
% mamba debug xrt-feedstock
% mamba create --name myenv2 git
% conda activate myenv2
% conda config --get channels
%
```

``` console
% conda search vs2019
% conda search pyopencl
% conda search opencl
% mamba search --info intel-opencl-rt
% mamba repoquery search intel-opencl-rt
% mamba repoquery depends intel-opencl-rt
% mamba repoquery depends xternsor
% mamba repoquery whoneeds intel-opencl-rt
% mamba install conda-tree
% conda search 'conda-build
```

note:

1. 不要添加 conda-forge
2. 尽量指定版本

``` console
% cd C:\Users\chunywan\Anaconda3\conda-bld\xrt_1656060134849
% cd C:\Users\chunywan\Anaconda3\conda-bld
% cd ".."

% cd C:\Users\chunywan\Anaconda3\conda-bld\xrt_1656060134849\work

% cd C:\Users\chunywan\Anaconda3\conda-bld\xrt_1656060134849\work_moved_xrt-1.1.0-hf8fef2a_1_win-64_main_build_loop #

% dir

```

try to run xrtdeps-win19.py

``` console
% dir src\runtime_src\tools\scripts\xrtdeps-win19.py
% type
% dir src\runtime_src\tools\scripts
% python src\runtime_src\tools\scripts\xrtdeps-win19.py --boost skip --icd --opencl --install_dir %PREFIX% --build_dir %SRC_DIR%\build-release
% dir
```


``` console
% dir %PREFIX%\include

% cd %SRC_DIR%

% python %SRC_DIR%\src\runtime_src\tools\scripts\xrtdeps-win19.py --boost skip --icd --opencl --install_dir %LIBRARY_PREFIX% --build_dir %SRC_DIR%\build-ext

% xcopy %SRC_DIR%\build-ext\OpenCL-Headers\CL %LIBRARY_INC%\CL /C/H/E/I
% xcopy %SRC_DIR%\build-ext\OpenCL-Headers\CL \include\CL /C/H/E/I
% dir %SRC_DIR%\build-ext\OpenCL-Headers\CL

% dir %LIBRARY_INC%\CL
% mkdir %SRC_DIR%\build-release
% cd %SRC_DIR%\build-release
% cmake -G "Ninja" -DCMAKE_BUILD_TYPE=Release -DPython3_EXECUTABLE="%PYTHON%" -S %SRC_DIR%/src -B %SRC_DIR%/build-release -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=%PREFIX% -DCMAKE_INSTALL_PREFIX=%PREFIX% -DCMAKE_CXX_FLAGS="/DBOOST_ALL_NO_LIB /D_WINDOWS /EHsc"
% cmake --build %SRC_DIR%/build-release --config Release --verbose --target xrt_coreutil

% cd %SRC_DIR\build\WRelease%
% cmake --build . --config Release --verbose --target xrt_coreutil

% cmake --build %SRC_DIR%/build-release --config Release --verbose --target xrt_coreutil
% cmake --build %SRC_DIR%/build-release --config Release --verbose --target xdp_core
% cmake --build %SRC_DIR%/build-release --config Release --verbose --target xocl -j 4
% cmake --build %SRC_DIR%/build-release --config Release --verbose -j 4

% cd build-release

% rmdir /S /Q C:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\work\build-release\OpenCL-Headers\CL

% C:\msvsn2019\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64\cl.exe  /nologo /TP -DBOOST_BIND_GLOBAL_PLACEHOLDERS -DBOOST_LOCALE_HIDE_AUTO_PTR -DXRT_AIE_BUILD -DXRT_ENABLE_AIE -D_SILENCE_CXX17_ALLOCATOR_VOID_DEPRECATION_WARNING -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\work\src\runtime_src -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\work\src\runtime_src\core\include -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\work\build-release\gen -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\work\build-release -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\_h_env\Library\include -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\work\src\include\1_2 -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\work\src\runtime_src\xocl\api -I\include /DWIN32 /D_WINDOWS /W3 /GR /EHsc /MD /O2 /Ob2 /DNDEBUG /Zc:__cplusplus /WX /W4 -DXRT_XOCL_SOURCE -std:c++17 /showIncludes /Foruntime_src\xocl\CMakeFiles\xocl.dir\api\clCreateContext.cpp.obj /Fdruntime_src\xocl\CMakeFiles\xocl.dir\ /FS  -c C:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\work\src\runtime_src\xocl\api\clCreateContext.cpp 2>Z:\software\workspace\chunywan\d\working\xdock-vitis-ai-sw\workspace\aisw\tmp\a.txt 1>Z:\software\workspace\chunywan\d\working\xdock-vitis-ai-sw\workspace\aisw\tmp\b.txt

> C:\msvsn2019\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64\cl.exe  /nologo /TP -DBOOST_BIND_GLOBAL_PLACEHOLDERS -DBOOST_LOCALE_HIDE_AUTO_PTR -DXRT_AIE_BUILD -DXRT_ENABLE_AIE -D_SILENCE_CXX17_ALLOCATOR_VOID_DEPRECATION_WARNING -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\work\src\runtime_src -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\work\src\runtime_src\core\include -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\work\build-release\gen -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\work\build-release -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\include -IC:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\work\src\runtime_src\core  /w /MD /O2 /Ob2 /DNDEBUG /Zc:__cplusplus  /W4 -std:c++17  /Foruntime_src\core\common\api\CMakeFiles\core_common_api_library_objects.dir\xrt_bo.cpp.obj /Fdruntime_src\core\common\api\CMakeFiles\core_common_api_library_objects.dir\ /FS -c C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\work\src\runtime_src\core\common\api\xrt_bo.cpp

C:\msvsn2019\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:"C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\work\build\WRelease\runtime_src\core\common\Release\xrt_coreutil.dll" /INCREMENTAL:NO /NOLOGO "C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\lib\libboost_filesystem.lib" "C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\lib\libboost_system.lib" kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:"C:/Users/chunywan/Anaconda3/conda-bld/debug_1656079768710/work/build/WRelease/runtime_src/core/common/Release/xrt_coreutil.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"C:/Users/chunywan/Anaconda3/conda-bld/debug_1656079768710/work/build/WRelease/runtime_src/core/common/Release/xrt_coreutil.lib" /MACHINE:X64  /machine:x64 /DLL C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\work\build\WRelease\runtime_src\core\common\core_common_library_objects.dir\Release\config_reader.obj

C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\lib\libboost_filesystem.lib

dumpbin.exe -headers C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\lib\libboost_filesystem.lib >c:\temp\a.txt

> dumpbin.exe /?
> dumpbin.exe /exports C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\lib\libboost_filesystem.lib >c:\temp\a.txt
> dumpbin.exe /summary C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\lib\libboost_filesystem.lib >c:\temp\a.txt
> dumpbin.exe /directives C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\lib\libboost_filesystem.lib
> dumpbin.exe /headers C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\lib\libboost_filesystem.lib
> dumpbin.exe /relocations C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\_h_env\Library\lib\libboost_filesystem.lib
> findstr libboost_filesystem-vc142-mt-x64-1_73.lib "C:\Users\chunywan\Anaconda3\conda-bld\debug_1656079768710\work\build\WRelease\runtime_src\core\common\core_common_library_objects.dir\Release\config_reader.obj"

2>c:\temp\b.txt

% cd %SRC_DIR%\build

%
% build_ipu19.bat -clean
% build_ipu19.bat -release %LIBRARY_PREFIX%

% type C:\Users\chunywan\Anaconda3\conda-bld\debug_1656062602488\work\build-release\OpenCL-Headers\CL\cl_ext.h

% dir runtime_src\xocl\CMakeFiles\xocl.dir\api\
```

## too long file

``` console
% New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
% git config --system core.longpaths true
```
