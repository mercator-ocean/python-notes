
# Plan de formation

- Présentation & Historique
- Syntaxe et bases du langage
- Approche Orientée Objet
- Programmation Orientée Objet en Python
- Librairies standard
- **Outils de qualité et tests**


--------------------------------------------------------------------------------

## Outils de qualités et tests

- Les logs
- Le debugger
- Les exceptions
- La documentation
- Les tests
- La mesure des performances
- La mesure de la qualité du code


--------------------------------------------------------------------------------

## Outils de qualités et tests

Une autre grande force du langage Python est qu'il dispose de tout un
 tas d'outils permettant de vérifier la **qualité de votre code**, et
 notamment de le tester.
 
Ces outils sont tellement importants dans le monde de Python qu'ils
 sont devenus un art de programmer, voire même un art de vivre.
 
En Python, quand on crée un programme, les bonnes pratiques veulent
 que l'on crée d'abord des fonctions qui testeront les fonctions de
 notre programme avant d'écrire le programme proprement dit.
 
On appelle cela la **programmation par les tests**.


--------------------------------------------------------------------------------

## Outils de qualités et tests

Pour découvrir toutes ces nouvelles sensations, nous vous proposons
 de reprendre le module `booleens` que nous avons créé dans la
 partie `découverte des fonctions` ainsi que les script des
 2 techniques d'intersection.

Avant de véritablement démarrer sur la partie `qualité logicielle`,
nous allons apprendre 2/3 notions complémentaires :

- Les logs
- Le *debugging*
- Les Exceptions


--------------------------------------------------------------------------------

## Outils de qualités et tests

### Exercice

Exécutez les fonctions `xor` de votre module `booleens`
 en leur passant des paramètres non booléens.
 
Faîtes différents essais jusqu'à ce que :

- Vous obteniez des résultats erronés
- Ou vous obteniez des valeurs non booléennes

Si vraiment vous n'y arrivez pas, essayez en mixant des valeurs comme
 None, '', et des chaînes de caractères.

Vous allez voir, ça devrait finir par boguer !

![](images/exercice-1.png)


--------------------------------------------------------------------------------

## Outils de qualités et tests

- **Les logs**
- Le debugger
- Les exceptions
- La documentation
- Les tests
- La mesure des performances
- La mesure de la qualité du code


--------------------------------------------------------------------------------

## Outils QA – Les logs

**Ca y est ! Ca bogue !**

Cool…

Debuggons !

La première technique que je vous propose pour deboguer consiste à
 créer des logs.

Python possède pour cela un module nommé
 `logging`

<https://docs.python.org/3.4/library/logging.html>
![](images/ca-y-est-ca-bogue.png)
 


--------------------------------------------------------------------------------

## Outils QA – Les logs

Le module `logging` permet d'afficher des messages permettant de suivre
 la trace de votre programme.

Ces messages peuvent avoir différents niveaux d'importance :

- `DEBUG`, le niveau le plus faible<br />
`var1 = 10`
- `INFO`, un message d'information<br />
`initialisation de var1`
- `WARN`, un avertissement<br />
`attention, fichier non trouvé`
- `ERROR`, une erreur<br />
`Erreur d'écriture du fichier`
- `CRITICAL` ou `FATAL`, un message critique<br />
`Plus d'espace disque, arrêt du système`


--------------------------------------------------------------------------------

## Outils QA – Les logs

A chaque niveau de criticité, le module `logging` propose une
 fonction du même nom, en minuscules.

    !python
    import logging
    logging.debug("Salut")
    logging.info("Je te le dis")
    logginga.warn("Arrête tes bêtises !")
    logging.error("Ou un problème")
    logging.fatal("fatal se produira !")
 
 <!-- -->
 
    WARNING:root:Arrête tes bêtises !
    ERROR:root:Ou un problème
    CRITICAL:root:fatal se produira !


--------------------------------------------------------------------------------

## Outils QA – Les logs

Les messages de logging sont affichés dans le flux d'erreur standard
 par défaut.

Ils peuvent donc se retrouver mélangés avec les messages de la
fonction `print` dans un ordre par forcément cohérent car cette
dernière écrit dans la sortie standard.

Ces 2 flux sont mélangés dans une console Unix/Windows, c'est une
des raisons pour lesquelles on préfère stocker les logs dans un
fichier

