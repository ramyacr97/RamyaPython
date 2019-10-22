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
cfg_command = ['logging buffered 8000','logging console']
output = net_conn.send_config_set(cfg_command)
print(output)
filename = 'change_file.txt'
out = net_conn.send_config_from_file(filename)
print('-'*50)
print(out)
show_run = net_conn.send_command("show run")
print(show_run)
show_ip_arp = net_conn.send_command("show ip arp", use_textfsm = True)
print(show_ip_arp)
