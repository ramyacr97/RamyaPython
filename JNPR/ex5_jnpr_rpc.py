#!usr/bin/env python
from __future__ import print_function
from jnpr_devices import srx_device
from lxml import etree
from getpass import getpass
#from pprint import pprint
a_device = srx_device()
# show version | display xml rpc
# <get-software-information>
xml_out = a_device.rpc.get_software_information()
print(etree.tostring(xml_out, encoding="unicode"))

## show interfaces terse | display xml rpc
#<get-interface-information>
interface_out = a_device.rpc.get_interface_information(terse=True)
print(etree.tostring(interface_out, encoding="unicode"))
xml_out1 = a_device.rpc.get_interface_information(interface_name="fe-0/0/7",terse=True,normalize=True)
print(etree.tostring(xml_out1,pretty_print=True,encoding="unicode"))
