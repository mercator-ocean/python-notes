#!/usr/bin/python3
import os
import shutil


def get_adresses(filename):
    file = open(filename, 'r')
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

if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser("Adresses")
    parser.add_argument('--source', '-s', action="store", dest='source',
                        required=False, help='Nom du fichier source',
                        default='adresses.csv')
    parser.add_argument('--ext', '-e', action="store", dest='extension',
                        required=False, help='Extension du fichier temporaire',
                        default='bak')
    args = parser.parse_args(sys.argv[1:])

    source_file = args.source
    tmp_file = os.path.splitext(args.source)[0] + "." + args.extension

    shutil.copy(source_file, tmp_file)
    print(get_adresses(tmp_file))
    os.remove(tmp_file)
