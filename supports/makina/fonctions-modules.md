
## Plan de formation

.fx: plan-formation

- Présentation & Historique
- **Syntaxe et bases du langage**
- Approche Orientée Objet
- Programmation Orientée Objet en Python
- Librairies standard
- Outils de qualité et tests


--------------------------------------------------------------------------------

# Les fonctions, modules et packages


![](images/ecolepourtousse.png)

--------------------------------------------------------------------------------

# Plan de formation : Syntaxe et bases du langage

.fx: section-first-page

- Les types et variables
- **Les fonctions**
- Les modules
- Les générateurs
- map, filter, reduce, zip

--------------------------------------------------------------------------------

## Les fonctions - Définition

Pour définir une fonction on utilise le mot clef `def`.

    !python
    def f1():
        print("Fonction 1")
 
Pour exécuter une fonction on saisit son nom suivi de parenthèses. 
    
    !python
    f1() # Appel de la fonction

Les fonctions ne sont pas typées en python.


--------------------------------------------------------------------------------

## Les fonctions – Paramètres

Une fonction peut accepter des **paramètres**.

Ils sont écrits entre parenthèses après le nom de la fonction.

Les paramètres ne sont pas typés non plus.

    !python
    def f2(a, b):
        print("Fonction 2")
        print("a=%s, b=%s" % (a,b))

    x = 10
    y = 20
    f2(x,y)
    f2(3,4)


--------------------------------------------------------------------------------

## Fonction / procédure

- En python, il n'y a pas vraiment de différence entre fonction et procédure.
- On appellera **procédure** une fonction qui ne retourne pas de valeur.
- Par convention en python, une fonction qui modifie un paramètre ou un objet
  ne renvoit pas de valeur.


--------------------------------------------------------------------------------

## Les fonctions – Valeur de retour

- Une fonction peut retourner une valeur.
- La valeur est retournée via le mot clef `return`.
- La fonction s'arrête après l'exécution de l'instruction `return`.


<!-- -->

    !python
    def f3(a, b):
        print("Fonction 3")
        return a * b + a + b
        
    f3(2,5)
    r = f3(4,6)
    print("Résultat de f3: %s" % r)


--------------------------------------------------------------------------------

## Les fonctions – Exercice

Écrivez une fonction `min_max` prenant une liste de nombres en
paramètre et renvoyant le minimum et le maximum.
 
_Une fonction ne peut pas vraiment retourner plusieurs valeurs.
Mais pour le simuler, c'est tout simple, pensez aux tuples !_


--------------------------------------------------------------------------------

## Les fonctions – Ordre des paramètres

Quand on passe des valeurs ou des variables en paramètre aux
fonctions ils sont affectés dans l'ordre de saisie.
 
Il est toutefois possible de **nommer** les paramètres que l'on passe.<br />
Dans ce cas on n'est pas tenu de respecter l'ordre de passage.

    !python
    def f5(a,b):
        print("a=%s, b=%s" % (a,b))
        
    x = 10
    y = 20
    f5(5,6)
    f5(a=5, b=6)
    f5(b=6, a=5)
    f5(x, y) 
    f5(b=y, a=x)


--------------------------------------------------------------------------------

## Les fonctions – Valeurs par défaut

Les paramètres des fonctions peuvent accepter des **valeurs par
 défaut**.

Dans ce cas il n'est pas nécessaire de définir ces paramètres lors
 de l'appel de la fonction.

Tous les paramètres ne sont pas obligés d'avoir une valeur par
défaut, dans ce cas ils sont obligatoirement listés avant les autres.

    !pycon
    >>> def f6(a, b=5, c=(10,20)):
    >>>     print("Fonction 6 - valeurs par défaut")
    >>>     print("a=%s, b=%s, c=%s" % (a, b, c))
    
    >>> f6() 
    TypeError: f6() missing 1 required positional argument: 'a'
    
    >>> f6(10)
    >>> f6(1, 2)
    >>> f6(10, 3, 4)
    >>> f6(5, c=25)
    >>> f6(8, b=32)
    
    >>> f6(c=4,b=3) 
    TypeError: f6() missing 1 required positional argument: 'a'
    >>> def f6b(b=5, a):
            pass
    SyntaxError: non-default argument follows default argument


--------------------------------------------------------------------------------

## Les fonctions – Liste non définie de paramètres

