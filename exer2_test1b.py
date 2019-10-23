from netmiko import Netmiko
from getpass import getpass

device1 = {
        "host": 'cisco4.lasthop.io',
        "username": 'pyclass',
        "password": getpass(),
        "device_type": 'cisco_ios'
}
net_connect = Netmiko(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("ping",expect_string=r':', strip_prompt= False, strip_command= False)
output += net_connect.send_command("", expect_string=r'address:', strip_prompt= False, strip_command= False)
output += net_connect.send_command("8.8.8.8", expect_string=r':', strip_prompt= False, strip_command= False)
output += net_connect.send_command("", expect_string=r':', strip_prompt= False, strip_command= False)
output += net_connect.send_command("", expect_string=r':', strip_prompt= False, strip_command= False)
output += net_connect.send_command("", expect_string=r':', strip_prompt= False, strip_command= False)
output += net_connect.send_command("", expect_string=r':', strip_prompt= False,strip_command= False)
output += net_connect.send_command("", expect_string=r':',delay_factor = 100)
print(output
net_connect.disconnect()
