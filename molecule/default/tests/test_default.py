import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kubelet_is_installed(host):
    kubelet = host.package('kubelet')

    assert kubelet.is_installed
    
def test_kubeadm_is_installed(host):
    kubeadm = host.package('kubeadm')

    assert kubeadm.is_installed

def test_kubectl_is_installed(host):
    kubectl = host.package('kubectl')

    assert kubectl.is_installed

def test_docker_is_installed(host):
    docker = host.package('docker')

    assert docker.is_installed