- Une fonction peut avoir un nombre indéfini de paramètres
 « positionnels »
- Dans ce cas les paramètres supplémentaires peuvent être
 récupérés dans un argument préfixé d'une étoile « * »    

<!-- -->
    !pycon
    >>> def moyenne(*valeurs):
    ...     return sum(valeurs) / len(valeurs)
    ... 
    >>> moyenne(2,4)
    3.0

- Le nom de cet argument est à votre discrétion.
- Son type sera celui d'un tuple.
- Il pourra être vide si aucun paramètre supplémentaire n'est
  transmis en plus des paramètres positionnels déclarés.


--------------------------------------------------------------------------------

## Les fonctions – Liste non limitée de paramètres

    !python
    def f7(a, b, *p_tuple):
        print("Fonction 7")
        print("a=%s, b=%s" % (a,b))
        # Ici vous me posez une question
        print("p_tuple = %s" % (p_tuple,) ) 
    
    f7(1,2)
    f7(1,2,3)
    f7(1,2,('a', 'b'), 'toto', "canari")
    f7(1,2,('a', 'b'), 'toto', titi="canari")
    TypeError: f7() got an unexpected keyword argument 'titi'


--------------------------------------------------------------------------------

## Réponse à la question – 42 ?

### Mais connaissez-vous vraiment la question ?#

Pourquoi avoir écrit : "p_tuple =%s" % (p_tuple,)

Si j'avais écrit :

    !pycon
    >>> def f7(a, b, *p_tuple):
    ...     print("Fonction 7")
    ...     print("a=%s, b=%s" % (a,b))
    ...     print("p_tuple = %s" % (p_tuple) )

Alors :

    !pycon
    >>> f7(1,2,3,4)
    Fonction 7
    a=1, b=2
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 4, in f7
    TypeError: not all arguments converted during string formatting
    
<!-- -->
    
    !pycon
    Traceback (most recent call last):
    File "/tmp/fonctions.py", line 56, in <module>
    f7(1,2,3,4)
    TypeError: not all arguments converted during string formatting
   

--------------------------------------------------------------------------------

### Réponse à la question – Ce n'est pas 42

- Le formatage avec  `%s % <variables>` attend une liste de paramètres
 passés sous la forme d'un tuple.
- Si le paramètre à formater est lui-même un tuple cela peut poser
 des problèmes.
- Sans la notation `(p,)` soit avec « `(p)` ou `p`, Python
 considérera que les paramètres à formater sont contenus dans le
 tuple.
- Il affichera le premier dans le premier `%s` trouvé et voudra
 afficher les autres valeurs du tuple dans d'autres `%s` de la
 chaîne qu'il ne trouve malheureusement pas.
- En écrivant `(p,)` on indique que l'on passe un tuple d'un élément,
 qui peut être un tuple ou non.


--------------------------------------------------------------------------------

### Réponse à la question – pour bien comprendre


    !pycon
    >>> a = 10
    >>> "a = %s" % a
    'a = 10'
    >>> a = [1,2,3]
    >>> "a = %s" % a
    'a = [1, 2, 3]'
    >>> a = (1,2,3)
    >>> "a = %s" % a
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: not all arguments converted during string formatting
    >>> "a = %s, b = %s, c = %s" % a
    'a = 1, b = 2, c = 3'
    >>> "a = %s" % (a,)
    'a = (1, 2, 3)'
    
C'était une excellente question ! Comme toutes les autres...


--------------------------------------------------------------------------------

## Les fonctions - Liste non limitée de paramètres

- Une fonction peut accepter une liste non limitée de paramètres
 nommés aussi appelés **keyword arguments**, passés sous la forme
 `param=valeur`.
- Cette liste d'arguments peut être précédée du paramètre recevant
 la liste d'arguments optionnels et non nommés `*p_tuple`.
- Le paramètre récupérant les arguments nommés non définis dans la
 signature de la fonction doit être préfixé par deux étoiles : `**`.
- Son nom est à votre discrétion.
- Son type sera celui d'un dictionnaire dont les clefs seront les noms
 des paramètres supplémentaires et les valeurs leurs valeurs.


--------------------------------------------------------------------------------

## Les fonctions - Liste non limitée de paramètres

### Avez-vous été attentif ?

