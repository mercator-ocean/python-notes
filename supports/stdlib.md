# Plan de formation

- Présentation & Historique
- Syntaxe et bases du langage
- Approche Orientée Objet
- Programmation Orientée Objet en Python
- **Librairies standard**
- Outils de qualité et tests

--------------------------------------------------------------------------------

# Librairies standard

Une des grandes forces de Python est qu'il est livré de base habillé
 et chaussé, prêt à l'emploi, avec un très large éventail de
 librairies couvrant de nombreux domaines de l'informatique :
 
- Gestion de fichiers
- Compression de données
- Chiffrement
- Mathématiques
- Bases de données
- IHM
- Internet et les réseaux
- Multimédia
- ...


--------------------------------------------------------------------------------

## Librairies standard

La liste exhaustive de ces librairies est fournie à cette
 URL :<br />
<https://docs.python.org/3/library/index.html> 

Nous aborderons dans ce chapitre les librairies suivantes :

- **Gestion de fichiers**
- Gestion des arguments en ligne de commande
- Les expressions régulières
- L'exécution de commandes systèmes
- L'exécution de requêtes http 
- Les bases de données relationnelles


--------------------------------------------------------------------------------

## Gestion de fichiers

### Ouverture et fermeture de fichiers

- La fonction `open` permet d'ouvrir un fichier en lecture ou
 écriture.
- Elle accepte plusieurs arguments :
    - le premier est le chemin d'accès vers le fichier (absolu ou relatif)
    - le second est le mode d'accès 
        - `w` pour l'écriture en mode création ou l'écrasement
        - `a` pour l'écriture en mode ajout en fin de fichier
        - `r` pour la lecture
        - Il est possible de mixer les modes<br />
          <https://docs.python.org/3/library/functions.html#open>
- Elle retourne un objet de type `file object` 
- Une fois vos opérations terminées il convient de fermer le fichier
 avec la méthode `close`


--------------------------------------------------------------------------------

## Gestion de fichiers

### Ecriture de fichier

- Il existe 2 méthodes pour écrire des données dans un fichier :
    - `write()`, pour écrire une chaîne de caractères
    - `writelines()`, pour écrire une liste de chaînes de caractères

### Lecture de fichiers

Les objets de type `file` possèdent 3 méthodes pour lire des données :

- `read()`, pour lire tout ou partie du fichier dans un buffer
- `readline()`, pour lire une ligne (ou boucler sur l’objet ficher)
- `readlines()`, pour lire toutes les lignes du fichier dans une liste

-------------------------------------------------------------------------------

## Gestion de fichiers

### Déplacement dans un fichier

La méthode `seek()` permet de se déplacer sur un caractère donné par son indice (identique à ceux des listes). `seek(0)` renvoit au début du fichier.

--------------------------------------------------------------------------------

## Gestion de fichiers


    !python
    # Création du fichier
    f = open("mon_fichier.txt", "w")
    f.write("ligne1\nligne2\n")
    f.writelines(["ligne3\n", 'ligne4\n'])
    f.close()

----------------------------------------------------------------------

## Gestion de fichiers
    
    !python
    # Lecture du fichier
    f = open("mon_fichier.txt", "r")
    # Lit tout si pas d'argument, sinon le nombre de caractères indiqué
    data = f.read() 
    print("***Data***", data)
    
    # Le curseur
    f.seek(0) # Retour au début
    lines = f.readlines()
    print("***Lines*** ", lines)
    lines = f.readlines()
    print("On avait déjà tout lu ! La preuve :", lines)
    f.close()

<!-- -->
    
    ***Data*** ligne1
    ligne2
    ligne3
    ligne4
    
    ***Lines***  ['ligne1\n', 'ligne2\n', 'ligne3\n', 'ligne4\n']
    On avait déjà tout lu ! La preuve : []

--------------------------------------------------------------------

## Gestion de fichiers


    !python
    f = open("mon_fichier.txt", "r")
    # Lecture ligne par ligne, readline() retourne '' si plus de données.
    line = f.readline() #  Une ligne vide contient '\n'
    for line in f: #  On boucle sur les lignes suivantes
        print("ligne courante :", line.strip())
        
    f.close()

<!-- -->

    ***ligne courante: ligne2
    ***ligne courante: ligne3
    ***ligne courante: ligne4