Enfin, par défaut le module logging n'affiche pas les messages dont
le niveau est inférieur à `WARN`

Vous pouvez paramétrer ceci avec la fonction `basicConfig`


--------------------------------------------------------------------------------

## Outils QA – Les logs

La fonction `basicConfig` permet de personnaliser la gestion des logs.

Elle accepte plusieurs paramètres :

- `level`, Le niveau de log, par exemple logging.INFO
- `filename`, le nom du fichier de logs à utiliser
- `format`, une chaine indiquant le format des logs.

--------------------------------------------------------------------------------

## Outils QA – Les logs

La chaîne `format` utilise le formatage de chaîne avec un dictionnaire :
 <https://docs.python.org/3.4/library/logging.html#logrecord-attributes> 

- `%(asctime)s` : Date/Heure
- `%(filename)s` : Nom de fichier du script Python
- `%(funcName)s` : Nom de la fonction ou le log est écrit
- `%(lineno)d` : Numéro de la ligne ou le log est écrit
- `%(message)s` : Emplacement de votre message dans la chaîne de log


--------------------------------------------------------------------------------

## Outils QA – Les logs

### Exercice

Utilisez la fonction `basicConfig` pour écrire vos logs dans un
 fichier nommé `booleens.log` avec le niveau `INFO` et en
 affichant :

- La date et l'heure
- Le niveau de log
- Le nom du fichier
- Le nom de la fonction
- Le numéro de la ligne
- Le message de log

Ajoutez des messages dans la fonction `xor` problématique pour
 afficher les valeurs des paramètres `a` et `b` ainsi que le
 résultat de l'évaluation


--------------------------------------------------------------------------------

## Outils de qualités et tests

- Les logs
- **Le debugger**
- Les exceptions
- La documentation
- Les tests
- La mesure des performances
- La mesure de la qualité du code

--------------------------------------------------------------------------------

## Outils QA – Le debugger

### Bravo !

Vous avez affiché des logs, mais vous ne comprenez toujours
 pas pourquoi vous avez un résultat non attendu dans votre fonction.

Python possède un debugger intégré en ligne de commande.

Il est rudimentaire mais très pratique, surtout quand vous devez
 intervenir sur un serveur sans interface graphique.

Il est inclus dans le module `pdb`, **Python DeBugger**.

Pour l'invoquer vous devez ajouter cette ligne dans votre programme :

    !python
    import pdb; pdb.set_trace()  # 2 instructions pour interrompre avec un debugger
    r = xor1(0, None)
    print(r)


--------------------------------------------------------------------------------

## Outils QA – Le debugger

La fonction `pdb.set_trace()` positionne un point d'arrêt dans
 votre programme et affiche un prompt dans la console.

Vous pouvez alors saisir la commande `help` pour connaître les commandes disponibles :
    
    -> r = xor1(0, None)
    (Pdb) help
    Documented commands (type help <topic>):
    ========================================
    EOF    c          d        h         list      q        rv       undisplay
    a      cl         debug    help      ll        quit     s        unt
    alias  clear      disable  ignore    longlist  r        source   until
    args   commands   display  interact  n         restart  step     up
    b      condition  down     j         next      return   tbreak   w
    break  cont       enable   jump      p         retval   u        whatis
    bt     continue   exit     l         pp        run      unalias  where
      
    Miscellaneous help topics:
    ==========================
    pdb  exec


--------------------------------------------------------------------------------

## Outils QA – Le debugger

Les commandes les plus utilisées sont :

- `l` ou `list` pour afficher l'emplacement de la ligne courante dans le code
- `n` ou `next` pour exécuter l'instruction suivante
- `s` ou `step` pour rentrer dans la fonction de l'instruction suivante
- `u` ou `up` pour remonter dans la fonction
- `c` ou `continue` pour rendre la main à Python

Vous pouvez aussi saisir toute expression Python dans PDB comme dans
 l'interpréteur Python. Notamment afficher vos variables.

Attention aux commandes : si vos variables ont des noms identiques, ne saisissez pas
 juste leur nom mais `print(<var>)`, sinon vous exécuterez la commande 


--------------------------------------------------------------------------------

## Outils QA – Le debugger

**SUPPRIMEZ TOUJOURS LES APPELS DES POINTS D'ARRETS une fois le
 debuggage terminé**

