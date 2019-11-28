from lxml import etree
import xmltodict
xml_string = """
<zones-information>
    <zones-security>
        <zones-security-zonename>trust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>1</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>vlan.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>untrust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-screen>untrust-screen</zones-security-screen>
        <zones-security-interfaces-bound>2</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>fe-0/0/0.0</zones-security-interface-name>
            <zones-security-interface-name>pt-1/0/0.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>junos-host</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>0</zones-security-interfaces-bound>
        <zones-security-interfaces>
        </zones-security-interfaces>
    </zones-security>
</zones-information>
"""
my_xml = etree.fromstring(xml_string)
a = etree.tostring(my_xml).decode()
print(a)
print("Question 1c: Root element tag is",my_xml.tag)
print("Question 1c:The number of child elements",len(my_xml))
print("Question 1d: Direct indices - First child element", my_xml[0].tag)
print("Question 1d: getchildren method - First child element",my_xml.getchildren()[0].tag)
####### Creating a variable named trust zone#####
trust_zone = my_xml[0]
for i in range(len(trust_zone)):
    if trust_zone[i].tag == 'zones-security-zonename':
        print("Question 1e: Text of the zones-security-zonename:",trust_zone[i].text)

for child in trust_zone:
    print("Question 1f",child.tag)


