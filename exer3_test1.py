from __future__ import print_function
from pprint import pprint
with open("arp_data.txt") as f:
    output = f.readlines()
F = []
list = []
for i in range(1,len(output)):
    F = output[i].split()
    ip_address = F[1]
    mac_address = F[3]
    interface = F[5]
    arp_entry = {}
    arp_entry['mac_address'] = F[3]
    arp_entry['ip_address'] = F[1]
    arp_entry['interface'] = F[5]
    list.append(arp_entry)
print(list) 
