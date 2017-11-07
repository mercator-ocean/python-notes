
# En partant de la liste suivante :
# `['cheval', 'bijou', 'genou', 'caillou', 'pou']`
# Obtenez la liste suivante :
# `['bijou', 'caillou', 'chou', 'genou', 'hibou', 'joujou', 'pou']`


liste = ['cheval', 'bijou', 'genou', 'caillou', 'pou']
#liste.remove('cheval')
#liste = liste[liste.index('cheval'):]
del liste[liste.index('cheval')]

#liste.append('chou'); liste.append('hibou'); liste.append('joujou')
#liste.extend(['chou', 'hibou', 'joujou'])
#liste = liste + ['chou', 'hibou', 'joujou']
liste += ['chou', 'hibou', 'joujou']

#liste = sorted(liste)
liste.sort()
print(liste)

# Avec une liste par compréhension, générer la liste des pluriels de :
# `['bijou', 'caillou', 'chou']`

print(['%sx' % s for s in ['bijou', 'caillou', 'chou', 'genou']])
