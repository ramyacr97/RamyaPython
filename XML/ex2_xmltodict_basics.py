#!usr/bin/env python
import xmltodict
f = open("show_security_zones.xml")
xmldata = f.read().strip()
my_xml = xmltodict.parse(xmldata)
print(my_xml)
print(type(my_xml))

####### Question 2B #####
xml_security = my_xml['zones-information']['zones-security']
for i,security_zone in enumerate(xml_security,1):
    for key,value in security_zone.items():
        if key == 'zones-security-zonename':
            print("Security zone #",i,":",security_zone[key])




