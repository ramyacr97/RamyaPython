#!/usr/bin/ env python
import pyeapi
import yaml
from getpass import getpass
from pprint import pprint

filename = "arista4_connect.yml"
with open(filename) as f:
    device_dict = yaml.load(f)
print(device_dict)
connection = pyeapi.client.connect(**device_dict,password=getpass())
device = pyeapi.client.Node(connection)
show_arp = device.enable("show ip arp")
arp_entry = show_arp[0]['result']['ipV4Neighbors']
for i in range(10):
    for k,v in arp_entry[i].items():
        if k == 'hwAddress':
            Mac_addr = v
        elif k == 'address':
            ip_addr = v
            print(ip_addr, "-->", Mac_addr)
