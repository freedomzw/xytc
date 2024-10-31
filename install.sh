#!/bin/bash

if [ "$(id -u)" -eq 0 ]; then
  echo "current user is root, please login system with user not root."
  exit 0
fi

homepath=$HOME
curuser=$USER
mkdir -p $HOME/.ssh
sudo chmod 700 $HOME/.ssh

curuser=$USER
echo "HOME path:$homepath"
echo "Current User:$curuser"

SUDODESC="$curuser ALL=(ALL:ALL) NOPASSWD:ALL"
sudo chmod 555 /etc/sudoers
sudo echo $SUDODESC | sudo tee -a /etc/sudoers
sudo chmod 440 /etc/sudoers

rootpath=/usr/cg

sudo mkdir -p $rootpath
sudo chmod a+rwx $rootpath

if [ -f "$rootpath/bm.tar.gz" ]; then
      	rm -f $rootpath/bm.tar.gz
fi

sudo systemctl stop bm-agent

sudo wget https://github.com/freedomzw/xytc/blob/main/bm-1.7.6.3.3229902.tar.gz -O $rootpath/bm.tar.gz

if [ -f "$rootpath/bm.tar.gz" ]; then
      	echo "download file success"
else
      	echo "download failed!"
      	exit 0
fi

tar -zxvf $rootpath/bm.tar.gz -C $rootpath

if [ -f "$rootpath/bm/bm-agent" ]; then
      	echo "unpress package success"
else
      	echo "unpress failed!"
      	exit 0
fi

sudo chmod -R a+rwx $rootpath/bm

if [ $# -eq 3 ]; then
	sudo $rootpath/bm/run.sh $1 $2 $3 $homepath
elif [ $# -eq 4 ]; then
	sudo $rootpath/bm/run.sh $1 $2 $3 $homepath $4
else
	echo "param error"
fi

if ps aux | grep -v grep | grep "bm-agent" >/dev/null; then
    	echo "bm-agent service is running..."
else
    	echo "bm-agent service start failed"
fi

echo "bm-agent install successful"


