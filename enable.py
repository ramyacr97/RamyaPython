from netmiko import Netmiko
from getpass import getpass
password = getpass()
my_device ={
        'host':'cisco3.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'secret': password,
        'device_type': 'cisco_ios',
}
net_conn = Netmiko(**my_device)
net_conn.send_command_timing("disable")
print(net_conn.find_prompt())
net_conn.enable()
print(net_conn.find_prompt())