Essayez de deviner le résultat

    !python
    def f8(a, b=10, *c, **d):
        print("f8 - Paramètres optionnels")
        print("a=%s, b=%s" % (a,b) )
        print("c=%s" % (c,))
        print("d=%s" % (d,))
    
    f8(1)
    f8(1,(1,2), 3, 4, 5, 6)
    f8(a=1,b=(1,2), c=3, d=4, e=5, f=6)
    f8(1,(1,2), 3, 4, e=5, f=6)


--------------------------------------------------------------------------------

## Les fonctions – Passage de paramètres par expansion

Alors ces fonctions ?

C'est simple non ?

C'est puissant ?

C'est presque intuitif… Presque.

C'est facile à retenir.

**Mais Python peut encore vous faciliter la vie !**


--------------------------------------------------------------------------------

## Les fonctions – Passage de paramètres par expansion

Le passage de paramètres par expansion permet de passer 
plusieurs paramètres distincts d'une fonction 
à l'aide d'une seule liste ou d'un seul dictionnaire.

### Paramètres positionnels : on utilise une liste

La liste doit être préfixée par `*`

    !python
    moyenne(*[2, 3, 4])
    # Correspond à:
    moyenne(2, 3, 4)

Les éléments de la liste sont passés comme des paramètres positionnels.

--------------------------------------------------------------------------------

### Paramètres nommés : on utilise un dictionnaire   

Le dictionnaire est préfixé par `**`.

    !python
    mafonction(**{'a': 1, 'b': 2})
    # Correspond à:
    mafonction(a=1, b=2}


Les éléments du dictionnaire sont passés comme des paramètres
 nommés où le nom du paramètre est la clef du dictionnaire.

Ceci impose que les clefs soient des chaînes de caractères.


--------------------------------------------------------------------------------

## Les fonctions – Paramètres par expansion

Passage d'arguments positionnels par extension :
    
    !python
    def affiche_personnages(pers1, pers2, pers3):
        print("personnages : %s, %s, %s" % (pers1, pers2, pers3))
    liste_personnages  = ("riri", "fifi", "loulou")
    print(affiche_personnages(*personnages))
    riri, fifi, loulou

    affiche_personnages(*("picsou", "riri", "fifi", "loulou"))
    TypeError: affiche_personnages() takes 3 positional arguments but 4
    were given
    
### Question

Comment faut-il modifier l'implémentation de
`affiche_personnages` pour que le code permette d'afficher autant de
personnages qu'on veut ?


--------------------------------------------------------------------------------

## Les fonctions – Passage de paramètres par expansion

Passage d'arguments mots-clés par extension :
    
    !python
    def affiche_groupes_personnages(canards=(), ecureuils=()):
        print(" canards : ")
        affiche_personnages(*canards)
        print(" ecureuils : ")
        affiche_personnages(*ecureuils)
    
    personnages = {'canards': liste_canards
                   'ecureuils': liste_ecureuils}
    print(affiche_personnages(**personnages))
    

### Question
Comment pourrait-on modifier l'implémentation de `affiche_groupes_personnages`
pour que le code permette d'afficher autant de groupes de personnages qu'on veut ?


--------------------------------------------------------------------------------

## Les fonctions - fonctions de premier ordre

Les fonctions en python sont dites « de premier ordre ».

Cela signifie que vous pouvez passer des fonctions en paramètre de fonctions

    !python
    import time
    def execute_n_fois(n, procedure):
        for i in range(n):
            procedure()
            time.sleep(delay)

    def affiche_echo():
        print("Echo")

    execute_n_fois(5, affiche_echo)

### Question

Que fait ce code ?

Comment pourrait-on faire pour rendre le texte affiché paramétrable ?


--------------------------------------------------------------------------------

## Les fonctions - récursivité

Python permet la récursivité des fonctions

    !python
    def compte_a_rebours(n):
        print(n)
        if n > 0:
            compte_a_rebours(n-1)
            
    compte_a_rebours(10)

### Exercice
Implémenter une fonction `factorielle(n)` en utilisant la récursivité


--------------------------------------------------------------------------------

# Les modules et packages

.fx: section-first-page

--------------------------------------------------------------------------------

# Plan de formation : Syntaxe et bases du langage

.fx: section-first-page

- Les types et variables
- Les fonctions
- **Les modules**
- Les générateurs
- map, filter, reduce, zip

---------------------------------------------------

## Packages, Modules

