import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
######Question 7A###
device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")
print(etree.tostring(output).decode())
interface = output.find(".//interface")
state = output.find(".//state")
mtu = output.find(".//eth_mtu")
print("Interface:",interface.text,"; State:",state.text,"; MTU:",mtu.text)

####Question 7B####
cmds = [
    "show system uptime",
    "show system resources",
]  

output1 = device.show_list(cmds,raw_text = True)
for entry in output1:
    print(etree.tostring(entry).decode())
    input("Hit enter to continue:")


####### Question 7C#####
cfg_cmd = [
    "interface loopback110",
    "description loopback110",
    "interface loopback111",
    "description loopback111",
]

output2 = device.config_list(cfg_cmd)
for i in range(4):
    print(etree.tostring(output2[i]).decode())
output2 = device.save()
print(output2)
