from jnpr.junos import Device
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx_device

a = srx_device()
print(a.facts)



