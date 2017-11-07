def get_adresses(filename):
    file = open(filename, 'r', encoding='utf-8')
    liste = []
    for line in file:
        prenom, nom, age, adresse = line.strip().split(';')
        liste.append({'prenom': prenom,
                      'nom': nom,
                      'age': age,
                      'adresse': adresse
                      })

    file.close()
    return liste

print(get_adresses('adresses.csv'))
