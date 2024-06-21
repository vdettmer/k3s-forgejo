K3s forgejo homelab example
=========

This repository provides a simple example on how to deploy and backup forgejo on a single host k3s. E.g. on a single board computer like a Raspberry Pi.

This is merely intended as inspiration and was originally a beginners Kubernetes learning experience for me.

Limitations
------------

This is merely 3 manifests chained together with static configs for hostname/dns, IP and certificates. It does not come with the aspiration to have dynamic helm chart configuration for multiple use cases.
It also relies on a host path persistent volume located on the single host.

How to setup forgejo?
--------------

Setup k3s on a single host in your lab. Edit externalIPs in the service and ingress hostname according to IP and DNS entry for your k3s in accordance to your lab infrastructure in the example manifests. Sign a certificate for your FQDN/hostname with your lab CA and push it along with your fullchain and secret key into a kubernetes secret.

```
kubectl create secret tls git-vincent-lan \
--key git.vincent.lan.key \
--cert git.vincent.lan.crt
secret "git-vincent-lan" created
```
Adjust tls: portion accordingly

Create path /usr/local/k8s/forgejo on your k3s single host.
```
mkdir -p /usr/local/k8s/forgejo
```

How to setup forgejo backup?
--------------

Put backupk3s.sh into your ssh k3s user's home directory on your k3s single host.
Put initiatebackup.sh to your local machine. Adjust k3s IP in the ssh statement. Execute to initiate a backup dump, follow on screen instructions, adjust backup path in instruction example if needed...

ssh port 222?
--------------

To avoid confusion with ssh port of 22 for the k3s host I chose to setup port 222 for ssh git cloning. Feel free to use the port shift script in the gcportshift directory and alias it to for example fclone on your local machine.
In my .zshrc it looks like this given the script has been copied to /opt/
```
fclone='python /opt/gcportshift.py'
```
I can now clone repositories by using the ssh clone string and by prefixing it with "fclone" instead of "git clone" all consecutive commands are the default git commands.
```
fclone git@git.vincent.lan:vincent/git-clone_port_shift.git
git pull
...
```
