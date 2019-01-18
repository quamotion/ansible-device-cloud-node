import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# These packages must NOT be installed
@pytest.mark.parametrize('name', [
  ('kubelet', '1.12.1'),
  ('kubeadm', '1.12.1'),
  ('kubectl', '1.12.1'),
  ('docker-ce', '18.06.0')
])
def test_package_is_installed(host, name, version):
    package = host.package(name)

    assert package.is_installed
