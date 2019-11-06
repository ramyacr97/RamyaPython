from netmiko import Netmiko
from getpass import getpass
password = getpass()
nxos1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_nxos',
}
nxos2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_nxos',
}
nxos1_connect = Netmiko(**nxos1)
nxos2_connect = Netmiko(**nxos2)
print(nxos1_connect.find_prompt())
print(nxos2_connect.find_prompt())

