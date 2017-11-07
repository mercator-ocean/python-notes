import os
import yaml

filename = os.path.join(os.path.dirname(__file__), "example.yml")

with open(filename) as fp:
    data = yaml.load(fp)
    print(data["technologies"][1])  # Django
