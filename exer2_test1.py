from netmiko import Netmiko
from getpass import getpass

device1 = {
          "host": 'cisco4.lasthop.io',
          "username": 'pyclass',
          "password": getpass(),
          "device_type": 'cisco_ios',
 }
net_connect = Netmiko(**device1)
print(net_connect.find_prompt())
command = 'ping'
output = [net_connect.send_command_timing(command),
          net_connect.send_command_timing("", strip_prompt=False, strip_command=False),
          net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
          net_connect.send_command_timing('',strip_prompt= False, strip_command= False),
          net_connect.send_command_timing('',strip_prompt= False, strip_command= False),
          net_connect.send_command_timing('',strip_prompt= False, strip_command= False),
          net_connect.send_command_timing('',strip_prompt= False, strip_command= False),
          net_connect.send_command_timing('',strip_prompt= False, strip_command= False, delay_factor =10)]
       

print(output[-1])
net_connect.disconnect()

