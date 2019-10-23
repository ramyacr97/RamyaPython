import json
from pprint import pprint
filename = "nxos_interfaces.json"
with open(filename) as f:
    output = json.load(f)
ipv4_list = []
ipv6_list = []
for interface,ip in output.items():
    for key in ip:
        if key == 'ipv4':
            ip_list = [ip[key]]
            ipv4_list.append(ip_list)
print("IPv4 list:")
print("-"*50)
print(ipv4_list)
for interface, ip in output.items():
    for key in ip:
        if key == 'ipv6':
            new_list = [ip[key]]
            ipv6_list.append(new_list)
print("IPv6 list:")
print("-"*50)
print(ipv6_list)




