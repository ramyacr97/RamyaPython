from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader('.')
my_vars = {
    "nxos1": True,
    "nxos2": True,
    "interface_name": "Ethernet1/1",
    "ip_addr1": "10.1.100.1",
    "ip_addr2": "10.1.100.2",
    "netmask": "255.255.255.0",
}
template_file = 'nxos_conf.j2'
template = env.get_template(template_file)
output = template.render(**my_vars)
print ('-'*50)
print(output)
print ('-'*50)
