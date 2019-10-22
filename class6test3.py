from netmiko import Netmiko
from getpass import getpass
password = getpass()
device1 = {
        "host": 'cisco4.lasthop.io',
        "username": 'pyclass',
        "password": password,
        "device_type": 'cisco_ios',
}
net_connect = Netmiko(**device1)
print(net_connect.find_prompt())
output = net_connect.send_command_timing('ping', strip_prompt= False, strip_command= False)
output+= net_connect.send_command_timing('', strip_prompt= False,strip_command= False)
output+= net_connect.send_command_timing('8.8.8.8', strip_prompt= False, strip_command= False)
output+= net_connect.send_command_timing('', strip_prompt= False,strip_command= False)
output+= net_connect.send_command_timing('', strip_prompt= False,strip_command= False)
output+= net_connect.send_command_timing('', strip_prompt= False,strip_command= False)
output+= net_connect.send_command_timing('', strip_prompt= False,strip_command= False)
output+= net_connect.send_command_timing('', strip_prompt= False,strip_command= False, delay_factor = 100)
print(output)
