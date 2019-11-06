from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
env = Environment()
env.loader = FileSystemLoader('.')
my_vars = {
    "nxos1": 1,
    "nxos2": 1,
    "interface_name": "Ethernet1/1",
    "ip_addr1": "10.1.100.1",
    "ip_addr2": "10.1.100.2",
    "netmask": "255.255.255.0",
    "local_as": 22,
}
template_file = 'nxos_conf1.j2'
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)
#nxos1_run = nxos1_connect.send_command("")
#print(nxos1_run)

