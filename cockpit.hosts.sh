#!/bin/bash
HOSTS="/etc/hosts"
HOSTNAME=$1
IP=$2
FUNCAO=$3

function step1(){
grep $HOSTNAME $HOSTS 1> /dev/null
case $? in
    1) echo "$IP $HOSTNAME" >> $HOSTS; step2;;
esac
}
function step2(){
cock=$(find /etc/cockpit/machines.d/ -type f -name $HOSTNAME.json)
if [ $cock -z ]; then
    echo 0 > /tmp/cockpit_check.txt
else
    echo 1 > /tmp/cockpit_check.txt
fi
exit 0
}
$FUNCAO
