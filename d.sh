#!/bin/bash
sshpass -e  scp c.sh c.cmd xbj-pvapjmp11:
function loop ()
{
    eval "$@";
    while sleep 1; do
        eval "$@";
    done
}

loop sshpass -e  ssh  -T xbj-pvapjmp11  c.cmd $1