### Définition : package
Le terme **package** est utilisé pour désigner un ensemble de
 modules Python dont les fonctions et variables qu'ils définissent
 peuvent être utilisés par d'autres programmes.

Concrètement un package est un **dossier** de votre disque contenant éventuellement un fichier nommé `__init__.py`
Un package peut contenir d'autres packages.

*Pypi* est le *Python Package Index*.


### Définition : module
Un **module** est un script Python contenu dans un Package.

*Le terme librairie / bibliothèque est un terme générique utilisé pour désigner soit un
 package, soit un module, soit un ensemble de packages.*


--------------------------------------------------------------------------------

### Packages - `__init__.py`

- Le fichier « `__init__.py` » était obligatoire jusqu'à Python 3.2
- Si il existe, il peut contenir des fonctions et variables et autres objets
 Python


--------------------------------------------------------------------------------

## Packages
 
### Exercice

- Créez un package nommé « `outils` » contenant un module nommé
 « `booleens` »
- Définissez la variable `PI` directement dans le fichier `__init__` du
 package.
- Définissez et implémentez une fonction « `xor` » dans le module
 booléen.
- Cette fonction prendra 2 paramètres « a » et « b » supposés
 être des booléens.
- Écrire dans le module « `booleens` » un code permettant de vérifier
 le bon fonctionnement de votre fonction.


--------------------------------------------------------------------------------

## Packages – Utilisation

- Pour utiliser les éléments d'un package depuis un programme Python
 il convient d'utiliser le mot-clef « `import` »
- L'import d'un package et de ses modules se fait via 2 syntaxes
 différentes :
    - `import <package>[.<sous package>.<module>.<objet>]`
    - `from <package>[.<sous package>…] import <objet>`
- Lors de l'import, le contenu des fichiers importés est exécuté,
 avec tout ce que cela implique.
- Le fichier exécuté pour l'import d'un package est `__init__.py`.
- Même si vous faîtes plusieurs imports pour un même package ou
 module, il ne sera exécuté qu'une fois.
Pas de `#if def` /  `#if ndef` comme en C/C++.


--------------------------------------------------------------------------------

## Package - Utilisation

- Au même niveau que le dossier « outils », créez un script python
 `test_outils.py` dans lequel nous testerons les différentes méthodes d'importation
- Il est important de comprendre que ce sont les objets placés
 derrière le mot « `import` » qui seront utilisables dans votre
 programme.
- Le reste ne sera pas accessible.


--------------------------------------------------------------------------------

## Package - Utilisation


    !pycon
    >>> import outils
    >>> print('Pi = %f' % outils.PI)
    Pi = 3.141593
    >>> outils.booleens.xor(True, False)
    Traceback (most recent call last):
    File "/home/makina/FormationPython/test_outils.py", line 4, in <module>
    outils.booleens.xor(True, False)
    AttributeError: 'module' object has no attribute 'booleens'

Les variables et fonctions sont automatiquement chargées quand on
charge un package.

Pas les modules !


--------------------------------------------------------------------------------

## Package - Utilisation

    !python
    import outils.booleens
    print('Pi = %f' % outils.PI)
    print("xor1(True, False)=%s" % 
    outils.booleens.xor(True, False))
    Pi = 3.141593
    xor(True, False)=True

Cette fois c'est bon !

Mais c'est contraignant de devoir nommer le chemin complet d'accès à
 la fonction `xor`...


--------------------------------------------------------------------------------

## Package - Utilisation

    !python
    from outils import booleens
    print("xor(True, False)=%s" % booleens.xor(True, False))
    print('Pi = %f' % outils.PI)
    Traceback (most recent call last):
    File "/home/makina/FormationPython/test_outils.py", line 3, in <module>    
    NameError: name 'outils' is not defined


--------------------------------------------------------------------------------

## Package - Utilisation

    !python
    from outils import booleens
    import outils
    print('Pi = %f' % outils.PI)
    print("xor1(True, False)=%s" %
           booleens.xor(True, False))


Pffiou… C'est compliqué !

Rappelez-vous, seul ce qui est après « `import` » est accessible


--------------------------------------------------------------------------------

## Package - Utilisation
    
    !python
    from outils.booleens import xor as exclusive_or
    
    print("exclusive_or(True, False)=%s"  % exclusive_or (True, False))
    exclusive_or(True, False)=True
    print("xor(True, False)=%s" % xor(True, False)) 
    NameError: name 'xor' is not defined