Sinon votre programme s'arrêtera de nouveau lorsqu'il passera sur ces
 lignes.

S'il est lancé en tâche de fond, cela le bloquera et vous risquerez
 de ne pas vous en rendre compte immédiatement... 

Avec les quelques déconvenues possibles...


--------------------------------------------------------------------------------

## Outils QA – Le debugger

### Exercice

Placez un point d'arrêt avant l'appel de votre fonction `xor` puis :

- Avec `pdb` rentrez dans la fonction.
- Affichez les valeurs des paramètres `a` et `b`
- Evaluez dans l'interpréteur l'expression opérateur par opérateur et
 identifiez la cause du problème observé

--------------------------------------------------------------------------------

## Outils de qualités et tests

- Les logs
- Le debugger
- **Les exceptions**
- La documentation
- Les tests
- La mesure des performances
- La mesure de la qualité du code


--------------------------------------------------------------------------------

## Outils QA – Les exceptions

**Bravo !**
 
Vous avez identifié la cause de ce vilain bug :

Votre fonction est conçue pour manipuler des booléens, comme vous
 lui avez passé des paramètres d'un autre type, les opérateurs
 booléens retournant l'opérande d'une opération et non son équivalent
 booléen, vous vous retrouvez avec des résultats non souhaités.

Nous allons lever des exceptions pour arrêter le traitement dans la
 fonction `xor` si les opérandes passées en arguments ne sont pas
 booléennes.

Ceci fera les pieds aux développeurs qui ne respectent pas votre
 documentation...


--------------------------------------------------------------------------------

## Outils QA – Les exceptions

Une **exception** est une interruption de traitement qui est remontée à
 la fonction appelante, et ainsi de suite jusqu'à ce qu'une des
 fonctions appelantes traite cette exception, ou, à défaut, jusqu'au
 programme principal.

Si ce dernier n'a pas prévu de traiter cette exception le programme
 est arrêté.

Une exception est un objet en Python issu de la classe Exception.

Pour lever une exception, vous devez instancier une variable de la
 classe Exception, ou d'une de ses sous classes, avec un mot clef
 particulier `raise`.
    
    !python
    raise Exception("Erreur : Et pan ! Fallait bien coder !")


--------------------------------------------------------------------------------

## Outils QA – Les exceptions

Quelques exemples d’exceptions courantes :

- `KeyError` quand on essaye d’accéder à une clé non existante d’un mapping
- `IndexError` quand on essaye d’accéder à un indice inexistant d’une séquence
- `TypeError` quand on fait une opération avec des valeurs de mauvais type<br />
  `(1 + "toto")`
- `ValueError` quand on fait une opération avec des valeurs qui ne permettent
pas le traitement (racine carrée d’un nombre négatif par exemple)

--------------------------------------------------------------------------------

## Outils QA – Les exceptions

    !python
    def xor1(a,b):
        """
        Fonction xor1(a,b)
        
        Retourne le OU exclusif entre 2 booléens a et b
        """
        logging.info("a=%s, b=%s" % (a,b))
        
        if type(a) != bool or type(b) != type(True):
            logging.error("Paramètre 'a' ou 'b' invalide")
            raise Exception("Les paramètres a et b doivent être de type bool")
        
        r = (a or b) and not (a and b)
        logging.info(" a xor b = %s" % r)
        return r

<!-- -->

    ERROR:root:Paramètre 'a' ou 'b' invalide
    Traceback (most recent call last):
      File "/home/makina/FormationPython/test_outils.py", line 10, in <module>
        r = xor1(0, None)
      File "/home/makina/FormationPython/outils/booleens.py", line 24, in xor1
        raise Exception("Les paramètres a et b doivent être de type booléen")
    Exception: Les paramètres a et b doivent être de type booléen


--------------------------------------------------------------------------------

## Outils QA – Les exceptions

Si vous savez qu'une fonction est susceptible de générer des
 exceptions vous pouvez les intercepter en l'entourant d'un bloc "`try, except`"

- Le mot clef `try` débute un bloc d'interception d'exception.
- Le mot clef `except` indique le traitement à effectuer si une
 exception se produit. Après son exécution on sort du bloc
 `try`. Le code après l'instruction ayant généré l'exception
 n'est pas exécuté.
- Le mot clef `else` peut aussi être présent après les clauses
 `except` pour indiquer une action à réaliser si aucune exception
 ne s'est produite.
