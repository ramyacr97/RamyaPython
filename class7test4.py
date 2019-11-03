#!/usr/bin/env python
from pprint import pprint
import yaml
import jinja2
with open("interfaces1.yml") as f:
    output = yaml.load(f)
my_list = []
new_list = []
switchport_mode = []
access_vlan = []
for i in output.values():
    for k,v in i.items():
        my_list.append(k)
        new_list.append(v)
for i in range(3):
    switchport_mode.append(new_list[i].get('mode'))
    if 'access' in switchport_mode[i]:
        access_vlan.append(new_list[i].get('vlan'))
    elif 'trunk' in switchport_mode[i]:
        native_vlan = new_list[i].get('native_vlan')
        trunk_vlans = new_list[i].get('trunk_vlans')
my_vars = {
        "my_list": my_list,
        "switchport_mode": switchport_mode,
        "access_vlan": access_vlan,
        "native_vlan": native_vlan,
        "trunk_vlans": trunk_vlans,
}
interface_template = '''
{%- for i in range(3) %}
interface {{ my_list[i] }}
    {%- if my_list[i] == 'Ethernet1' %}
    switchport mode {{ switchport_mode[i] }}
    switchport access vlan {{ access_vlan[i] }}
    {%- elif my_list[i] =='Ethernet2' %}
    switchport mode {{ switchport_mode[i] }}
    switchport access vlan {{ access_vlan[i] }}
    {%- elif my_list[i] == 'Ethernet3' %}
    switchport mode {{ switchport_mode[i] }}
    switchport trunk native vlan {{ native_vlan }}
    switchport trunk allowed vlan {{ trunk_vlans }}
    {%- endif %}
{%- endfor %}
'''
t = jinja2.Template(interface_template)
print(t.render(**my_vars))

