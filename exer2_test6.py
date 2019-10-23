from netmiko import ConnectHandler
from getpass import getpass
password = getpass()
device = {
        "host": 'cisco4.lasthop.io',
        "username": 'pyclass',
        "password": password,
        "secret": password,
        "device_type": 'cisco_ios',
        "session_log": "my_output.txt",
}
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
print(net_connect.config_mode())
print(net_connect.exit_config_mode())
net_connect.enable()
net_connect.write_channel("disable\n")
net_connect.read_channel()
output = net_connect.find_prompt()
print(output)
net_connect.secret = getpass()
net_connect.enable()
print(net_connect.find_prompt())


