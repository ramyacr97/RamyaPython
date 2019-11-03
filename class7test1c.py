#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from jinja2 import Template
my_vars = {
        "501": "blue501",
        "502": "blue502",
        "503": "blue503",
        "504": "blue504",
        "505": "blue505",
        "506": "blue506",
        "507": "blue507",
        "508": "blue508",
}
template_vars = {
        "my_vars": my_vars,
}

vlan_config = '''
{%- for key,value in my_vars.items() %}
vlan {{ key }}
    name {{ value }}
{%- endfor %}
'''
j2_template = Template(vlan_config)
output = j2_template.render(**template_vars)
print(output)
