#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import threading
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list as devices

def show_version(a_device):
    print()
    print("#"*80)