--------------------------------------------------------------------------------

.fx: section-first-page

# Visibilité des variables




--------------------------------------------------------------------------------

## Visibilité des variables - blocs

- En Python, comme dans tout langage les variables ont une **visibilité** 
  en fonction de là où elles ont été déclarées.
- La visibilité des variables est locale au bloc les déclarant et à leurs sous-blocs.
- Les boucles et conditionnelles « `if`, `elif`, `else` », « `for` » et « `while` » 
  sont considérées comme étant dans le bloc « courant ».

--------------------------------------------------------------------------------

## Visibilité des variables - blocs

- Dans les autres cas, les variables sont **visibles dans les sous-blocs
 mais pas dans les blocs de niveau supérieur**.
- On a accès aux variables des blocs de niveau supérieur, mais pas aux
 variables des blocs de même niveau ou de niveau inférieur.
- On parle de variable **globale** quand une variable est déclarée au
 niveau du script Python.
- On parle de variable **locale** lorsque qu'une variable est déclarée au
 niveau d'un module, d'une classe, d'une fonction. Dans ce cas sa
 visibilité est locale au bloc où elle est déclarée.


--------------------------------------------------------------------------------

## Visibilité des variables - structure conditionnelle

    !python
    est_bissextile = True
    jours_annee_bissextile = 366
    jours_annee_normale = 365
    if est_bissextile:
        print("Est bissextile")
        jours_annee = jours_annee_bissextile
    else:
        print("Année normale")
        jours_annee = jours_annee_normale
    print(jours_annee)
    
    Est bissextile
    366


--------------------------------------------------------------------------------

## Visibilité des variables - structure conditionnelle

Qu'affiche ce programme ?
    
    !python
    liste_mois = ["avril", "mai", "juin", "juillet"]
    for mois in liste_mois:
        if "r" in mois:
            a_mois_avec_r = True
            break
    else:
        a_mois_avec_r = False
    print("Mois avec r ? %s " % a_mois_avec_r)

Qu'affiche-t'il si on retire 'avril' de la liste ?

--------------------------------------------------------------------------------

## Visibilité des variables - Fonctions

### Avez-vous été attentif ?
Qu'affiche ce programme ? Une erreur ?

    !python
    jours_annee_normale = 365
    jours_annee_bissextile = 366
    def affiche_jours() :
        print("Jours année normale : %s" % jours_annee_normale)
        print("Jours année bissextile : %s" % jours_annee_bissextile)
    affiche_jours()


--------------------------------------------------------------------------------

## Visibilité des variables - Fonctions

Et celui-ci ?
    
    !python
    def affecte_jours():
        jours_annee_normale = 365
        jours_annee_bissextile = 366
    affecte_jours()
    print("Jours année normale :%s" % jours_annee_normale)
    print("Jours année bissextile :%s" % jours_annee_bissextile)
    

--------------------------------------------------------------------------------

## Visibilité des variables - Fonctions

Et que se passe-t'il dans celui-ci ?

    !python
    jours_annee_normale = 365
    jours_annee = jours_annee_normale
    annee_bissextile = True
        
    def calcule_jours():
        if annee_bissextile:
            jours_annee = jours_annee_normale + 1

    calcule_jours()
    print("Jours année : %s" % jours_annee)


--------------------------------------------------------------------------------

## Visibilité des variables - Fonctions

Difficile : et que se passe-t'il dans ce script ?

    !python
    jours_annee = 365
    annee_bissextile = True
    def calcule_jours():
        if annee_bissextile:
            jours_annee += 1
            
    calcule_jours()
    print("Jours année:%s" % jours_annee)


--------------------------------------------------------------------------------

## Visibilité des variables - Fonctions

Pour *modifier* une variable globale dans une fonction ou tout autre
 bloc local, vous devez indiquer au préalable que vous souhaitez accéder
 localement à cette variable globale.
 
Pour cela vous utilisez le mot clef « `global` »
    
    !python
    jours_annee = 365
    annee_bissextile = True
    def calcule_jours():
        global jours_annee
        if annee_bissextile:
            jours_annee += 1
            
    calcule_jours()
    print("Jours année:%s" % jours_annee)


--------------------------------------------------------------------------------

## Visibilité des variables - Fonctions

- À noter qu'il existe aussi 2 fonctions :
    - `globals()` qui affiche les objets globaux au bloc courant
    - `locals()` qui affiche les objets locaux au bloc courant
