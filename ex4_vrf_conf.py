from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
env = Environment()
env.loader = FileSystemLoader('.')
vrf_name = ['blue','red','yellow','green','orange']
rd_number = ['100:1','200:1','300:1','400:1','500:1']
vrf_list = {
    "blue": "100:1",
    "red": "200:1",
    "yellow": "300:1",
    "green": "400:1",
    "orange": "500:1",
}
my_val = {
    "vrf_list": vrf_list,
    "ipv4_enabled": 1,
    "ipv6_enabled": 1,
}
template_file = 'ex4_vrf_conf.j2'
template = env.get_template(template_file)
output = template.render(**my_val)
print(output)
