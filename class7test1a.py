from __future__ import print_function, unicode_literals
import jinja2
vlan_vars = {
        "vlan_id": "400",
        "vlan_name": "red400",
}
vlan_template = '''
vlan {{vlan_id}}
    name {{vlan_name}}

'''
t = jinja2.Template(vlan_template)
print(t.render(vlan_vars))


