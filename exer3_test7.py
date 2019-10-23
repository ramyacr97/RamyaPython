from __future__ import print_function
from ciscoconfparse import CiscoConfParse
import re
cisco_obj = CiscoConfParse("bgp_info.txt")
neig = cisco_obj.find_objects(linespec = r"neighbor")
bgp_peer =[]
for i in range(0,len(neig)):
    parent = neig[i]
    children = parent.children
    match = re.search(r"^\sneighbor\s(.*)$",neig[i].text, flags=re.DOTALL)
    bgp_ip = match.group(1) 
    for j in range(0,1):
        Result = re.search(r"\d\d",children[j].text.strip()).group()
        bgp_as = Result
    bgp_detail = (bgp_ip,bgp_as)
    print(bgp_detail)   
    new_list = bgp_detail
    bgp_peer.append(new_list)
print("BGP_Peers")
print("-"*50)
print(bgp_peer)
