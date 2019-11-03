# !/usr/bin/env python
from pprint import pprint
import yaml
with open("interfaces1.yml") as f:
    output = yaml.load(f)
pprint(output)
