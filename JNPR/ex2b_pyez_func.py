from jnpr.junos import Device
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx_device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
import sys

def check_connected(device):
    print()
    if device.connected:
        print(f"Device {device.hostname} is connected")
    else:
        print(f"Device {device.hostname} is not connected")
        sys.exit(1)

def gather_routes(device):
    route = RouteTable(srx_device())
    route.get()
    return route

def gather_arp_table(device):
    arp = ArpTable(srx_device())
    arp.get()
    return arp
    

def print_output(dev):
    device = {}
    device["hostname"] = srx_device().facts['hostname']
    device["connected_user"] = dev.user
    device["connected_port"] = dev.port
    device["route_table"] = route.items()
    device["arp_table"] = arp.items()
    pprint(device)
    
if __name__ == "__main__":
    
    device = srx_device()
    check_connected(device)
    route = gather_routes(device)
    arp = gather_arp_table(device)
    print_output(device)
