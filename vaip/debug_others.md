
# login as other users

```
ls
ssh -Jlocalhost:10022 xcdl190253.xilinx.com
docker ps
chunywan.dev.container
user=genmingz
user=hawkwang
docker exec -it $user.dev.container sudo -H -u $user /bin/bash  -l
up
tmux attach
```


# update

```
tmux new -s main -A
vi ~/.ssh/config
set https_proxy=http://127.0.0.1:9181
```
