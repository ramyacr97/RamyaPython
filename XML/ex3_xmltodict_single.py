#!usr/bin/env python
import xmltodict
def fileopenread(filename):
    f = open(filename)
    xmldata = f.read().strip()
    my_xml = xmltodict.parse(xmldata)
    return my_xml

file1 = fileopenread("show_security_zones.xml")
file2 = fileopenread("show_security_zones_single_trust.xml")

#####Question 3B ####

print(type(file1['zones-information']['zones-security']))
print(type(file2['zones-information']['zones-security']))
#n#### Question 3C ###

def fileopenread_forcelist(filename):
    f = open(filename)
    xmldata1 = f.read().strip()
    my_xml1 = xmltodict.parse(xmldata1, force_list = {'zones-security': True})
    return my_xml1

security_zone1 = fileopenread_forcelist("show_security_zones_single_trust.xml")
print(type(security_zone1['zones-information']['zones-security']))

