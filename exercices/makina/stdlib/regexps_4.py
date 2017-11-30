import re
with open('regexps.ini') as fichier:
    text = fichier.read()

groups = re.findall(r"([a-zA-Z]*)\s*=\s*([^;\n]*[^ ;\n]).*\n", text)
dictionnaire = dict(groups)
print(dictionnaire)
