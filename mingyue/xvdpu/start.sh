#!/bin/bash
ip=$1

sshpass -p root scp /home/mingyue/d/working/aisw/work_log/mingyue/xvdpu/run.sh root@$ip:
sshpass -p root ssh root@$ip 'bash -ex run.sh'