- ATTENTION : si vous modifiez les objets retournés par ces fonctions
 vous modifiez les véritables variables.

<!-- -->
    !pycon
    >>> jours_annee = 365
    >>> globals()['jours_annee'] += 1   # pirate !!
    >>> jours_annee
    366
    
RAPPEL : la manipulation de variables globales est à éviter autant
que possible !


--------------------------------------------------------------------------------

## Visibilité des variables – Passage d'arguments

- Le passage d'arguments aux fonctions se fait par **référence**.
- Si vous modifiez une valeur passée en paramètre, vous modifiez sa
 valeur en dehors de la fonction.


--------------------------------------------------------------------------------

## Visibilité des variables – Passage d'arguments

### Avez-vous été attentif, très attentif ?
Que valent `jours_boulangerie` et `new_jours_boulangerie` à la fin du script ?

    !python
    semaine_boulangerie = {'ouverts': [2, 3, 4, 5, 6],
                           'fermes': [1, 7]}
    def ouvre_jour(jours, jour_ouvert):
        jours['ouverts'].append(jour_ouvert)
        jours['ouverts'].sort()
        jours['fermes'].remove(jour_ouvert)
        return jours
        
    semaine_boulangerie_noel = ouvre_jour(semaine_boulangerie, 7)
    print(semaine_boulangerie_noel)
    print(semaine_boulangerie)

Exercice : écrire le programme qui ne provoque pas d'effet de bord !


--------------------------------------------------------------------------------

## Visibilité des variables – Valeurs par défaut

- Attention aux paramètres ayant des valeurs par défaut.
- Les arguments de fonctions ayant des valeurs par défaut ne sont
 initialisés qu'une seule fois, lors du premier appel de la fonction.


--------------------------------------------------------------------------------

## Visibilité des variables – Valeurs par défaut


_Mieux connaître l'interpréteur python !_

Qu'est ce qui est affiché pour `a=` et `b=` au troisième appel ?

    !python
    def f2(a=10, b=[]):
        a += 2
        b.append(5)
        print("a=%s, b=%s, id(a)=%s, id(b)=%s" % (a, b, id(a), id(b)))
        
    f2()
    f2(100, ['toto', 'titi'])
    f2()


--------------------------------------------------------------------------------

## Visibilité des variables – Valeurs par défaut


_Mieux connaître l'interpréteur python !_

Qu'est ce qui est affiché pour `a=` et `b=` au troisième appel ?

    !python
    def f2(a=10, b=[]):
        a += 2
        b.append(5)
        print("a=%s, b=%s, id(a)=%s, id(b)=%s" % (a, b, id(a), id(b)))
        
    f2()
    f2(100, ['toto', 'titi'])
    f2()

<!-- -->

    a=12, b=[5], id(a)=10455072, id(b)=140219040322888
    a=102, b=['toto', 'titi', 5], id(a)=10455999, id(b)=140219040324872
    a=12, b=[5, 5], id(a)=10455072, id(b)=140219040322888


--------------------------------------------------------------------------------

## Visibilité des variables – Valeurs par défaut

![](images/visibilite-des-variables-valeurs-par-defaut-1.svg)


--------------------------------------------------------------------------------

## Visibilité des variables – Valeurs par défaut

![](images/visibilite-des-variables-valeurs-par-defaut.svg)

--------------------------------------------------------------------------------

## Visibilité des variables – Valeurs par défaut

### Exercice

Trouvez une façon de ré-écrire la fonction f2() pour éviter cet
 effet de bord dans le cas de la variable « b ».

*Indication: utilisez autre chose qu'un type modifiable comme valeur par
 défaut*


--------------------------------------------------------------------------------

## Variables spéciales du module

- Les modules Python possèdent par défaut différentes variables
 globales.
- Parmi celles-ci il en existe 2 très utiles :
    - `__file__` : Qui contient le nom de fichier du script/module courant
    - `__name__` : Qui contient le nom du module tel que vu par Python


--------------------------------------------------------------------------------

## Variables spéciales du module

Un exercice pour comprendre l'usage de `__name__` 

- Depuis le script « `test_outils` », trouvez la manière d'afficher
 toutes les variables globales du module « outils »
- Puis, affichez la variable « `__name__` » dans le module
 «booleens »
