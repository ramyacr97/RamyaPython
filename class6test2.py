from netmiko import Netmiko
from getpass import getpass
password = getpass()
cisco3 = {
        "host":'cisco3.lasthop.io',
        "username":'pyclass',
        "password":password,
        "device_type":'cisco_ios',
}
net_conn = Netmiko(**cisco3)
print(net_conn.find_prompt())
show_cmd = net_conn.send_command("show ip int brief")
print(show_cmd)
