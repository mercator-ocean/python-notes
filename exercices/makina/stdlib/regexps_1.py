import re
with open('regexps.ini') as fichier:
    text = fichier.read()


for line in text.split("\n"):
    match = re.match(r"([a-zA-Z]*)\s*=\s*([^;]*[^\s;])", line)
    print(match)
    if match:
        print("Ligne conforme: ", line)

