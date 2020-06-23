#!/bin/bash
tmux new-session -d -c "$PWD" -s 'bjlabdpsrv' 'while sleep 10; do clear; toilet `date`; hostname; done'
tmux split-window -c "$PWD" -p 75 -v 'bash -ex d.sh 04'
tmux split-window -c "$PWD" -p 66 -v 'bash -ex d.sh 15'
tmux split-window -c "$PWD" -p 50 -v 'bash -ex d.sh 16'
tmux -2 attach-session -d
