#!/bin/bash
#copy res from /group/xbjlab/dphi_software/software/workspace/mingyue/d
ip=10.176.179.54
sshpass -p root scp /home/mingyue/d/working/aisw/work_log/mingyue/xvdpu/run.sh root@$ip:
sshpass -p root ssh root@$ip 'bash -ex run.sh 0'
