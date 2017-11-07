#!/home/tde/anaconda3/bin/python3

# TODO: ce corrige ne repart pas du resultat de l'exercice precedent

# ./ajouteadresses.py -s adresses.csv -d adresses.new.csv --prenom Thomas --nom Desvenain --adresse Nantes --age 36

import argparse
import csv
import os.path
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', action='store', dest='source', required=True)
parser.add_argument('-d', '--destination', action='store', dest='destination')
parser.add_argument('--prenom', action='store', dest='prenom', required=True)
parser.add_argument('--nom', action='store', dest='nom', required=True)
parser.add_argument('--adresse', action='store', dest='adresse', default="")
parser.add_argument('--age', action='store', dest='age', required=True)
parsed = parser.parse_args(sys.argv[1:])

# adresses_file = os.path.abspath(os.path.join(__file__, '../adresses.csv'))
adresses_file_path = parsed.source


def get_adresses(filenom):
    file = open(filenom, 'r')
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

new_entry = {'nom': parsed.nom,
             'prenom': parsed.prenom,
             'adresse': parsed.adresse,
             'age': parsed.age,
             }

adresses = get_adresses(filenom=parsed.source)
for line in adresses:
    if line['nom'] == new_entry['nom'] and line['prenom'] == new_entry['prenom']:
        line['adresse'] = new_entry['adresse']
        line['age'] = new_entry['age']
        added = True
        break
else:
    adresses.append(new_entry)

adresses.sort(key=lambda x: "%s-%s" % (x['nom'], x['prenom']))

dest = parsed.destination or os.path.join(os.curdir, parsed.destination)
with open(adresses_file_path, 'r') as src_file:
    dialect = csv.Sniffer().sniff(src_file.read(), delimiters=";")

with open(dest, 'w') as dest_file:
    dest_writer = csv.writer(dest_file, dialect=dialect)

    for line in adresses:
        dest_writer.writerow([line['prenom'],
                              line['nom'],
                              line['age'],
                              line['adresse']])
