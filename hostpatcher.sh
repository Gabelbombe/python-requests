#!/bin/bash

# ensure running as root
if [ "$(id -u)" != "0" ] ; then
  exec sudo "$0" "$@"
fi


if ! grep "^#- twittermarker " /etc/hosts ; then
  echo -e '\n##+ twittermarker' >> /etc/hosts
  while read server ; do
    [ 'x' != "${server}x" ] && echo -e "127.0.0.1 ${server}.io www.${server}.io" >> /etc/hosts
  done <read/servers.txt
  echo -e '\n##- twittermarker' >> /etc/hosts
fi
