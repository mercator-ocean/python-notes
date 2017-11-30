liste_mois = [
    ('janvier', 31),
    ('fevrier', 28),
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

calendrier = []
for nom_mois, nb_jours in liste_mois:
    for numero_jour in range(1, nb_jours + 1):
        calendrier.append({
            'j': numero_jour,
            'm': nom_mois
        })

print(calendrier)
