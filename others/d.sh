#!/bin/bash
scp c.sh xbjjmphost02:
function loop ()
{
    eval "$@";
    while sleep 1; do
        eval "$@";
    done
}

loop sshpass -e  ssh  -T xbjjmphost02  bash -xe c.sh $1