--------------------------------------------------------------------

## Gestion de fichiers

### Utilisation du context manager `with`

    !python
    # Création du fichier
    with open("mon_fichier.txt", "w") as f:
        f.write("ligne1\nligne2\n")
        f.writelines(["ligne3\n", 'ligne4\n'])
    
    # Lecture
    with open("mon_fichier.txt", "r+") as f:
        data = f.read() 
        print("Data :", data)


--------------------------------------------------------------------------------

## Gestion de fichiers

### Exercice

Créez un programme Python qui lise le fichier CSV d'utilisateurs qui vous est fourni.

- Il se compose de 4 champs séparés par des points virgules
    - Prénom
    - Nom
    - Age
    - Adresse
- Lisez les enregistrements du fichier et stockez chaque ligne dans un dictionnaire que vous stockerez lui-même dans une liste.
- Les clefs du dictionnaire seront les noms des 4 champs ci-dessus

Indication : la classe `string` possède des fonctions permettant de décomposer une chaîne en plusieurs morceaux, de retirer des caractères...


--------------------------------------------------------------------------------

## Gestion de fichiers

Python possède plusieurs librairies pour manipuler des fichiers :

- Le module `os` permet de manipuler les fichiers et leurs
 attributs : droits d'accès, dates de modifications…<br />
<https://docs.python.org/3/library/os.html>
- Le sous module `os.path` permet de manipuler les noms de
 fichiers et de dossiers, tester leur existence…:<br />
<https://docs.python.org/3/library/os.path.html> 
- Le module `shutil` permet de copier/déplacer/supprimer des
 fichiers et dossiers:<br />
<https://docs.python.org/3/library/shutil.html> 
- Le module `tempfile` permet de trouver un chemin et nom pour un fichier temporaire<br />
<https://docs.python.org/3/library/tempfile.html> 


--------------------------------------------------------------------------------

## Gestion de fichiers

### Exercice

- Modifiez le programme précédent pour le transformer en une fonction qui prend en paramètre d'entrée le nom du fichier des utilisateurs
- Lisez une copie du fichier source faite avant, dont l'extension sera `.bak`  et qui sera située dans le même dossier (`/tmp/monfichier.txt` => `/tmp/monfichier.bak`)
- Supprimez le fichier de sauvegarde `.bak` en fin de traitement


--------------------------------------------------------------------------------

## Gestion de fichiers

Pour aller plus loin avec les fichiers :

- Tout sur la fonction `open`:<br />
<https://docs.python.org/3/library/functions.html#open>
- Les objets fichiers :<br />
<https://docs.python.org/3/glossary.html#term-file-object> 
- Les flux de données :<br />
<https://docs.python.org/3/library/io.html>  
- La compression de fichiers et l'archivage :<br />
<https://docs.python.org/3/library/archiving.html> 
- Tous les autres modules sur la gestion de fichiers :<br />
<https://docs.python.org/3/library/filesys.html> 
- Les fichiers CSV :<br />
<https://docs.python.org/3/library/csv.html> 


--------------------------------------------------------------------------------

## CSV dans la vraie vie

Lire des fichiers CSV est plus difficile qu'il n'y parait : que se passe-t-il si une valeur contient un point-virgule ?

Python est livré avec un module `csv` robuste que vous devrez utiliser en
production.

    !python
    import csv
    import os

    filename = os.path.join(os.path.dirname(__file__), 'adresses.csv')
    fieldnames = ("prenom", "nom", "age", "adresse")

    with open(filename) as fp:
        reader = csv.DictReader(fp, fieldnames=fieldnames, delimiter=";")
        for row in reader:
            print("{prenom} {nom}, {age} ans".format_map(row))


--------------------------------------------------------------------------------

## JSON

La bibliothèque standard Python fournit un module pour manipuler du JSON.

    !pycon
    >>> import json

### Lecture

    !pycon
    >>> string = '{"name": "White Rabbit", "age": 3}'
    >>> json.loads(string)
    {'name': 'White Rabbit', 'age': 3}

### Écriture

    !pycon
    >>> data = {"name": "Alice", "age": 14, "salary": None}
    >>> json.dumps(data)
    '{"name": "Alice", "age": 14, "salary": null}'

### Exercice

