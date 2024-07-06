#!/bin/sh


for ip in "172.18.116.140 -p 7384" "172.18.116.142 -p 7384" "172.18.116.143 -p 7384" "172.18.116.144 -p 7384" "172.18.116.146 -p 7384"
do
    echo ::---- New session for machine ----

    echo ::---- timestamp
    echo `date +"%y-%m-%d %H:%M:%S"`

    echo ::---- machineIP
    echo $ip

    echo ::---- uptime
    ssh $ip uptime

    echo ::---- free
    ssh $ip free -h

    # echo ::---- df
    # ssh $ip df -h

    echo ::---- ps
    ssh $ip ps -e -o pid,cmd,user,%cpu,%mem,  --sort=-%cpu | head -n 20

    # echo ::---- nvidia-smi ----
    # ssh $ip nvidia-smi

    # echo ::---- passwd ----
    # ssh $ip cat /etc/passwd
done


