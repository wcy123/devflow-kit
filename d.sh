#!/bin/bash
sshpass -e  scp c.sh c.cmd xbj-pvapjmp11:
sshpass -e  ssh  -T xbj-pvapjmp11  c.cmd $1
