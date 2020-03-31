from getpass import getpass

password = getpass()
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}
arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "global_delay_factor": 4,
}
arista2 = {
    "device_type": "arista_eos",
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "global_delay_factor": 4,
}
srx2 = {
    "device_type": "juniper_junos",
    "host": "srx2.lasthop.io",
    "username": "pyclass",
    "password": password,
}

device_list = [cisco3,arista1,arista2,srx2]
