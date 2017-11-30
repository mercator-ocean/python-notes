is_bissextile = True

liste_mois = [
    ('janvier', 31),
    ('fevrier', 29 if is_bissextile else 28),
    ('mars', 31),
    ('avril', 30),
    ('mai', 31),
    ('juin', 30),
    ('juillet', 31),
    ('aout', 31),
    ('septembre', 30),
    ('octobre', 31),
    ('novembre', 30),
    ('decembre', 31)
]

liste_jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

indice_jour_annee = 0
calendrier = []
for nom_mois, nb_jours in liste_mois:
    for numero_jour in range(1, nb_jours + 1):
        calendrier.append({
            'j': numero_jour,
            'm': nom_mois,
            'js': liste_jours[indice_jour_annee % 7]
        })
        indice_jour_annee += 1

print(calendrier)

for num_jour, infos_jour in enumerate(calendrier, 1):
    if infos_jour['j'] == 11 and infos_jour['m'] == 'novembre':
        print("Le 11 novembre est un %s" % infos_jour['js'])
        print("C'est le %s eme jour de l'année" % num_jour)
        break
