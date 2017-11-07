import re
with open('regexps.ini') as fichier:
    text = fichier.read()

dictionnaire = {}
for line in text.split("\n"):
    match = re.match(r"([a-zA-Z]*)\s*=\s*([^;]*[^\s;])", line)
    if match:
        cle, valeur = match.groups()
        dictionnaire[cle] = valeur

print(dictionnaire)
