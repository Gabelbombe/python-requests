#!/bin/bash

# ensure running as root
if [ "$(id -u)" != "0" ] ; then
  exec sudo "$0" "$@"
fi

while read server ; do
  if ! grep "^$server " /etc/hosts ; then
    echo '#- marker'                                 >> /etc/hosts
    echo $(tr '\n' ' ' < read/servers.txt) 127.0.0.1 >> /etc/hosts
    break
  fi
done <read/servers.txt
