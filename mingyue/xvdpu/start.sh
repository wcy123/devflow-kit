#!/bin/bash
#copy test files from xbj:/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/xvdpu
run_sh=/group/xbjlab/dphi_software/software/workspace/mingyue/d/working/aisw/work_log/mingyue/xvdpu/run.sh
ip=$1
sshpass -p root scp $run_sh root@$ip:
sshpass -p root ssh root@$ip 'bash -ex run.sh 0'
