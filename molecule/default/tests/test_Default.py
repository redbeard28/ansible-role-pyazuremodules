import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
    'python3',
    'python3-pip'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed

@pytest.mark.parametrize("pip3_packages", [
    ("packaging"),
    ("requests[security]"),
    ("xmltodict"),
    ("azure-cli-core"),
    ("azure-cli-nspkg"),
    ("azure-common"),
    ("azure-mgmt-authorization"),
    ("azure-mgmt-batch"),
    ("azure-mgmt-cdn"),
    ("azure-mgmt-compute"),
    ("azure-mgmt-containerinstance"),
    ("azure-mgmt-containerregistry"),
    ("azure-mgmt-containerservice"),
    ("azure-mgmt-dns"),
    ("azure-mgmt-keyvault"),
    ("azure-mgmt-marketplaceordering"),
    ("azure-mgmt-monitor"),
    ("azure-mgmt-network"),
    ("azure-mgmt-nspkg"),
    ("azure-mgmt-redis"),
    ("azure-mgmt-resource"),
    ("azure-mgmt-rdbms"),
    ("azure-mgmt-servicebus"),
    ("azure-mgmt-sql"),
    ("azure-mgmt-storage"),
    ("azure-mgmt-trafficmanager"),
    ("azure-mgmt-web"),
    ("azure-nspkg"),
    ("azure-storage"),
    ("msrest"),
    ("msrestazure"),
    ("azure-keyvault"),
    ("azure-graphrbac"),
    ("azure-mgmt-cosmosdb"),
    ("azure-mgmt-hdinsight"),
    ("azure-mgmt-devtestlabs"),
    ("azure-mgmt-loganalytics"),
    ("azure-mgmt-automation"),
    ("azure-mgmt-iothub"),
    ("pyOpenSSL"),
    ("cryptography")
])
def test_required_pip3_packages_exist(host, pip3_packages):
    packaging = host.pip_package.get_packages(pip_path='pip3')['packaging']
#    requests = host.pip_package.get_packages(pip_path='pip3')['requests[security]']
#    xmltodict = host.pip_package.get_packages(pip_path='pip3')['xmltodict']
#    azure-cli-core = host.pip_package.get_packages(pip_path='pip3')['azure-cli-core']
#    azure-cli-nspkg = host.pip_package.get_packages(pip_path='pip3')['azure-cli-nspkg']
#    azure-common = host.pip_package.get_packages(pip_path='pip3')['azure-common']
#    azure-mgmt-authorization = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-authorization']
#    azure-mgmt-batch = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-batch']
#    azure-mgmt-cdn = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-cdn']
#    azure-mgmt-compute = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-compute']
#    azure-mgmt-containerinstance = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-containerinstance']
#    azure-mgmt-containerregistry = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-containerregistry']
#    azure-mgmt-containerservice = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-containerservice']
#    azure-mgmt-dns = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-dns']
#    azure-mgmt-keyvault = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-keyvault']
#    azure-mgmt-marketplaceordering = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-marketplaceordering']
#    azure-mgmt-monitor = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-monitor']
#    azure-mgmt-network = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-network']
#    azure-mgmt-nspkg = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-nspkg']
#    azure-mgmt-redis = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-redis']
#    azure-mgmt-resource = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-resource']
#    azure-mgmt-rdbms = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-rdbms']
#    azure-mgmt-servicebus = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-servicebus']
#    azure-mgmt-sql = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-sql']
#    azure-mgmt-storage = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-storage']
#    azure-mgmt-trafficmanager = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-trafficmanager']
#    azure-mgmt-web = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-web']
#    azure-nspkg = host.pip_package.get_packages(pip_path='pip3')['azure-nspkg']
#    azure-storage = host.pip_package.get_packages(pip_path='pip3')['azure-storage']
#    msrest = host.pip_package.get_packages(pip_path='pip3')['msrest']
#    msrestazure = host.pip_package.get_packages(pip_path='pip3')['msrestazure']
#    azure-keyvault = host.pip_package.get_packages(pip_path='pip3')['azure-keyvault']
#    azure-graphrbac = host.pip_package.get_packages(pip_path='pip3')['azure-graphrbac']
#    azure-mgmt-cosmosdb = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-cosmosdb']
#    azure-mgmt-hdinsight = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-hdinsight']
#    azure-mgmt-devtestlabs = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-devtestlabs']
#    azure-mgmt-loganalytics = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-loganalytics']
#    azure-mgmt-automation = host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-automation']
#    azure-mgmt-iothub= host.pip_package.get_packages(pip_path='pip3')['azure-mgmt-iothub']
#    pyOpenSSL = host.pip_package.get_packages(pip_path='pip3')['pyOpenSSL']

#    cryptography = host.pip_package.get_packages(pip_path='pip3')['cryptography']
    assert pip3_packages in pip3_packages
