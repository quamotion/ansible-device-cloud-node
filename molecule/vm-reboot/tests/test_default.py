import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_no_swap_in_fstab(host):
    fstab = host.file("/etc/fstab")
    assert not fstab.contains("swap")


# Make sure /proc/swaps contains one line at most (the header),
# and no content like 'file' which would indicate content like this:
# Filename				Type		Size	Used	Priority
# /swapfile                               file		2097148	1631232	-2
def test_no_swaps_in_proc(host):
    swaps = host.file("/proc/swaps")
    assert len(swaps.content_string.split('\n')) < 2
    assert not swaps.contains("file")
    assert not swaps.contains("partition")


# The goal of these tests are to make sure that the Kubernetes cluster
# is still up and running _after_ a reboot.
# The main process which can die is kubelet, which goes in a crash
# loop when, say, swap is enabled (and the playbooks disabled swap
# in a non-presisent manner).
@pytest.mark.parametrize('name', [
    'docker',
    'kubelet'
])
def test_service_is_running(host, name):
    service = host.service(name)

    assert service.is_running


# It never hurts to run some other commands, too.
# Running kubectl get pods will make sure the API server is
# up and running.
# These commands will only be successful once Kubernetes is
# up and running, so there's a delay in the side_effect playbook
# to allow for Kubernetes to start once the VM has rebooted.
def test_kubectl_get_pods_works(host):
    host.run_expect([0], "kubectl get pods -n kube-system")


def test_kubectl_version_works(host):
    host.run_expect([0], "kubectl version")


def test_helm_version_works(host):
    host.run_expect([0], "helm version")


def test_helm_list_works(host):
    host.run_expect([0], "helm list")
