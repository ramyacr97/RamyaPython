import json
from pprint import pprint
filename = "arp_arista.json"
with open(filename) as f:
    output = json.load(f)
out = output['ipV4Neighbors']
dict = {}
new_list = []
ip_list = []
for i in range(0,len(out)):
    arp_entry = out[i]
    for keys,values in arp_entry.items():
        if keys == 'hwAddress':
             list = values
             new_list.append(list)
        if keys == 'address':
             list1 = values
             ip_list.append(list1)
print(new_list)
print(ip_list)
    
        
        
        

