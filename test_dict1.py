from netmiko import ConnectHandler
from getpass import getpass

device_1 = {
            "host":'nxos1.lasthop.io', 
            "username":'pyclass', 
            "password":getpass(),
            "device_type":'cisco_nxos',
            }
device_2 = {             
            "host":'nxos2.lasthop.io',
            "username":'pyclass',
            "password":getpass(),
            "device_type":'cisco_nxos',
            }
connect = [device_1, device_2]
for i in range(2):
    net_connect = ConnectHandler(**connect[i])
    print(net_connect.find_prompt())



    
