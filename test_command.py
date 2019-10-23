from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": 'my_session1.txt'
}
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
output = net_connect.send_command("show version")
print(output)

