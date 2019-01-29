#!/bin/bash
sudo apt-get -qq update
sudo apt-get -y install snapd
sudo snap install lxd

sudo sh -c 'echo PATH=/snap/bin:$PATH >> /etc/environment'

while [ ! -S /var/snap/lxd/common/lxd/unix.socket ]
do
  echo "Waiting for LXD socket..."
  sleep 0.2
done

sudo lxd init --auto
sudo usermod -a -G lxd travis

lxd.lxc network list
lxd.lxc storage list
