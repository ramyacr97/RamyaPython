from __future__ import unicode_literals, print_function
from netmiko import Netmiko
from getpass import getpass
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
password = getpass()
env = Environment()
env.loader = FileSystemLoader('.')
cisco3 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_ios',
}
my_vars = {
        "ntp_server1":'130.126.24.24',
        "ntp_server2": '152.2.21.1',
        "timezone": 'PST',
        "timezone_offset": '-8',
        "timezone_dst": 'PDT',
}       
net_connect = Netmiko(**cisco3)
template_file = 'base_template.j2'
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)

