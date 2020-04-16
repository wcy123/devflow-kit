# rewrite history


https://github.com/git-lfs/git-lfs/issues/326

https://github.com/git-lfs/git-lfs/wiki/Tutorial

## install git lfs

``` console
% curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh |  /tools/xgs/bin/sudo bash
% /tools/xgs/bin/sudo yum install git-lfs
```

## git a list of large files

``` console
% git ls-tree -r -t -l --full-name HEAD | sort -n -k 4 | awk '$4 > 1024*1024*1 { print $5 }' | tee /tmp/large_files
```

## init git lfs


``` console

% cd $HOME/d/working/aisw/vart; ls
% git filter-branch --prune-empty --index-filter 'git rm --ignore-unmatch --cached `cat /tmp/large_files`'
```
