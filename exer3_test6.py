from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse
import re
device = {
        'host': 'cisco4.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'device_type': 'cisco_ios',
        'session_log': 'cisco4.txt',
}
net_connect = ConnectHandler(**device)
show_run = net_connect.send_command("show run")
net_connect.disconnect()
cisco_obj = CiscoConfParse("cisco4.txt")
intf = cisco_obj.find_objects_w_child(parentspec=r"^interface",childspec = r"^\s+ip address") #finding object with ip address
for int,addres in enumerate(intf[:]):
    parent = intf[int]
    children = parent.children
    print ("Interface Line: {}".format(parent.text))
    for j in range(0,2):
        match = parent.re_search_children(r"^\s+ip address")
    #print("Interface Line: {}".format(parent.text))
        if 'ip address' in children[j].text:
            print("IP Address Line:",children[j].text)
        else: 
            break


        