- Le mot clef `finally` peut être présent en tout dernier pour
 indiquer une action à exécuter en fin de bloc, quoiqu'il arrive,
 exception ou pas.


--------------------------------------------------------------------------------

## Outils QA – Les exceptions

    !python
    try:
        r = xor1(0, None) # exception ici
        print("Ne sera donc pas exécuté")
    except Exception as err:
        print("Une erreur est survenue:", err)
    else:
        print("Exécuté uniquement si pas d'exception")
    finally:
        print("Toujours exécuté")


--------------------------------------------------------------------------------

## Outils QA – Les exceptions

Les exceptions sont des classes.

Il y a donc une hiérarchie d'exceptions.

![](images/les-exceptions-sont-des-classes.png)



--------------------------------------------------------------------------------

## Outils QA – Les exceptions

- Vous pouvez décider de n'intercepter que certaines exceptions en
 indiquant dans la clause `except` les classes interceptées
Votre
 traitement sera appliqué pour toutes ces classes et leurs filles
- Vous pouvez avoir plusieurs clauses `except` pour réaliser des
 traitements différents
- Vous pouvez lever une autre exception ou transmettre la même dans une
 clause `except`
- Vous pouvez créer vos propres classes d'exception


--------------------------------------------------------------------------------

## Outils QA – Les exceptions

    !python
    try:
        a = 10 / 0 # division par zero
        r = xor1(True, False) 
        print("Ne sera donc pas exécuté")
    except (ZeroDivisionError, ValueError) as err:
        print("Division par zéro, c'est malin !")
    except Exception as err:
        print("Une erreur est survenue:", err)
        raise err
    else:
        print("Exécuté uniquement si pas d'exception")
    finally:
        print("Toujours exécuté")


--------------------------------------------------------------------------------

## Outils QA – Les exceptions

Pour connaître la classe d'une exception vous pouvez

- Lire la documentation de Python
- La retrouver dans le message d'erreur généré

<!-- -->

    !pycon
    >>> 10 / 0
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero


--------------------------------------------------------------------------------

## Outils de qualités et tests

- Les logs
- Le debugger
- Les exceptions
- **La documentation**
- Les tests
- La mesure des performances
- La mesure de la qualité du code


--------------------------------------------------------------------------------

## Outils QA – Documentation

- Nous avons vu que les docstrings placées en début de module, de
 classe ou de fonction sont stockées dans l'attribut `__doc__` de
 ces objets.
- Le système d'aide de l'interpréteur Python les utilise pour afficher
 la description de ces objets via la commande `help`.
- Vous pouvez aussi générer une documentation automatique dans
 différents formats avec le module  `pydoc`:<br />
<https://docs.python.org/3.4/library/pydoc.html>
 
 <!-- -->
 
    !bash
    pydoc -w outils.booleens
    firefox outils.booleens.html


--------------------------------------------------------------------------------

## Outils QA – Documentation

Il existe plusieurs autres outils d'extraction automatique de
 documentation depuis les sources de Python et notamment des docstrings.

- Sphinx et autodoc :<br />
<http://sphinx.pocoo.org/> 
- Doxygen :<br />
<http://www.doxygen.org/> 
- Liste assez complète d'autres outils :<br />
<https://wiki.python.org/moin/DocumentationTools> 



--------------------------------------------------------------------------------

## Outils de qualités et tests

- Les logs
- Le debugger
- Les exceptions
- **La documentation**
- (et...) **Les tests**
- La mesure des performances
- La mesure de la qualité du code

--------------------------------------------------------------------------------

## Outils QA – Documentation & tests

La documentation présente dans les docstrings peut aussi servir
 à générer des tests unitaires automatiques.

Complétez la documentation de la fonction `xor` pour qu'elle
inclue des exemples comme si vous l'appeliez depuis l'interpréteur 
    
    !python
    def xor(a,b):
        """Fonction xor1(a,b)
        
        Retourne le OU exclusif entre 2 booléens a et b
        Exemples:
        
        >>> xor(True, True)
        False
        >>> xor(True, False)
        True
        >>> xor(False, True)
        True
        """


--------------------------------------------------------------------------------

## Outils QA – Documentation & tests

Python possède un module nommé `doctest` :

<https://docs.python.org/3.4/library/doctest.html> 