- Executez le script « `booleens.py` » puis « `test_outils.py` »
- Deduisez de la valeur de « `__name__` » qui est affichée dans les 2
 cas un moyen de ne plus faire afficher les tests réalisés dans
 « `booleens.py` » lorsqu'il est importé.


--------------------------------------------------------------------------------

# Plan de formation : Syntaxe et bases du langage

.fx: section-first-page

- Les types et variables
- Les fonctions
- Les modules
- **Les générateurs**
- map, filter, reduce, zip


--------------------------------------------------------------------------------

## Générateurs 

- Très souvent quand vous parcourez une séquence, la seule valeur qui
 vous intéresse, c'est la valeur en cours, pas la peine d'avoir
 toute la liste en mémoire.
- En plus, Python a quelques problèmes avec les listes d'entiers et de
 réels.
    - Elles ne sont pas forcément libérées avant la fin du programme
    - Si vous allouez 100 listes d'un million d'entiers, vous pouvez vous
     retrouver dans une situation critique avec ces 100 listes toujours en
     mémoire même si elles ne sont plus utilisées ou que vous avez appelé
     le garbage collector


--------------------------------------------------------------------------------

## Générateurs

    $ python numbers_in_list.py

<!-- -->

    !python
    # pip install psutil
    import os
    import psutil
    process = psutil.Process(os.getpid())
    for i in range(50):
        l = list(range(1000*1000))
        print("Memory usage: %d MB" % (process.memory_info()[0] / float(2 **
     20),))
 
<!-- -->

    Memory usage: 49 MB
    Memory usage: 50 MB
    Memory usage: 51 MB
    ...
    Memory usage: 80 MB
    Memory usage: 81 MB

--------------------------------------------------------------------------------

## Générateurs

- La mémoire augmente jusqu'à saturer votre PC ou croit jusqu'à une
 certaine taille
- Selon votre version de Python vous pouvez avoir des comportements
 différents avec ce programme
- Le fait d'appeler le garbage collector sera souvent sans effet, en
 raison de ce défaut.
-  <http://stackoverflow.com/questions/9617001/python-garbage-collection-fails>
-  <http://stackoverflow.com/questions/1316767/how-can-i-explicitly-free-memory-in-python/>
  


-------------------------------------------------------------------------------

## Générateurs

Pour contourner ce problème de nombreuses fonctions Python, comme
 « `range` » qui retournaient des listes d'entiers en Python 2 sont
 devenues des générateurs en Python 3
 
 
    $ python2
    Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    $ python3
    Python 3.4.0 (default, Jun 19 2015, 14:20:21)
    >>> range(10)
    range(0, 10)

En Python2, vous pouvez utiliser « xrange » pour avoir le même
comportement que le range de Python 3.


--------------------------------------------------------------------------------

## Générateurs - syntaxe

- Les générateurs sont des fonctions spéciales qui retournent leur
 résultat par *morceaux* successifs
- Elles utilisent pour cela le mot clef « `yield` »
- Cette commande permet de retourner une valeur, tout comme le mot clef
 « `return`, mais au prochain appel de la fonction son code reprendra
 l'exécution juste après le mot clef `yield`.
- C'est très particulier, mais bigrement intéressant.


--------------------------------------------------------------------------------

## Générateurs - Exemple

    !python
    def my_range(start, stop, step):
        ind = start
        
        while ind < stop:
            print("Avant yield")
            yield ind
            print("Après yield")
            ind += step

    for i in my_range(10,20,2):
        print("i = %d" % i)

<!-- -->
    Avant yield
    i = 10
    Après yield
    Avant yield
    i = 12
    Après yield
    Avant yield
    i = 14
    Après yield
    Avant yield
    i = 16
    Après yield
    Avant yield
    i = 18
    Après yield
        
--------------------------------------------------------------------------------

## Générateurs - Exercices

- Écrire un générateur de la suite de fibonacci qui prend en paramètre un nombre à ne pas dépasser.

- Affectez ce générateur à une variable. Affichez cette variable deux fois : quel problème pouvez-vous
 rencontrer ?


--------------------------------------------------------------------------------

## Générateurs : générateurs par compréhension


    !pycon
    >>> (x ** 2 for x in range(10))
    <generator object <genexpr> at 0x7f77a38547d8>

Pour tester les générateurs, vous pouvez les caster en liste
    
    !pycon
    >>> list((x ** 2 for x in range(10)))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


