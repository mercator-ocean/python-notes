#!/home/tde/anaconda3/bin/python3
import argparse
import csv
import os.path
import sqlite3
import sys

# TODO: ce corrige ne repart pas du resultat de l'exercice precedent

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', action='store', dest='source', required=True)
parser.add_argument('-d', '--database', action='store', dest='database')
parsed = parser.parse_args(sys.argv[1:])

# adresses_file = os.path.abspath(os.path.join(__file__, '../adresses.csv'))
adresses_file_path = parsed.source

addresses = []
with open(adresses_file_path, 'r') as adresses_file:
    lines = adresses_file.readlines()
    for line in lines:
        line = line.strip()
        firstname, name, age, address = line.split(";")
        addresses.append({'firstname': firstname,
                         'name': name,
                         'address': address,
                         'age': int(age)})

db_file = parsed.database or os.path.join(os.curdir, 'users.db')
conn = sqlite3.connect(db_file)  # TODO: check if we can use 'with' statement
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS USER (
    FIRSTNAME VARCHAR(200),
    LASTNAME VARCHAR(200),
    AGE INTEGER,
    ADDRESS VARCHAR(200) )
""")

cursor.execute("DELETE FROM USER")
print(addresses)
cursor.executemany("INSERT INTO USER (FIRSTNAME, LASTNAME, AGE, ADDRESS) VALUES (?,?, ?, ?)",
                   [(line['firstname'],
                     line['name'],
                     line['age'],
                     line['address'])
                    for line in addresses])
conn.commit()
conn.close()