Enregistrer les données du fichier adresses.csv dans un nouveau fichier au format JSON.

--------------------------------------------------------------------------------

## Librairie Standard

- Gestion de fichiers
- **Gestion des arguments en ligne de commande**
- Les expressions régulières
- L'exécution de commandes systèmes
- L’exécution de requêtes http 
- Les bases de données relationnelles

--------------------------------------------------------------------------------

## Ligne de commande

Il est très fréquent d'utiliser un programme Python comme utilitaire en ligne de commandes.

Dans ce cas il est possible de lui passer des arguments lors de son lancement depuis la ligne de commande afin de rendre paramétrable son exécution

`$ ./database_query.py -u user --database MYDB --host 127.0.0.1  --password 'secret' --no-commit`

--------------------------------------------------------------------------------

## Ligne de commande

Python possède pour cela 5 modules :

- `sys`, le module de base qui permet juste de récupérer les
 arguments sous forme de données
 brutes<br />
 <https://docs.python.org/2/library/sys.html> 
- `getopt`, qui calque son équivalent `bash`<br />
  <https://docs.python.org/3.1/library/getopt.html>
- `optparse` qui est plus convivial que le
  précédent <br />
  <https://docs.python.org/3/library/optparse.html> 
- `argparse`, que nous étudierons<br />
  <https://docs.python.org/3/library/argparse.html> 
- `click`, une bibliothèque supplémentaire, qui fonctionne  avec des décorateurs<br />
 <http://click.pocoo.org> 


--------------------------------------------------------------------------------

## Ligne de commande

Le module `sys` possède une variable nommée `argv` qui
 est une liste contenant les paramètres passés au programme Python.

Le premier élément de la liste est le nom du script.

    !python
    import sys
    
    print("Paramètres reçus: %s" % sys.argv)
    input_file, output_file = sys.argv[1:3]
    VERBOSE = "-v" in sys.argv

Cela peut convenir quand on veut passer un ou deux arguments positionnels.

Mais cela devient très compliqué si on veut gérer des paramètres clé / valeur, des paramètres obligatoires, etc.


--------------------------------------------------------------------------------

## Ligne de commande

Le module `argparse` facilite grandement la gestion des
 paramètres.

- Il permet de générer automatiquement une aide en ligne de commande
- Il accepte les options longues : `--file`, et courtes : `-f`
- Il réalise les conversions de types de données
- Il peut gérer de nombreuses options comme récupérer plusieurs
 valeurs passées avec un même nom de paramètre dans un tableau
`-f toto -f titi -f tutu` -> ['toto', 'titi', 'tutu']
- Il gère les erreurs
- Il permet de définir des contraintes, des valeurs par défaut...


--------------------------------------------------------------------------------

## Ligne de commande

Il s'utilise comme suit :

- Vous instanciez un parser d'arguments avec la classe  `ArgumentParser`
- Puis vous déclarez les arguments que vous souhaitez gérer avec la  méthode `add_argument`
- Enfin, vous récupérez les paramètres de votre script en appelant la méthode `parse_args`

<!-- -->

    !python
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()
    print(args.foo)

----------------------------------------------------------------------------------------

## Ligne de commande

La méthode `add_argument` représentera le coeur de votre travail.
 
Ses paramètres sont les suivants :

- En premier lieu, les libellés acceptés pour votre paramètre: '-f', '--file'
- `action` : indique ce que vous souhaitez faire avec le
 paramètre. Par défaut elle vaut `store`, ce qui le sauvegarde
 dans une variable. Il existe d'autres options comme `store_true` qui sauvegardera la valeur True s'il est présent
- `default` : permet de définir une valeur par défaut si le
 paramètre n'est pas présent
- `type` : indique le type du paramètre, par défaut `string`
- `required` : True indiquera que le paramètre est obligatoire
- `help` : permet de fournir un message d'aide 
- `dest` : indique le nom de la variable qui contiendra la valeur du paramètre


--------------------------------------------------------------------------------

## Ligne de commande
    
    !python
    import argparse
    parser = argparse.ArgumentParser("Mon programme à moi")
    parser.add_argument('--file', '-f', action="store", dest='fichier',
                    required=True, help='Nom du fichier source')
    parser.add_argument('--binary', '-b', action="store_true", 
                    default=False, dest='binaire', required=False, 
                    help='Indique si le fichier est binaire')
    args = parser.parse_args()
    print(args)

