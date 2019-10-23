from __future__ import print_function
list =[]
dict_1 = {
    'device_name': 'nxos1',
    'host': 'nxos1.lasthop.io',
    'username': 'cisco',
    'password': 'cisco123',
}
dict_2 = {
    'device_name': 'cisco3',
    'host': 'cisco3.lasthop.io',
    'username': 'admin',
    'password': 'cisco123',
}
dict_3 = {
    'device_name': 'arista1',
    'host': 'arista1.lasthop.io',
    'username': 'admin',
    'password': 'arista123',
}
dict_4 = {
    'device_name': 'srx2',
    'host': 'srx2.lasthop.io',
    'username': 'junos2',
    'password': 'admin123',
}
list = [dict_1,dict_2,dict_3,dict_4]
print(list)
