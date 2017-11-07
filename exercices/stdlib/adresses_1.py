f = open('adresses.csv', 'r', encoding='utf-8')
liste = []
for line in f:
    prenom, nom, age, adresse = line.strip().split(';')
    liste.append({'prenom': prenom,
                  'nom': nom,
                  'age': age,
                  'adresse': adresse
                  })

print(liste)
f.close()
