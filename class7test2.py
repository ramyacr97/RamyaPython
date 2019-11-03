#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import jinja2
ospf_interfaces = ["Vlan1", "Vlan2"]
ospf_routes = ["10.10.10.0/24", "10.10.20.0/24", "10.10.30.0/24"]
ospf_vars = {
        "ospf_priority_enable": True,
        "ospf_priority": 100,
        "ospf_process_id": 10,
        "interface_list": ospf_interfaces,
        "ospf_routes": ospf_routes,
}
template_file = 'ospf_temp.j2'
with open(template_file) as f:
    ospf_template = f.read()
template = jinja2.Template(ospf_template)
print(template.render(ospf_vars))
