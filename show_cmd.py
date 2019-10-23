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
output = net_conn.send_command("show arp", expect_string = r'#')
print(output)

