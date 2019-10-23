import yaml
from netmiko import Netmiko
filename = input("Enter the filename:")
with open(filename) as f:
    yaml_out = yaml.load(f)
device = yaml_out['cisco3']
net_connect = Netmiko(**device)
print(net_connect.find_prompt())

