from netmiko import Netmiko
from getpass import getpass
Device1 = {
        "host": 'nxos1.lasthop.io',
        "username": 'pyclass',
        "password": getpass(),
        "device_type": 'cisco_nxos',
}
Device2 = {
         "host": 'nxos2.lasthop.io',
         "username": 'pyclass',
         "password": getpass(),
         "device_type": 'cisco_nxos',
}
net_connect1 = Netmiko(**Device1)
net_connect2 = Netmiko(**Device2)
net_connect = [net_connect1, net_connect2]
for i in range(2):
    print(net_connect[i].find_prompt())
    output = net_connect[i].send_config_from_file(config_file='my_changes.txt')
    print(output)
    save_out = net_connect[i].save_config()
    print(save_out)
    net_connect[i].disconnect()