<!-- -->
    
    $ sys_params.py --help
    usage: Mon programme à moi [-h] --file FICHIER [--binary]
    optional arguments:
      -h, --help            show this help message and exit
      --binary, -b          Indique si le fichier est binaire


--------------------------------------------------------------------------------

## Ligne de commande

### Exercice 1

Améliorer le programme lisant le fichier CSV des utilisateurs pour qu'il soit paramétrable.
Il acceptera les paramètres suivants :

- `-s` ou `--source` : le chemin absolu vers le fichier
 source
- `-e` ou `--ext` : l'extension du fichier temporaire

### Exercice 2

L'améliorer pour qu'il permette d'ajouter un nouvel utilisateur (d'abord dans le dictionnaire final et, quand vous y serez parvenu, dans le fichier cible).

- `--name` et `--firstname` : le nom et le prénom, obligatoires
- `--address` : son adresse, facultative
- `--age` : l'age, obligatoire
- `-d` ou `--dest` : le fichier cible (si indéfini,
 'adresses.new.csv' dans le dossier d'où l'on lance le script)

### Exercice bonus

Si l'utilisateur passé en argument existe déjà (il a le même nom et prénom), il est modifié.

--------------------------------------------------------------------------------

## Librairie Standard

- Gestion de fichiers
- Gestion des arguments en ligne de commande
- **Les expressions régulières**
- L'exécution de commandes systèmes
- L’exécution de requêtes http 
- Les bases de données relationnelles

--------------------------------------------------------------------------------

## Les expressions régulières

Le terme **expression régulière**, ou **expression rationnelle**, désigne une syntaxe
permettant de vérifier que des chaînes de caractères répondent à
des motifs particuliers.
 
 <https://fr.wikipedia.org/wiki/Expression_rationnelle> 

Elles servent en général à :

- Valider la syntaxe des chaînes de caractères, comme un email, une
 URL, un numéro de téléphone, etc.
- Rechercher une suite de caractères dans une chaîne
- Effectuer des opérations de remplacement ou d'extraction de chaînes
 avancées.
 
On fait souvent ce genre de choses avec Perl. Mais Python reste très efficace.



-----------------------------------------------------------------------------

### Les expressions régulières

Les expressions régulières ne sont pas très compliquées, mais leur
 syntaxe très concise et quelque peu obscure pour les novices les
 rendent souvent effrayantes.
 
*Il n'en est rien !*

Quand vous utilisez les expressions régulières vous procédez en 3
 étapes :
 
- vous définissez ce que l'on appelle un **motif**, c'est à dire la
 syntaxe que vous voulez rechercher/valider dans une chaîne de
 caractères,
- vous utilisez des fonctions pour savoir si cette chaîne respecte
 ce motif,
- si nécessaire, vous récupérez les éléments qui sont conformes à ce motif.


--------------------------------------------------------------------------------

### Les expressions régulières

L'étape la plus difficile est de définir le motif que vous
 recherchez.
 
Pour cette initiation nous vous proposons de lire un fichier de
 configuration de type `.ini`
 
    [Display]
    height=600 ; hauteur de l'écran
    width=800
    ; un commentaire toto = titi
    [User]
    name = Toto
    age = 20
    address=20, rue des olivettes
 
 L'exercice consistera à extraire de ce fichier de configuration les
 couples `<clef> = <valeur>` en ignorant ceux qui sont en commentaires,
 indiqués par un "` ;`" dans la ligne.


--------------------------------------------------------------------------------

### Les expressions régulières

Dans notre exemple nous voulons récupérer :

- "Height" et "600"
- "address" et "20, rue des olivettes"

MAIS PAS :

- "; hauteur de l'écran"
- "un commentaire toto = titi"

Pour cela commençons par définir ce qu'est une clef et sa valeur... en
langage naturel !


--------------------------------------------------------------------------------

### Les expressions régulières

- clef :<br />
une lettre minuscule/majuscule suivie de
0 ou plusieurs lettres (min/maj), chiffres ou tiret bas `_`
- valeur :<br />
toute suite de caractères sauf un point virgule `;`
 
Le motif que nous recherchons sera donc :

    clef + espaces éventuels + caractère "`=`" + espaces éventuels + valeur