--------------------------------------------------------------------------------

## Lambda expressions

- Le mot clef « `lambda` » permet de définir des **fonctions  anonymes**
 dont le code généralement tient sur une ligne.
- Une fonction anonyme est une fonction qui n'a pas de nom. 
On ne peut donc pas l'appeler explicitement.
- Généralement on se sert de fonctions `lambda` pour passer des
 fonctions comme arguments d'autres fonctions

<!-- -->
    !pycon
    >>> f = lambda a,b : a+b
    >>> f(4)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: <lambda>() missing 1 required positional argument: 'b'
    >>> f(4,5)
    9


--------------------------------------------------------------------------------

## Lambda expressions

- Vu comme cela, elles ne présentent pas immédiatement un grand
  intérêt.
- Mais elles permettent de faire des choses plus sophistiquées
- Ou d'avoir des écritures très concises

<!-- -->
    !pycon
    >>> def make_incrementor(n):
    ...     return lambda x: x + n
    ...
    >>> f = make_incrementor(42)
    >>> f(0)
    42
    >>> f(1)
    43


--------------------------------------------------------------------------------

## map, filter et reduce

La fonction `map` permet d'appliquer une fonction aux éléments
d'une liste et retourne le résultat sous forme d'un générateur
(d'une liste en Python 2)

    !pycon
    >>> map(lambda x: x**2, range(10))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Mais vous saviez déjà le faire autrement...
    
    !pycon
    >>> gen = (x ** 2 for x in range(10))
    >>> list(gen)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


--------------------------------------------------------------------------------

## map, filter, reduce

### Exercice

Pouvez vous expliquer ce que fait ce code ?

    !python
    def square(x):
         return (x**2)
    
    def cube(x):
         return (x**3)
    
    funcs = [square, cube]
    for r in range(5):
        value = map(lambda func: func(r), funcs)
        print(list(value))


--------------------------------------------------------------------------------

## map, filter, reduce

La fonction « `filter` » quant-à elle applique une fonction à une
liste de valeurs et ne retourne que celles pour lesquelles le résultat
vaut `True`. 

Elle retourne un générateur.

    !pycon
    >>> mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> mult3
    <filter object at 0x7f9861d0f588>
    >>> for i in mult3:
    ...   print(i)
    ...
    3
    6
    9


--------------------------------------------------------------------------------

## map, filter, reduce

- La fonction « `reduce` » est elle aussi assez originale.
- On peut traduire `reduce` par "consolidation".
- Elle prend comme premier argument une fonction acceptant deux
 paramètres, en second argument une liste de valeurs, en troisième
 argument une valeur initiale (facultative).
- Puis elle applique la fonction aux 2 premiers éléments de la liste,
 puis au résultat de la fonction et à l'élément suivant et ainsi de
 suite, pour retourner le résultat du dernier appel.

<!-- -->

    !python
    from functools import reduce  # nécessaire en python 3 seulement
    def consolide_somme(consolidation_precedente, valeur):
        return consolidation_precedente + valeur

    print(reduce(consolide_somme, [1, 2, 3, 4, 5], 0))
    15


--------------------------------------------------------------------------------

## map, filter, reduce

- Certains les adorent, d'autres les détestent.
- Elles apportent une plus grande concision dans l'écriture de vos
  programmes.
- Mais aussi une plus grande difficulté pour les lire et les
 comprendre... D'où les 2 écoles.
- Elles permettent une technique de programmation appelée
 **closure** ou **fermeture** ou **clotûre**.
<https://fr.wikipedia.org/wiki/Fermeture_%28informatique%29>
- Enfin, cet article de stackoverflow résume bien leur intérêt et
 cette guerre des écoles
<http://stackoverflow.com/questions/890128/why-python-lambdas-are-useful>
- <http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php> 


--------------------------------------------------------------------------------

## zip

zip produit des tuples qui combinent les éléments de plusieurs *itérables*.

    !pycon
    >>> list(zip(range(5), "hello"))
    [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

* le premier tuple contient les premiers éléments de chaque itérable
* le second tuple contient les seconds éléments
* et ainsi de suite suite jusqu'à ce qu'on ait consommé tous les éléments d'un des itérables

<!-- -->

    !pycon
    >>> list(zip(range(100), "bye"))
    [(0, 'b'), (1, 'y'), (2, 'e')]


--------------------------------------------------------------------------------
