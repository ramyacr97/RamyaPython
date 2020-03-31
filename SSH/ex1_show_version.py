from __future__ import print_function, unicode_literals
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list 


def Netmiko_connect(device,command):
    """Execute show version command using Netmiko."""
    print()
    print("#" * 80)
    remote_conn = ConnectHandler(**device)
    output = remote_conn.send_command_expect("show version")
    remote_conn.disconnect()
    return output



def main():
    start_time = datetime.now()
    
    for device in device_list:
        output =Netmiko_connect(device, "show version")
        print(output)

    print("\nElapsed time: " + str(datetime.now() - start_time))

if __name__ == "__main__":
    main()

