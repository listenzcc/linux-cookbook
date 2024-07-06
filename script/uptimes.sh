#!/bin/sh


for ip in 172.18.116.140 172.18.116.141 172.18.116.142 172.18.116.143 "172.18.116.144 -p 7384" 172.18.116.146
do
    echo ---------------------------------------------------
    echo ---- `date +"%y-%m-%d %H:%M:%S"` ----
    echo ---- $ip ----

    echo
    ssh $ip uptime

    echo
    ssh $ip df -h

    echo
    ssh $ip ps -e -o pid,cmd,user,%cpu,%mem,  --sort=-%cpu | head -n 11

    # echo
    # ssh $ip cat /etc/passwd

    # echo
    # ssh $ip nvidia-smi

    # echo
    # ssh $ip ls /nfs

    echo
    cat /nfs/mount_cmd.sh

done


