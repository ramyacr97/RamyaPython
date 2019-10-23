import yaml
list = [{'device_name': 'nxos1', 'host': 'nxos1.lasthop.io', 'username': 'cisco', 'password': 'cisco123'}, {'device_name': 'cisco3', 'host': 'cisco3.lasthop.io', 'username': 'admin', 'password': 'cisco123'}, {'device_name': 'arista1', 'host': 'arista1.lasthop.io', 'username': 'admin', 'password': 'arista123'}, {'device_name': 'srx2', 'host': 'srx2.lasthop.io', 'username': 'junos2', 'password': 'admin123'}]
filename = "output.yml"
with open(filename, "w") as f:
    output = yaml.dump(list,f)
