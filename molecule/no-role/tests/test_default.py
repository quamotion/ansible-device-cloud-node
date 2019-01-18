import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# These packages must be installed, and at the correct version
@pytest.mark.parametrize('name', [
  'kubelet',
  'kubeadm',
  'kubectl',
  'docker-ce',
  'gitlab-runner',
  'i965-va-driver',
  'libva1',
  'libva2'
])
def test_package_is_installed(host, name, version):
    package = host.package(name)

    assert not package.is_installed


@pytest.mark.parametrize('path', [
    '/usr/local/bin/helm',
    '/etc/kubernetes/kubelet.conf'
])
def test_file_is_installed(host, path):
    assert not host.file(path).exists
