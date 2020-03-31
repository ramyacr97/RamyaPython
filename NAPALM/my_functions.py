from my_devices import device_list
from pprint import pprint
from napalm import get_network_driver
 
def napalm_connect(dev):
    device = dev.copy()
    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    device_conn = driver(**device)
    print()
    device_conn.open()
    print()
    return device_conn

def create_backup(conn):
    backup = conn.get_config()
    filename= f"{conn.hostname}-running.txt"
    with open(filename, "w") as f:
        f.write(backup["running"])

def create_checkpoint(conn):
    """Function use config getter or get checkpoint file and write to disk"""
    if "nxos" in conn.platform:
        filename = f"{conn.hostname}-checkpoint.txt"
        backup = conn._get_checkpoint_file()
        with open(filename, "w") as f:
            f.write(backup)
    else:
        raise ValueError("Checkpoint requires NX-OS")
