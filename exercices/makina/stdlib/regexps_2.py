import re
with open('regexps.ini') as fichier:
    text = fichier.read()

for line in text.split("\n"):
    match = re.match(r"([a-zA-Z]*)\s*=\s*([^;]*[^\s;]).*", line)
    if match:
        #  groups renvoit les valeurs pour les groupes de l'expression régulière
        print("Clé, valeur", match.groups())
