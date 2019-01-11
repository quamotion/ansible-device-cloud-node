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
    docker = host.package('docker-ce')

    assert docker.is_installed


def test_docker_is_enabled(host):
    docker = host.service("docker")

    assert docker.is_enabled


def test_docker_is_running(host):
    docker = host.service("docker")

    assert docker.is_running


def test_docker_version_works(host):
    host.run_expect([0], "docker version")


def test_kubectl_version_works(host):
    host.run_expect([0], "kubectl version")


def test_helm_version_works(host):
    host.run_expect([0], "helm version")


def test_helm_list_works(host):
    host.run_expect([0], "helm list")
