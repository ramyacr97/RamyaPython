from pprint import pprint
import textfsm

template_file = "ex1_show_int_status.template"
template = open(template_file)

with open("ex1_show_int_status.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()
print(re_table.header)
pprint(data)
print()
