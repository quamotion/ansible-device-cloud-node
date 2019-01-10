# Quamotion Device Cloud Node

[![Build Status](https://travis-ci.org/quamotion/ansible-device-cloud-node.svg?branch=master)](https://travis-ci.org/quamotion/ansible-device-cloud-node)

Configures a server to host the Quamotion Device Cloud. This will install
Kubernetes, Helm and VAAPI.

The role targets Ubuntu Server 16.04 and 18.04. 

## Quickstart

If you want to use this role to provision a single-node Kubernetes cluster,
run the following commands:

```
apt-get update
apt-get install -y software-properties-common
apt-add-repository --yes --update ppa:ansible/ansible
apt-get install -y ansible

ansible-galaxy install quamotion.device_cloud_node

ansible localhost -c local -m include_role -a name=quamotion.device_cloud_node -e "device_farm_role=master"
```

## Example Playbooks

### Single node cluster

```yml
- hosts: all

  vars:
    device_farm_role: master

  roles:
    - quamotion.device_cloud_node
```

## License

This Ansible module is licensed under the terms of the MIT License.

## Author Information

This role was created in 2018 by [Quamotion](http://quamotion.mobi), a mobile
test automation company.
