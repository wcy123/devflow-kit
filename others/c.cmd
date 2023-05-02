@echo on
echo "hello %1"
dir
mkdir c:\tmp
copy c.sh c:\tmp\
"C:\Program Files\Git\bin\bash.exe" -exc "/c/tmp/c.sh %1"
