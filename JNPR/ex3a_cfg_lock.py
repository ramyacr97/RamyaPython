from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
from getpass import getpass
from jnpr_devices import srx_device

a_device = {}
if a_device == True:
    a_device = Device(host="srx2.lasthop.io",user="pyclass",password=getpass())
    a_device.open()
    a_device.timeout = 60
    cfg = Config(a_device)
    cfg.lock()

#### Class 8 exercise 3a  importing srx_device###
else:
    srx_device().timeout = 60
    cfg = Config(srx_device())

## Gracefully handle the LockError
    try:
        cfg.lock()
        print("locking the configuration")
    except LockError:
        print("Already locked")


cfg.load("set system host-name python4life", format ="set", merge=True)
#cfg.rollback(0)
print(cfg.diff())
#cfg.commit(comment =" Making hostname change")
### Rollback the configuration ###
print("Making hostname change")
#cfg.load("set system host-name srx2", format = "set", merge=True)
cfg.rollback(0)
print(cfg.diff())
#cfg.commit(comment="Changing back the hostname")
print("Changing the hostname")

