import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# These packages must be installed, and at the correct version
@pytest.mark.parametrize('name,version', [
  ('kubelet', '1.12.1'),
  ('kubeadm', '1.12.1'),
  ('kubectl', '1.12.1'),
  ('docker-ce', '18.06.0')
])
def test_package_is_installed(host, name, version):
    package = host.package(name)

    assert package.is_installed
    assert package.version.startswith(version)


# These services must be enabled.
@pytest.mark.parametrize('name', [
    'docker',
    'kubelet'
])
def test_service_is_enabled(host, name):
    service = host.service(name)

    assert service.is_enabled


# These sevices must be running
@pytest.mark.parametrize('name', [
    'docker',
    'kubelet'
])
def test_service_is_running(host, name):
    service = host.service(name)

    assert service.is_running


def test_docker_version_works(host):
    host.run_expect([0], "docker version")


def test_kubectl_version_works(host):
    host.run_expect([0], "kubectl version")


def test_helm_version_works(host):
    host.run_expect([0], "helm version")


def test_helm_list_works(host):
    host.run_expect([0], "helm list")
