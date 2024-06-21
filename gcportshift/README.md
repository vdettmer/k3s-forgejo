# git clone portshift

A cheap python port shifter for git clone using SSH.
I made this because I deployed a forgejo git server on my docker host and wanted to clone using SSH.
I forwarded 22 of the container to port 222 on my host as 22 already was the SSH of the container host itself and I couldn't be bothered to add another domain to my reverse proxy just for SSH cloning.

Feel free to customize the port variable to your specific port and set an alias. I for example made an alias "fclone" for this python script on my systems.

So instead of "git clone ssh://git@odroid.vincent.local:222/vincent/test.git" I simply type "fclone git@odroid.vincent.local:vincent/test.git". "git@odroid.vincent.local:vincent/test.git" being the URL I copy out of the SSH field on my forgejo server for the specific repository I want to clone.