from netmiko import Netmiko
from getpass import getpass
device = {
        "host": 'cisco3.lasthop.io',
        "username": 'pyclass',
        "password": getpass(),
        "device_type": 'cisco_ios',
       # "fast_cli": True,
}
net_connect = Netmiko(**device)
print(net_connect.find_prompt())

cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup',
]
output = net_connect.send_config_set(cfg)
print(output)
net_connect.disconnect()
