# how to check processes on windows

``` console
% sshpass -e ssh xbj-pvapjmp11 powershell
% netstat -n -a -o -n  | Select-String -Pattern '214.*LISTEN'
% Get-Process -IncludeUserName
% $owners = @{}
% gwmi win32_process |% {$owners[$_.handle] = $_.getowner().user}
% get-process | select processname,Id,@{l="Owner";e={$owners[$_.id.tostring()]}}
% Get-Process -IncludeUserName | Where {$_.username -eq "XLNX\chunywan" }
% Get-Process -IncludeUserName | Where {$_.username -eq "XLNX\chunywan" } | Stop-Process
% Get-Process -Id  29000 -IncludeUserName
```
