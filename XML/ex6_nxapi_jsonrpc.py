import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")
print(output)
interface_keys = output['TABLE_interface']['ROW_interface']
for key,value in interface_keys.items():
    if key == 'interface':
        print("Interface",interface_keys[key])
    elif key == 'state':
        print("STATE",interface_keys[key])
    elif key == 'eth_mtu':
        print("MTU",interface_keys[key])
    
