from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import Netmiko
from getpass import getpass
from my_devices import nxos1_connect, nxos2_connect
env = Environment()
env.loader = FileSystemLoader('.')
my_vars = {
    "interface_name": "Ethernet1/2",
    "ip_addr1": "10.1.100.1",
    "ip_addr2": "10.1.100.2",
    "netmask": "255.255.255.0",
    "local_as": 22,
    "nxos1": True,
}
my_vars1 = {
    "nxos2": True,
    "interface_name": "Ethernet1/2",
    "ip_addr1": "10.1.100.1",
    "ip_addr2": "10.1.100.2",
    "netmask": "255.255.255.0",
    "local_as": 22,
}
template_file = 'ex2_nxos_conf.j2'
template = env.get_template(template_file)
nxos1_config = template.render(**my_vars)
nxos2_config = template.render(**my_vars1)
print(nxos1_config)
print(nxos2_config)
nxos1_bgp = nxos1_connect.send_config_set(nxos1_config)
nxos2_bgp = nxos2_connect.send_config_set(nxos2_config)

