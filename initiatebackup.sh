#!/bin/bash
name=forgejo
ns=default
selector=$(kubectl get --raw "/apis/apps/v1/namespaces/${ns}/deployments/${name}/scale" | jq -r .status.selector)
pod=$(kubectl get pods -n "${ns}" --selector "${selector}" | grep Running | cut -d " " -f 1)
echo -e "Pod $pod found.\nInstructing backup..."
kubectl exec -it $pod -- sh -c "su -c '/app/gitea/gitea dump -c /data/gitea/conf/app.ini' - git"
echo -e "Forgejo dumped.\nCommandeering cluster backup..."
ssh 192.168.178.6 "sudo bash backupk3s.sh"
echo -e "Backup created. Please SCP the archive to your local drive:\nscp 192.168.178.6:/usr/local/backup/k8s$(date +%Y_%m_%d).tar.gz /mnt/daten/backup/k8s"
