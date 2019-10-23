from netmiko import Netmiko
from getpass import getpass
device1 = {
            "host": 'nxos2.lasthop.io',
            "username": 'pyclass',
            "password": getpass(),
            "device_type": 'cisco_nxos',
            "global_delay_factor": 2,
}
net_connect = Netmiko(**device1)
print(net_connect.find_prompt())
command = 'show lldp neighbors detail'
output = net_connect.send_command(command, delay_factor= 8)
print(output)
net_connect.disconnect()
