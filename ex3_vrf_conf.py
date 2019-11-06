from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
env = Environment()
env.loader = FileSystemLoader('.')
my_val = {
    "vrf_name": 'blue',
    "rd_number": '100:1',
    "ipv4_enabled": 1,
    "ipv6_enabled": 0,
}
template_file = 'vrf_conf.j2'
template = env.get_template(template_file)
output = template.render(**my_val)
print(output)