Il ne reste plus qu'à le traduire dans la langue des expressions régulières.

La syntaxe supportée par Python est définie dans le module `re`

<https://docs.python.org/3/library/re.html> 


--------------------------------------------------------------------------------

## Les expressions régulières

Dans le monde des expressions régulières, chaque caractère
 correspond à lui-même.

Donc si vous recherchez le terme `user` dans une chaîne son
 motif sera `user`.
 
Mais, bien sûr, il y a des caractères spéciaux qui permettent de
 définir des motifs répétitifs et plus complexes que de simples mots.


--------------------------------------------------------------------------------

## Les expressions régulières

### Motif "`.`"

Le caractère **point** représente n'importe quel caractère.
Si votre motif est `A.C`, alors :

- **ABC** sera strictement conforme au motif
- 'La chaîne de télé **ABC**D est en panne' contiendra le motif
- 'TOTO AC' ne contiendra pas votre motif 


--------------------------------------------------------------------------------

## Les expressions régulières

### Motif "`*`"

Le caractère **étoile** signifie que le caractère ou groupe
 précédant ce caractère peut être présent 0 ou plusieurs fois.

Si votre motif est `A*C`, alors :

- '**C**', '**AC**', '**AAAAC**' seront strictement conformes au motif
- 'La **c**haîne de télé AB**C**D a du t**ac**t' contiendra 3 fois le motif
- 'TOTO AB' ne contiendra pas votre motif 


--------------------------------------------------------------------------------

## Les expressions régulières

### Motif "`+`"

Le caractère «plus» signifie que le caractère ou groupe
 précédant ce caractère peut être présent 1 ou plusieurs fois.

Si votre motif est `A+C`, alors :

- '**AC**', '**AAC**', '**AAAAC**' seront strictement conformes au motif
- 'La chaîne de télé ABCD a du t**ac**t' contiendra 1 fois le motif
- 'TOTO AB' ne contiendra pas votre motif 


--------------------------------------------------------------------------------

## Les expressions régulières

### Motif "`?`"

Le caractère «point d'interrogation» signifie que le caractère
 ou groupe précédant ce caractère peut être présent 0 ou 1 fois.

Si votre motif est `A?C`, alors :

- '**C**', '**AC**' seront strictement conformes au motif
- 'La **c**haîne de télé **ABC**D a du t**ac**t' contiendra 3 fois le motif
- 'TOTO AB' ne contiendra pas votre motif 


--------------------------------------------------------------------------------

## Les expressions régulières

### Motif "`[]`"

Les crochets indiquent une liste de caractères autorisés.

- `[abcdef]` : indique que seules les 6 premières lettres minuscules de
 l'alphabet sont autorisées
- `[abxzABXZ]` : indique que seuls les caractères `a`, `b`,
 `x` et `z` sont autorisés, en minuscules comme en
 majuscules
- `[a-z]` : indique que tous les caractères compris entre le code ASCII
 de la lettre `a` et le code ASCII de la lettre `z` sont
 autorisés
- `[0-9a-z]` : autorise donc les chiffres et lettres minuscules

Si votre motif est `[abcdeu;,]+`, alors :

- '**;cad**' est strictement conforme
- '**u**n **beau** **cad**eau' contient 3 fois le motif


--------------------------------------------------------------------------------

## Les expressions régulières

### Motif "`[^]`"

Les crochets dont le premier caractère est `^` indiquent que
 tous les autres caractères de cet intervalle sont refusés.
 
 Cela équivaut à dire : "tout sauf"
 
- `[^abcdef]` : indique que les 6 premières lettres minuscules de l'alphabet sont refusées
- `[^a-z]` : indique que tous les caractères compris entre le code ASCII
 de la lettre `a` et le code ASCII de la lettre `z` sont
 refusés
- `[^0-9a-z]` : refuse donc les chiffres et lettres minuscules

Si votre motif est `[^abcdeu;,]+`, alors :

- ';cad' est strictement non conforme
- 'u**n** beau cadeau' contient 2 fois le motif (les espaces sont acceptés)


--------------------------------------------------------------------------------

## Les expressions régulières

### Motif "`()`"

Les parenthèses permettent de définir/encadrer un groupe de
 caractères qui vous intéresse dans votre motif.

