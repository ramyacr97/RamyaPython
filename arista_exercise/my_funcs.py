import pyeapi
import yaml
from  getpass import getpass
from  pprint import pprint

def myfunc_yaml_output(filename):
    with open(filename) as f:
        device_dict = yaml.load(f)
        return device_dict
def myfunc_show_arp(output):
    arp_entry = output[0]['result']['ipV4Neighbors']
    print("IP Address    MAC Address")
    for i in range(len(arp_entry)):
        for k,v in arp_entry[i].items():
            if k == 'hwAddress':
                Mac_addr = v
            elif k == 'address':
                ip_addr = v
                print(ip_addr, Mac_addr)
                
   