Ce module permet d'extraire les commandes suivant le prompt '>>>' dans
les docstrings de vos modules et d'exécuter le code associé pour le
comparer au résultat affiché en dessous.

Pour cela ajoutez les lignes suivantes en fin de votre module :

    !python
    if __name__ == "__main__":
        import doctest
        doctest.testmod()

Puis exécutez-le. Rien ne se passe…

![](images/doctest.png)



--------------------------------------------------------------------------------

## Outils QA – Documentation & tests

Si rien ne se passe c'est que tout va bien !

Vous pouvez changer un test en mettant volontairement un résultat
faux ou passer l'option `verbose=True` à la méthode testmod()

<!-- -->
    
    Trying:
       xor(True, True)
    Expecting:
       False
    ok
    Trying:
       xor(True, False)
    Expecting:
       True
    ok
    ...
    1 items had no tests:
       __main__
    1 items passed all tests:
       4 tests in __main__.xor1
    4 tests in 3 items.
    4 passed and 0 failed.
    Test passed.


--------------------------------------------------------------------------------

## Outils QA – Documentation & tests

Ce module présente quand même quelques inconvénients :

- Les docstrings deviennent vite énormes, et on se retrouve avec une
 documentation démesurée en regard de la taille du code
    - Pour cela vous pouvez externaliser les tests dans un fichier texte. *Super !*
- Les tests sont rudimentaires.
    - Ce sont des tests unitaires

Si vous voulez des tests plus riches, tenant sur plusieurs lignes, ou
des tests fonctionnels, il y a d'autres modules.


--------------------------------------------------------------------------------

## Outils QA – Documentation & tests

Fichier texte pour le module booleens: 'booleens.txt'
    

    >>> from outils.booleens import xor  # D'abord importer le module !
    >>> xor(True, True)
    False

Executer le doctest:
    
    !bash
    $ python -m "doctest" outils/booleens.txt -v
    Trying:
    from outils.booleens import xor
    ok
    Trying:
    xor(True, True)
    Expecting:
    False
    ok
    1 items passed all tests:
    2 tests in booleens.txt
    2 tests in 1 items.
    2 passed and 0 failed.
    Test passed.


--------------------------------------------------------------------------------

## Outils QA – Documentation & tests

### Exercice

Complétez les tests de la fonction `xor` pour vous assurer
 qu'une erreur est bien levée quand vous passez des paramètres non
 booléens.
 
Indication : Regardez la documentation du module sur le site de Python

--------------------------------------------------------------------------------

## Outils de qualités et tests

- Les logs
- Le debugger
- Les exceptions
- La documentation
- **Les tests**
- La mesure des performances
- La mesure de la qualité du code

--------------------------------------------------------------------------------

## Outils QA – Frameworks de tests

- Python est accompagné d'un autre module de tests nommé
  **unittest** :<br />
  <https://docs.python.org/3.4/library/unittest.html><br />
  Un  excellent tutorial est fourni sur le site *Dive into Python* :<br />
  <http://www.diveintopython3.net/unit-testing.html> 
- Le framework privilégié sur les nouveaux projets est **py.test** :<br />
  <http://pytest.org/latest/><br />
  Nous allons suivre son tutorial et écrire les tests pour `xor`

Il en existe d'autres :

- **Nose**, 
  <br /><https://nose.readthedocs.org/en/latest/> 
- Une liste complète des outils de testing en python : <br />
 <https://wiki.python.org/moin/PythonTestingToolsTaxonomy> 


--------------------------------------------------------------------------------

## Outils de qualités et tests

- Les logs
- Le debugger
- Les exceptions
- La documentation
- Les tests
- **La mesure des performances**
- La mesure de la qualité du code

--------------------------------------------------------------------------------

## Outils QA – Mesures de performances

Maintenant, nous savons :

- Debugger
- Écrire des programmes robustes avec les exceptions
- Bien les documenter
- Tester automatiquement nos programmes

Nous allons pouvoir passer à l'étape suivante :

- Mesurer les performances de nos programmes

Pour cela nous allons étudier 2 modules fournis par Python :

- `timeit`
- `cProfile`


--------------------------------------------------------------------------------

## Mesures de performances - timeit

Le module `timeit` permet de tester les performances d'un petit bout de code.
<https://docs.python.org/3.4/library/timeit.html>

