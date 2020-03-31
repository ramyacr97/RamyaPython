from my_functions import napalm_connect, create_backup
from my_devices import device_list
from pprint import pprint

#import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == "__main__":
    connection = []
    for device in device_list:
        conn = napalm_connect(device)
        connection.append(conn)
    for conn in connection:
        output = conn.get_arp_table()
        pprint(output)
    for conn in connection:
        try: 
            pprint(conn.get_ntp_peers())
        except NotImplementedError:
            print("NTP peers not implemented for this device {}".format(conn.platform))
    for conn in connection:
        create_backup(conn)
        conn.close()
    print("\n\n")

