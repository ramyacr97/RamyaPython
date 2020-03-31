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

if __name__ == "__main__":
    connection = []
    for device in device_list:
        conn = napalm_connect(device)
        connection.append(conn)

    for conn in connection:
        print(conn)
        output = conn.get_facts()
        pprint(output)
        conn.close()
        pprint(output)
         
