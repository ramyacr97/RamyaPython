#!usr/bin/env python
import pyeapi
import yaml
from getpass import getpass
from pprint import pprint
from jinja2 import Template

## Loading the yaml file
with open("arista_connect.yml") as f:
    device_dict = yaml.load(f)
new_list = []
### Keys in the dictionary stored in a list
for k in device_dict.keys():
    new_list.append(k)
#for i in range(len(new_list)):
#    connection = pyeapi.client.connect(**device_dict[new_list[i]],password=getpass())
 #   device = pyeapi.client.Node(connection)
 #   show_ip_route = device.enable("show ip interface brief")
 #   print(new_list[i])
 #   pprint(show_ip_route)
intf_vars = {}
connect_dict = {}
arista_1 = device_dict[new_list[0]]
arista_2 = device_dict[new_list[1]]
arista_3 = device_dict[new_list[2]]
arista_4 = device_dict[new_list[3]]
for k,v in arista_1.items():
    if k == 'data':
        intf_vars = arista_1[k]
    else:
        connect_dict[k] = arista_1[k]
connection = pyeapi.client.connect(**connect_dict,password=getpass())
device = pyeapi.client.Node(connection)
interface_config = '''
interface {{ intf_name }}
  ip address {{ intf_ip }}/{{ intf_mask }}

'''
j2_template = Template(interface_config)
output = j2_template.render(**intf_vars)
print(output)
config_1 = output.strip('/n')
config_list = config_1.split('\n')
print(config_list)
cfg = config_list[1:3]
out = device.config(cfg)
print(out)
show_ip_int = device.enable("show ip interface brief")
pprint(show_ip_int)
