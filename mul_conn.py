from netmiko import Netmiko
from getpass import getpass
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

password = getpass()

cisco3 ={
        'host':'cisco3.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'device_type': 'cisco_ios',
}
cisco4 ={         
        'host':'cisco4.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'device_type': 'cisco_ios',
   }       

for device in (cisco3, cisco4):
    net_conn = Netmiko(**device)
    output = net_conn.send_command("show arp", expect_string = r'#')
    print(output)