Vous pouvez bien sûr définir plusieurs groupes dans un motif.

Cela vous permettra par la suite de récupérer facilement ces groupes
 de caractères que vous aurez ainsi marqués.

Si votre motif est : '`REF-([0-9]+) CODE_PAYS:([A-Z][A-Z])`'

Vous pourrez facilement récupérer les valeurs '99' et 'FR' dans la chaîne '`REF-99 CODE_PAYS : FR`'


--------------------------------------------------------------------------------

## Les expressions régulières

### Motif "`\`"

 Le caractère `\` permet de protéger les caractères spéciaux :

- `\\` : représente le caractère `\`
- `\.` : représente le caractère point `.`
- `\+` : représente le caractère `+`
- `\s` : représente tous les types d'espaces, notamment `\n`,
 `\r`, `\t` (saut de ligne, retour chariot, tabulation)

Nous sommes maintenant en mesure de définir le motif de notre couple `clef = valeur`

--------------------------------------------------------------------------------

## Les expressions régulières

- clef : une lettre minuscule/majuscule suivie de
0 ou plusieurs lettres (min/maj), chiffres ou tiret bas "`_`"
- valeur : 
Toute suite de caractères avant un point virgule `;`
 
Le motif que nous recherchons sera donc :

- clef : `[a-zA-Z][a-zA-Z0-9_]*`
- espaces éventuels : `\s*`
- caractère `=` : `=`
- pas de point-virgule : `[^;]*`

Soit au final : `[a-zA-Z][a-zA-Z0-9_]*\s*=\s*[^;]*`


--------------------------------------------------------------------------------

## Les expressions régulières

Le module `re` propose des fonctions qui vous permettent de
 vérifier si une chaîne correspond à un motif :

- `search`, cette fonction accepte 2 paramètres, un motif et une  chaine. Elle retournera un objet de type `match` évalué à `True` si le motif est trouvé dans la chaîne.
- Les objets de types `match` retournés par `search`
 possèdent des méthodes `group` et `groups` permettant de
 récupérer les valeurs entourées de parenthèses dans votre motif.
- `compile`, cette fonction retourne un motif compilé, qui sera plus rapide à rechercher si vous avez de nombreuses analyses à faire

<!-- -->
    !pycon
    >>> import re
    >>> m = re.search('.*(def)', 'abcdef')
    >>> m.group(1)
    'def'


--------------------------------------------------------------------------------

## Les expressions régulières

### Exercice

Analysez les lignes du fichier de configuration présenté
 précédemment et affichez :
 
- Les lignes conformes au motif
- La liste des clefs et valeurs de chaque ligne conforme
- Renseignez un dictionnaire avec les clés / valeurs


--------------------------------------------------------------------------------

## Librairie Standard

- Gestion de fichiers
- Gestion des arguments en ligne de commande
- Les expressions régulières
- **L'exécution de commandes systèmes**
- L’exécution de requêtes http 
- Les bases de données relationnelles

------------------------------------------

## Exécuter des commandes système

Python dispose de bibliothèques permettant de lancer d'autres programmes disponibles sur le système.

- On utilise maintenant le module **subprocess**
  - `os.system`, `os.spawn` (et en python2 `os.popen`, `os.popen2`) sont obsolètes
- Des méthodes permettent d'exécuter facilement des commandes et de
 récupérer la sortie standard ou le code de retour
    - `subprocess.check_output(['df'])` renvoit la sortie standard
    - `subprocess.call(['ping', 'azertyazerty.com'])` renvoit  le code de retour de l'appel
- Pour des besoins plus complexes, on utilise la classe `Popen`

L'exemple suivant fait passer le résultat d'un ps aux dans un grep :

<!-- -->

    !python
    p1 = subprocess.Popen(["ps","aux"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(
            ["grep", "java"], 
            stdin=p1.stdout,stdout=subprocess.PIPE)
    p1.stdout.close()
    output, error = p2.communicate()
    print(output)

Si vous utilisez Pycharm, son processus devrait apparaître dans la sortie.

--------------------------------------------------------------------------------

## Librairie Standard

- Gestion de fichiers
- Gestion des arguments en ligne de commande
- Les expressions régulières
- L'exécution de commandes systèmes
- **L’exécution de requêtes http** 
- Les bases de données relationnelles

--------------------------------------------------------------------------------

## Requêtes http avec requests

`requests` est la bibliothèque moderne pour exécuter des requêtes http, avec une api très pratique pour le support REST/json.

C'est une bibliothèque externe mais incluse dans de nombreuses distributions.

    !pycon
    >>> import requests
    >>> response = requests.get("https://www.google.com")  # endpoint html
    >>> response.text
    ... # le code html de la page
    >>> response.status_code
    200
    >>> response = requests.get("http://api.fixer.io/latest", {'base': 'USD'})  # endpoint json
    >>> response.json()['rates']['EUR']
    0.91617

<!-- -->

--------------------------------------------------------------------------------

## Requêtes http avec requests

Vous pouvez réutiliser une connection TCP pour plusieurs requêtes en utilisant l'objet Session.

Il permet également de conserver certains paramètres, comme les cookies par exemple.
    
    !python
    s = requests.Session()
    
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('http://httpbin.org/cookies')
    
    print(r.text)
    # '{"cookies": {"sessioncookie": "123456789"}}'

<!-- -->

--------------------------------------------------------------------------------

## Requêtes http

`urllib.request` est la bibliothèque standard pour exécuter des requêtes http.
 
 <https://docs.python.org/3/library/urllib.html>

    !pycon
    >>> response = urllib.request.urlopen("http://www.google.fr")
    >>> response.read()
    
`urllib.parse` permet de composer, encoder, échapper des urls (et inversement)

<https://docs.python.org/3/library/urllib.parse.html>

    !pycon
    >>> urllib.parse.urlparse("http://www.google.fr/images?q=lions")
    ParseResult(scheme='http', netloc='www.google.fr', 
        path='/images', params='', query='q=lions', fragment='')

<!-- -->

    !pycon
    >>> urllib.parse.parse_qs("search=news&limit=100")
    {'limit': ['100'], 'search': ['news']}

<!-- -->

    !pycon
    >>> urllib.parse.urlencode({'q': 'éléphants'})
    'q=%C3%A9l%C3%A9phants'


--------------------------------------------------------------------------------

## Requêtes http

ATTENTION : il y a d'importantes différences dans l'organisation
 de ces modules dans Python2

- `urllib` de Python3 s'appelle `urllib2` dans Python2 (la bibliothèque `urllib` de Python2 est
 dépréciée)
- `urllib.parse` s'appelle `urlparse`


--------------------------------------------------------------------------------

## Requêtes http

### Exercice :

- Vous partez de cette chaîne de caractères : `https://twitter.com/search?q=clinton`
- Uniquement en la décomposant avec la lib `urllib.parse` (sans utiliser
 les fonctions de string!), remplacez le critère de recherche
 `clinton` par le hashtag `#trump`
