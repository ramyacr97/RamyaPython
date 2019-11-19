import pyeapi
from getpass import getpass
from my_funcs import myfunc_yaml_output, myfunc_show_arp
from pprint import pprint

connection = pyeapi.client.connect(**myfunc_yaml_output("arista4_connect.yml"),password=getpass())
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
pprint(myfunc_show_arp(output))


