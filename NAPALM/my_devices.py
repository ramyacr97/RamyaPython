from getpass import getpass
password = getpass()
cisco3 = dict(
    hostname= "cisco3.lasthop.io",
    username = "pyclass",
    password = password,
    device_type = 'ios',
    optional_args= {},
)
arista1 = dict(
    hostname = "arista1.lasthop.io",
    username = "pyclass",
    password = password,
    device_type= "eos",
)

nxos1 = dict(
    hostname = "nxos1.lasthop.io",
    username = "pyclass",
    password =  password,
    device_type = "nxos",
    optional_args= {"port": 8443},
)
device_list =[cisco3,arista1]
