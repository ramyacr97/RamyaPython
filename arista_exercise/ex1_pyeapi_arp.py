import pyeapi
from getpass import getpass
from pprint import pprint

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
pprint(output)
arp_entry = output[0]['result']['ipV4Neighbors']
for i in range(8):
    for k,v in arp_entry[i].items():
        if k == 'hwAddress':
            Mac_addr = v
        elif k == 'address':
            ip_addr = v
            print(ip_addr,"-->",Mac_addr)
