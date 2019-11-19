import pyeapi
from getpass import getpass
from my_funcs import myfunc_yaml_output
from pprint import pprint

connection = pyeapi.client.connect(**myfunc_yaml_output("arista4_connect.yml"),password=getpass())
device = pyeapi.client.Node(connection)
output = device.enable("show ip route")

routes = output[0]['result']['vrfs']['default']['routes']
new_list = []
for i in routes.keys():
    new_list.append(i)
for i in range(len(new_list)):
    if routes[new_list[i]]['directlyConnected'] == True:
        print("Connected route is", new_list[i])
    elif routes[new_list[i]]['directlyConnected'] == False:
        print("Static route is", new_list[i])
        if type(routes[new_list[i]]['vias']) == list:
            new_route = routes[new_list[i]]['vias']
            for j in range(len(new_route)):
                print("Next Hop Address for static route is", new_route[j]['nexthopAddr'])

