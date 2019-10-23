from netmiko import Netmiko
from getpass import getpass
device = {
        "host": 'cisco4.lasthop.io',
        "username": 'pyclass',
        "password": getpass(),
        "device_type": 'cisco_ios',
}
net_connect = Netmiko(**device)
command = 'show version'
command1 = 'show lldp neighbor'
output = net_connect.send_command(command, use_textfsm = True)
output1 = net_connect.send_command(command1, use_textfsm = True)
lldp_detail = output1[0]
print("The remote device interface is:",lldp_detail.get("neighbor_interface"))
net_connect.disconnect()
