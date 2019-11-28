#!usr/bin/env python
from lxml import etree
f = "show_security_zones.xml"
my_xml = etree.parse(f)
a = etree.tostring(my_xml).decode()
## find returns the first occurence
### print the first element of zones-security using findall
print('-'*30)
print(my_xml.find("zones-security").tag)
xml_data = my_xml.find("zones-security")
print("Printing the child elements of the zones-security")
for child in xml_data:
    print(child.tag)

#### Question 4B#####
zonename = my_xml.find(".//zones-security-zonename").text
print(" The text part of zonename is ",zonename)
#### Question 4c ####
xml_data1 = my_xml.findall("zones-security")
print(xml_data1)
for i in range(len(xml_data1)):
    zone = my_xml.findall(".//zones-security-zonename")[i]
    print("The",zone.tag,"text part is",zone.text)
