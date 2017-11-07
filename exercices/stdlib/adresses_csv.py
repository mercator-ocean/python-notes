import csv
import os

filename = os.path.join(os.path.dirname(__file__), 'adresses.csv')
fieldnames = ("prenom", "nom", "age", "adresse")

with open(filename) as fp:
    reader = csv.DictReader(fp, fieldnames=fieldnames, delimiter=";")
    for row in reader:
        print("{prenom} {nom}, {age} ans".format_map(row))
