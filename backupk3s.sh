#!/bin/bash
# stop k3s
/usr/local/bin/k3s-killall.sh;
/usr/bin/systemctl stop k3s.service;
# tar volumes
/usr/bin/tar czvf /usr/local/backup/k8s$(date +%Y_%m_%d).tar.gz /usr/local/k8s /home/vincent/backupk3s.sh;
# start k3s
/usr/bin/systemctl start k3s.service;