- Attention, `#` est un caractère spécial !
- Pour tester, exécutez la requête avec requests, et enregistrez le
 contenu dans un fichier 'test-twitter.html'.
 
*N'hésitez pas à utiliser internet pour vous aider*

--------------------------------------------------------------------------------

## Librairie Standard

- Gestion de fichiers
- Gestion des arguments en ligne de commande
- Les expressions régulières
- L'exécution de commandes systèmes
- L’exécution de requêtes http
- **Les bases de données relationnelles**

--------------------------------------------------------------------------------

## Bases de données relationnelles

Python a standardisé une interface de programmation (API) pour
 accéder aux bases de données relationnelles.

Elle se nomme la **DBAPI**: *DataBase Application Programming Interface*

Elle est officialisée par la PEP249 :

<https://www.python.org/dev/peps/pep-0249/> 

Les fournisseurs de bases de données sont invités à s'y conformer
 afin d'offrir une interface identique quelle que soit la base de
 données utilisée. 

L'intérêt est énorme : vous pouvez changer de base sans presque rien
 changer à votre programme.


--------------------------------------------------------------------------------

## Bases de données relationnelles


Cette API se compose de 2 classes principales : `Connection` et
 `Cursor`

- La classe `Connection` permet d'ouvrir une connexion sur une
 base, d'enregistrer ou d'annuler des modifications
- La classe `Cursor` permet d'exécuter des requêtes sur la base

