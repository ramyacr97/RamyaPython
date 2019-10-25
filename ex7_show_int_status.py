from pprint import pprint
import textfsm

template_file = "ex7_show_int_status.template"
template = open(template_file)

with open("ex7_show_int_status.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()
print()
new_list = []

keys = re_table.header
values = data
new_list = [{k:v for k,v in zip(keys,v)} for v in values] 
print(new_list)



