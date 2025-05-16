#!/bin/bash
# remove backup archives
rm -rf /usr/local/backup/*.tar.gz
# remove forgejo backup dumps
rm -rf /usr/local/k8s/forgejo/git/forgejo-dump-*.zip
