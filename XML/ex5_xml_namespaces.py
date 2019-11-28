from lxml import etree
x = etree.parse("show_version.xml")
print(x)
my_xml = x.getroot()
print(my_xml.tag)
ns_map = {}
ns_map['nf'] = "urn:ietf:params:xml:ns:netconf:base:1.0"
ns_map[None] = "http://www.cisco.com/nxos:1.0:sysmgrcli"
print(my_xml.find("nf:data",namespaces=ns_map))
print(my_xml.find("nf:data/show",namespaces=ns_map))
print("The serial number is ",my_xml.find(".//{*}proc_board_id").text)