En plus de cette API, qui n'est autre qu'un standard, Python fournit
 une base de données clef en main `SQLite` avec un module prêt à
 l'emploi.

`SQLite` est une base de données légère foù chaque base est un simple fichier. 


--------------------------------------------------------------------------------

## Bases de données relationnelles

La classe `Connection`
 
- Avant d'exécuter des requêtes sur une base vous devez créer une
 instance de la classe `Connection`
- La fonction `connect` réalise cette tâche. Les paramètres qu'elle accepte sont dépendants de l'éditeur.
Généralement tous respectent les préconisations de la PEP249, à savoir 'user',
 'password', 'host', 'database' et 'port'
 
Dans le cas de SQLite, seul le nom du fichier stockant la base est requis

    !python
    import sqlite3
    conn = sqlite3.connect('example.db')


--------------------------------------------------------------------------------

## Bases de données relationnelles

La classe `Connection` propose 4 fonctions :

- `commit`, pour enregistrer les modifications réalisées
- `rollback`, pour annuler les modifications réalisées
- `close`, pour fermer la connexion
- `cursor`, pour créer un curseur permettant d'exécuter des
 requêtes

<!-- -->

    !python
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    conn.commit()
    conn.close()


--------------------------------------------------------------------------------

## Bases de données relationnelles

La classe `Cursor` permet d'exécuter des requêtes SQL.

Elle propose plusieurs fonctions :

- `execute`, pour exécuter une instruction SQL quelconque,
- `executemany`, pour exécuter plusieurs fois la même instruction
 sur une liste d'enregistrements,
- `fetchone`, pour lire le prochain enregistrement issu du
 résultat de la fonction `execute`,
- `fetchall`, pour lire tous les enregistrements issus de la
 fonction `execute`,
- `callproc`, pour appeler une procédure stockée 
(en PL/SQL par exemple),
- `close`, pour fermer le curseur.


--------------------------------------------------------------------------------

## Bases de données relationnelles

### Protection contre les injections SQL

- La fonction `execute` accepte en premier paramètre la requête
 SQL à utiliser.
- Elle peut être suivie d'une liste de paramètres à insérer dans
 cette requête.
 
**Ne formatez jamais vous-mêmes votre requête SQL !**

Prenons l'instruction suivante : 
    
    !python
    c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

Si un petit malin fournit "`' ; delete from stocks where 1=1 or ''='`"  dans la variable `symbol` votre requête deviendra :
    
    !sql
    SELECT * FROM stocks WHERE symbol = '' ; delete from stocks where 1=1 or '' = ''

Et vous aurez très certainement des problèmes...


--------------------------------------------------------------------------------

## Bases de données relationnelles

### Protection contre les injections SQL

Pour éviter l'injection SQL, passez vos paramètres en second
 argument dans un tuple, comme ceci :
    
    !python
    data = ('RHAT',)
    c.execute('SELECT * FROM stocks WHERE symbol=?', data)
    
Selon le fournisseur de votre base de données, d'autres caractères
 sont utilisables à la place du `?` pour indiquer l'emplacement de
 vos paramètres :

- `%s`
- `:1,:2,:3`, …
- `:name`

<https://www.python.org/dev/peps/pep-0249/#paramstyle> 


--------------------------------------------------------------------------------

## Bases de données relationnelles

### Exercice

En partant du script modifiant le fichier CSV des utilisateurs.

Ecrivez un programme qui :

- Accepte les paramètres 
    - `--database` indiquant le nom du fichier de votre base de données sqlite
    - `--source` indiquant le fichier csv à importer
- Vide la table `user`
- Ajoute les utilisateurs du fichier dans la table
- Les requêtes SQL dont vous aurez besoin sont indiquées ci-après


--------------------------------------------------------------------------------

## Bases de données relationnelles

### Exercice : indications

#### Création de la table `user`
    
    !sql
    CREATE TABLE USER (
      FIRSTNAME VARCHAR(200),
      LASTNAME VARCHAR(200),
      AGE INTEGER,
      ADDRESS VARCHAR(200)
    )

#### Suppression d'enregistrements dans la table `user`
    
    !sql
    DELETE FROM USER

#### Ajout d'un enregistrement

    !sql
    INSERT INTO USER (FIRSTNAME, LASTNAME, AGE, ADDRESS) VALUES ( ?, ?, ?,?)

