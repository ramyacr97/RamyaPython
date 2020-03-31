from jnpr.junos import Device
from pprint import pprint
from getpass import getpass
password = getpass()

def srx_device():
    srx2 = {
    "host":'srx2.lasthop.io',
    "user":'pyclass',
    "password":password,
    }
    srx_device = Device(**srx2)
    return srx_device.open()
    

