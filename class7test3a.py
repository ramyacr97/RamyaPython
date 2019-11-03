import yaml
with open("interfaces.yml") as f:
    output = yaml.load(f)
print(output)
