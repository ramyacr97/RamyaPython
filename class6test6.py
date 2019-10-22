from netmiko import Netmiko
from getpass import getpass
password = getpass()
arista1 = {
        "host": 'arista1.lasthop.io',
        "username": 'pyclass',
        "password": password,
        "device_type":'arista_eos',
}
srx2 = {
        "host": 'srx2.lasthop.io',
        "username": 'pyclass',
        "password": password,
        "device_type":'juniper_junos',
}
nxos1 = {
        "host": 'nxos1.lasthop.io',
        "username": 'pyclass',
        "password": password,
        "device_type":'cisco_nxos',
}
for device in (arista1, srx2, nxos1):
    net_conn = Netmiko(**device)
    print(net_conn.find_prompt())
    output = net_conn.send_command("show version")
    print(output)