Il convient de préciser *"petit bout de code"* car il permet de
 tester un morceau de code fourni dans une chaîne de caractères.
 
Il n'est pas adapté pour de véritable programmes.

Mais est très pratique pour tester rapidement la validité d'une solution.


--------------------------------------------------------------------------------

## Mesures de performances - timeit

Parmi les fonctions qu'il propose, la fonction `timeit` permet
 d'exécuter un code un certain nombre de fois et de retourner son temps
 moyen d'exécution.

Elle prend 3 paramètres :

- `stmt`, le code à tester
- `setup`, un code initial à exécuter au préalable, souvent
 utilisé pour initialiser des paramètres utilisés dans `stmt`
- `number`, nombre de fois que le code sera exécuté (1 million
 par défaut)

<!-- -->

    !pycon
    >>> import timeit
    >>> t = """
    ... for i in range(1000*1000):
    ...   a = a +i
    ... """
    >>> timeit.timeit(setup="a=0", stmt=t, number=5)
    0.23607094200269785


--------------------------------------------------------------------------------

## Mesures de performances - timeit

### Exercice

- Utilisez le module `timeit` pour mesurer le temps d'exécution des 2
 implémentations de l'intersection de 2 listes.
- Mesurez le ratio des 2 temps d'exécution des 2 solutions.
- Etes-vous convaincu par la version utilisant les dictionnaires ?

Le tutorial ci-dessous vous permettra de bien comprendre les dessous
 de l'histoire :
 
<http://makina-corpus.com/blog/metier/2014/python-tutorial-reducing-algorithm-complexity-from-n-n-to-2-n>
 


--------------------------------------------------------------------------------

## Mesures de performances - cProfile

Les modules `profile` et `cProfile` fournis avec Python
 permettent de mesurer les performances de l'ensemble ou partie de votre
 programme.

Ils ne permettent cependant de mesurer que la durée d'exécution des
 fonctions et non celle du code situé directement à la racine de votre
 programme.

Pour les utiliser il convient 

- d'instancier un objet de la classe `Profile`,
- d'appeler la méthode `enable` pour activer le profiling du code,
- d'appeler la méthode `disable` pour le désactiver.


--------------------------------------------------------------------------------

## Mesures de performances - cProfile

- Ces modules collectionnent des informations de statistiques sur la
 portion de code analysée.
- Vous pouvez les afficher via le module `pstats`

L'usage le plus fréquent est le suivant :

    !python
    import cProfile, pstats, io
    pr = cProfile.Profile()
    pr.enable() # début profiling
    # ... le code à tester ici ...
    pr.disable() # fin profiling
    # statistiques
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


--------------------------------------------------------------------------------

## Mesures de performances - cProfile

### Exercice

- Transformez les techniques d'intersection en 2 fonctions prenant 2
 listes en arguments.
- Mesurez leurs temps d'exécution à l'aide du module `cProfile`
 comme indiqué dans l'exemple précédent.
- Vérifiez les mesures avec celles retournées par `timeit`

--------------------------------------------------------------------------------

## Outils de qualités et tests

- Les logs
- Le debugger
- Les exceptions
- La documentation
- Les tests
- La mesure des performances
- **La mesure de la qualité du code**

--------------------------------------------------------------------------------

## Outils QA – Mesures de qualité

L'outil **Pylint** permet d'évaluer la qualité vos programmes en leur attribuant une note.
 
<http://www.pylint.org/>
 
Il détecte :

- code dupliqué,
- variables non déclarées,
- variables non utilisées,
- modules non importés,
- documentation manquante,
- respect de la convention de codage PEP8


--------------------------------------------------------------------------------

## Outils QA – Mesures de qualité

Flake8 est aussi une excellente alternative

<https://pypi.python.org/pypi/flake8> 

- Il s'utilise simplement en ligne de commande en lui passant le nom du
 fichier à analyser
- Il s'intègre facilement avec les éditeurs Python comme Eclipse,
 Spyder ou Vim
- Il est accompagné d'un programme `pyreverse` permettant de
 générer les diagrammes UML des classes Python


--------------------------------------------------------------------------------

## Outils QA – Mesures de qualité

### Exercices

- Utilisez la commande `pylint` sur votre module `booleens`
- Utilisez la commande `pyreverse`  sur votre module `Vehicules`

<!-- -->

    !bash
    $ pyreverse approche_poo -o png

