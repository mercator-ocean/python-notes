
# Plan de formation

- Présentation & Historique
- Syntaxe et bases du langage
- **Approche Orientée Objet**
- Programmation Orientée Objet en Python
- Librairies standard
- Outils de qualité et tests


--------------------------------------------------------------------------------

.fx section-first-page

# Approche Orientée Objet

Découverte par l'exemple.

![](images/poo-animal.png)



--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

### Soit le problème suivant :

![](images/approche-orientee-objet.png)

Vous venez de gagner à l'Euromillions le Jackpot de tous les temps !

--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

- Vous avez décidé d'acheter une île et d'y faire la fête avec tous
  vos amis, notamment vos collègues de formation
- Mais vous devez vous rendre du continent à l'île et pour cela vous
  avez opté pour 2 moyens
    - Par mer, avec le beau voilier que vous venez juste d'acquérir
    - Par le pont que vous venez de faire construire et qui relie le
      continent à votre île afin de pouvoir vous y rendre avec votre Ferrari
      ou Tesla sans la salir dans le sable à marrée basse.
- Et vous avez décidé de créer un programme informatique pour
  cela...


--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

Et pour cela, vous avez décidé de créer votre propre
 société de services en Python !!

![](images/go.png)

Ce programme sera votre première création dans cette nouvelle entreprise…

Le plan que vous avez dessiné se trouve sur la page suivante.


--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

<!-- -->

--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

L'algorithme de votre programme est fort simple :

- Sélectionner un véhicule (voiture ou voilier)
- Démarrer le véhicule
- Avancer avec le véhicule jusqu'à destination
- Arrêter le véhicule
- Faire la fête avec les amis

![](images/pourquoi-utiliser-python.png)


--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

![](images/poo-exemple-algo.png)


--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

- Comme vous êtes aguerri à la programmation procédurale et que vous
 avez un très bon esprit d'analyse, vous avez remarqué que vous
 pourriez faire une fonction pour traiter chaque action
- Vous avez aussi remarqué, que, quelque soit le type de véhicule,
 vous pourriez faire une fonction `suivre_itineraire` qui serait la
 même quel que soit le type de véhicule :
    - Démarrer
    - Avancer jusqu'à destination
    - Arrêter
    - Mais vous êtes embêté...
    
<!-- -->
![](images/comme-vous-etes-aguerri-a-la-programmation-procedurale-et-que-vous-avez-un-tres-bon-esprit-d.png)

--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

Vous avez relevé que chaque véhicule possède des actions qui lui
 sont propres :
 
### Démarrer

- Pour un bateau il faut lever l'ancre, larguer les amarres, hisser la
 voile
- Pour une voiture il faut tourner la clef de contact et enlever le
 frein à main

### Avancer
- Pour un voilier cela se fait sur la mer, en zigzaguant le vent dans le
 dos
- Pour une voiture cela se fait sur la route en respectant le code de la
 route

### Arrêter
- Pour un voilier il faut ranger la voile, jeter l'ancre, attacher les
 amarres
- Pour une voiture il faut couper le moteur et mettre le frein à main

--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

- Maintenant que vous êtes initié aux fonctions en Python, vous vous
 dites que vous pourriez implémenter ce programme de 2 manières :
    - Soit en créant 3 fonctions `demarrer()`, `avancer()` et `arreter()`,
     prenant comme argument un véhicule puis dans chaque fonction tester le
     type du véhicule pour exécuter la bonne action selon ce dernier
    - Soit en créant une fonction `demarrer()`, `avancer()` et `arreter()` par
     type de véhicule, par exemple `demarrerVoiture()`, `demarrerBateau()` et en
     exécutant juste les bonnes actions dans chaque fonction
- Quelle est votre solution préférée, et pourquoi ?

![](images/poo-exercice.png)


--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

Dans les 2 cas vous vous retrouvez à soit :

- Effectuer des tests en double dans chaque fonction et avoir un code deux
  fois plus long par fonction
- Doubler le nombre de fonctions


--------------------------------------------------------------------------------

## POO – Découverte par l'exemple

- Vous avez noté que :
    - La première solution permet de n'avoir qu'une seule fonction
      `suivre_itineraire`
- Vous avez cependant choisi la seconde :
    - Vous vous dites que séparer les fonctions sera plus pratique si plus
      tard les comportements d'un des véhicules changent
    - Vous pourrez réutiliser les fonctions de déplacement d'un véhicule
      donné dans d'autres programmes sans devoir importer les comportements
      des autres, par exemple pour :
        - participer à la course du Rhum avec les fonctions « bateau »
        - participer aux 24h du mans avec les fonctions « voiture »
    - Vous n'aimez pas avoir plein de `if` partout
- C'est la solution implémentée par le formateur et vous comptez-bien
 essayer de la lui racheter à bon prix afin d'aller plus vite faire la
 fête.


--------------------------------------------------------------------------------

## Organigramme final

<!-- -->

![](images/poo-exemple-algo-definitif.png)

--------------------------------------------------------------------------------

## POO – Découverte par la pratique

### Exercice

- Le programme `approche_procedurale` qui vous est proposé
 implémente cette étude de cas.
- Exécutez-le, étudiez-le et formulez quelques propositions
 d'évolution ou critiques dans l'hypothèse d'y ajouter d'autres types
 de véhicules comme :
    - Un avion
    - Un vélo
    - Un hélicoptère
    - Une trottinette
    - ...

![](images/exercice-2.png)

--------------------------------------------------------------------------------

# POO – Historique

- La programmation orientée objet a vu ses fondations puisées dans ces
 mêmes difficultés que vous venez de soulever.
- Mais avant la programmation procédurale c'était encore bien plus
 laborieux...

![](images/exercice-1.png)


--------------------------------------------------------------------------------

## POO – Historique

### Fin des années 1950 - GOTO

- Avant l'apparition de la programmation par fonctions, dite
 « procédurale », à ne pas confondre avec la programmation
 fonctionnelle, les fonctions n'existaient
 pas…<br />
<https://fr.wikipedia.org/wiki/Paradigme_%28programmation%29> 
- Les langages conçus sur ce mode utilisaient généralement une
 instruction nommée `GOTO` pour éviter l'exécution de certaines
 instructions<br />
<https://fr.wikipedia.org/wiki/Goto_%28informatique%29>
- Le Fortran (1954), puis le COBOL(1959) et« le BASIC » en sont les
 précurseurs (en dehors de l'assembleur)

<!-- -->

    !basic
    10 PRINT 'ENTREZ UN CHIFFRE '
    20 LET $A = INPUT 
    30 IF $A % 2 <> 0 THEN GOTO 60
    40 PRINT $A + ' EST PAIR'
    50 EXIT
    60 PRINT $A + 'EST IMPAIR'


--------------------------------------------------------------------------------

## POO – Historique

### 1960/70 – Les fonctions

- Le tout premier langage a avoir introduit la notion de fonctions est
 l'ALGOL, en 1958.<br />
<https://fr.wikipedia.org/wiki/Programmation_proc%C3%A9durale> 
- Mais c'est avec l'arrivée de langages comme Fortran (1958),
 Pascal(1970) et C(1972) que la programmation procédurale a vraiment
 pris son envol et permis de quasiment éradiquer le GOTO de nos
 programmes
- Ces langages ont aussi apporté le typage de données, offrant ainsi
 une plus grande rigueur dans vos programmes.
- Les fonctions ont apporté de nouvelles techniques de programmation
 très avancées et prometteuses, comme la «récursivité»
- Plus de facilités pour certaines choses...
- Mais les programmes avaient toujours tout un tas de problèmes
 récurrents...


--------------------------------------------------------------------------------

## POO – Historique

### Années 80/2000

- Conception inadaptée...
- Code patché...
- Cycle de Test sans fin...
- Mauvaise Communication...
- Dépassement des coûts et des  délais...
- Exigences Floues...
- Mauvaise gestion des risques...
- Evolution compliquée à réaliser...
- Mauvaise Traçabilité...


--------------------------------------------------------------------------------

## POO – Historique

### Les approches traditionnelles ne suffisent plus


- Les méthodes traditionnelles avec le cycle en V,
 montrent leurs limites
- Tout un tas de méthodologies de mesure de la qualité du code voient
 alors le jour :
Cocomo, Méthode B, Point de fonction, Métriques
 d'Halstead…<br />
<https://fr.wikipedia.org/wiki/M%C3%A9trique_%28logiciel%29> 
- La qualité logicielle et le génie logicie affirment alors leur
 autorité <br />
<https://fr.wikipedia.org/wiki/Qualit%C3%A9_logicielle><br />
 <https://fr.wikipedia.org/wiki/G%C3%A9nie_logiciel> <br />
- Un nouveau modèle de conception émerge : **le modèle objet**<br />
Et avec lui de nouvelles méthodes de conception

![](images/les-approches-traditionnelles-ne-suffisent-plus.png)

--------------------------------------------------------------------------------

## POO – Historique

![](images/conception-objet.png)

--------------------------------------------------------------------------------

### POO - Historique

La **Programmation Orientée Objet** voit le jour dans le début des
 années 1960 avec les travaux des Norvégiens Ole-Johan Dahl et Kristen
 Nygaard.

Ils sont complétés par les travaux d'Alan Kay dans les années 1970.

Elle « consiste en la définition et l'interaction de briques
 logicielles appelées objets ; **un objet représente un concept, une
 idée ou toute entité du monde physique**, comme une voiture, une
 personne ou encore une page d'un livre. Il possède **une structure
 interne et un comportement**, et il sait interagir avec ses pairs. »,
 *Wikipédia*.<br />

 <https://fr.wikipedia.org/wiki/Programmation_orient%C3%A9e_objet> 



--------------------------------------------------------------------------------

### POO - Historique

- Les principes de la POO ont concrètement vu le jour avec le langage
 Simula-67.
- Mais c'est le langage **SmallTalk** qui réussi véritablement à mettre
 en exergue ce nouveau concept auprès des informaticiens.
- Enfin, c'est avec l'arrivée de langages comme C++ (1983),
 Python(1990) et Java(1995) que l'industrie s'empare du concept pour en
 faire son cheval de bataille.
- Avec la programmation objet, de nouvelles méthodes de conception
 voient le jour :
    - Merise Objet
    - BOOCH, 
    - OOSE
    - Unified Process (USDP)
 
 Mais c'est **UML** qui s'imposera quasi unanimement dans l'industrie<br />
<https://fr.wikipedia.org/wiki/UML_%28informatique%29>


--------------------------------------------------------------------------------

### POO – Historique – Méthodes agiles

Enfin, tout comme les méthodes de conception, de nouvelles pratiques
 de programmation ont vu le jour ces dernières années sous le terme de
 méthodes agiles :
 
- XP, eXtreme Programming
- Kanban
- Scrum

Elles visent à simplifier le cycle de vie d'un logiciel en favorisant
 les interactions entre les intervenants et supprimant de nombreuses
 lourdeurs procédurales afin de faciliter le changement dans un
 programme

![](images/poo-historique-methodes-agiles.png)

--------------------------------------------------------------------------------

### POO – Finalement

Finalement la POO, accompagnée de bonnes méthodes de conception et
 d'une gestion de projet agile aura réussi à gagner son pari :

- Des programmes plus simples
- Plus maintenables
- Plus évolutifs
- Plus fiables
- Moins coûteux
- Plus vite développés

L'incroyable réconciliation des utilisateurs et décideurs avec les
 informaticiens a lieu… 


--------------------------------------------------------------------------------

## POO – Quelques termes

Quelques termes de **qualité logicielle** que vous pourrez rencontrer :

- **L'exactitude** : c'est l'aptitude d'un logiciel à fournir le
 résultat attendu, autrement dit, à répondre correctement au cahier
 des charges.
- **La robustesse** : c'est l'aptitude à bien réagir lorsque l'on
 s'écarte des conditions normales d'utilisation
- **L'extensibilité** : c'est la facilité avec laquelle un programme
 pourra être adapté pour répondre des demandes d'évolution  
- **La réutilisabilité** : c'est la possibilité d'utiliser certaines
 parties du logiciel dans un autre programme pour répondre à d'autres
 besoins.
- **La portabilité** : c'est l'aptitude d'un logiciel à fonctionner dans
 un environnement matériel ou logiciel différent de son environnement
 initial
- **L'efficience/performance** :  c'est le rapport entre la quantité de
 ressources utilisées et la quantité de résultats délivrés
Temps de réponse, ressources utilisées (mémoire, disque, ...)


--------------------------------------------------------------------------------

# POO - Principes

![](images/poo-monde-animal.png)

- L'idée principale de la programmation Orientée Objet est d'essayer
 de **classifier** les types de données de votre programme en les regroupant
 selon leurs points communs.
- Et créant des sous-ensembles dès que des objets partagent des
 **données ou comportements communs**.
- Exactement comme dans le cas des classifications animales et
 végétales.


--------------------------------------------------------------------------------

## POO - Principes

- Dans notre exemple nous avons un type de données « Véhicule »
 qui se décompose en 2 sous-types : « Voiture » et « Bateau »
- Tous les véhicules, quel que soit leur type, possèdent des attributs
 communs :
    - Identifiant (plaque d'immatriculation pour la voiture, nom pour le bateau)
    - Longueur, hauteur, largeur, couleur, etc.
- Les véhicules possèdent aussi des comportements communs
    - Demarrer, 
    - Avancer, 
    - Arreter
    - Suivre itinéraire
- On peut faire des choses similaires avec ("**l'interface**") mais ils le
 font différemment ("**l'implémentation**")


--------------------------------------------------------------------------------

## POO - Principes

- Chaque sous-type de Véhicule possède aussi des **attributs** qui lui
 sont propres :
    - Pour une voiture : nombre de portes, quantité d'essence
    - Pour un bateau : nombre de voiles pour un bateau, état de ces voiles
 (levée / baissée...)
- Chaque sous type de Véhicule possède aussi des **comportements** qui lui
 sont propres
    - Soit des comportements communs mais qui sont réalisés de manière
     particulière pour ce sous type (un bateau n'avance pas comme une
     voiture)
    - Soit des comportements propres :
        - Passer le contrôle technique pour une voiture,
        - Hisser la voile pour un bateau.
 
La **Programmation Orientée Objet** (POO) permet de représenter toutes ces choses….


--------------------------------------------------------------------------------

## POO - Principes

<!-- -->
![](images/poo-patates.png)

--------------------------------------------------------------------------------

## POO - Principes

- On définit au niveau de chaque type/ensemble tout ce qui est
 commun à tous les sous-types.
- On ne redéfinit au niveau de chaque sous-type que ce qui est
 réalisé particulièrement pour ce sous-type ou unique à celui-ci.

Que ce soit au niveau des **attributs** (données) ou des **comportements**
 (actions).

Cela s'appelle la **spécialisation**.

![](images/poo-specialisation.png)

--------------------------------------------------------------------------------

## POO - Principes

<!-- -->
![](images/poo-patates-details.png)

--------------------------------------------------------------------------------

## POO - Terminologie

Le fait de regrouper dans une même structure de données, le type de
 la donnée, ses attributs et ses comportements s'appelle
 **l'encapsulation**.

En notation **UML** la symbolique est la suivante :

![](images/poo-uml.png)


--------------------------------------------------------------------------------

## POO - Terminologie

- Définir un sous-ensemble dans un ensemble d'objets s'appelle la
 **spécialisation**.
- Un sous ensemble est aussi appelé un sous-type, ou une **sous-classe**.
- Une sous-classe bénéficie automatiquement de tout ce qui est défini
 dans sa classe parent. On appelle cela l'**héritage**.
- Une sous-classe a uniquement besoin de définir ce qui lui est
 propre : nouveaux attributs et nouvelles méthodes ainsi que les
 actions personnalisées.
- Redéfinir une action commune à tous les objets dans une sous-classe,
 autrement dit, personnaliser une action s'appelle le polymorphisme ou la
 **surcharge**.


--------------------------------------------------------------------------------

## POO - Terminologie


![](images/poo-uml-vehicule.png)


--------------------------------------------------------------------------------

## POO - Terminologie

- Quand une classe B hérite d'une autre classe A on dit que :
    - La classe A est la **classe parent** de la classe B
    - La classe B est une **classe fille** de la classe A
    - La classe B **hérite** de A
    - La classe B est une **classe dérivée** de la classe A
    - La classe B est une **sous-classe** de la classe A
    - La classe A est une **super-classe**
- Une variable issue d'une classe est appelée « **instance** » de la classe.

![](images/poo-terminologie.png)

--------------------------------------------------------------------------------

.fx section-first-page

# Python et la POO 

## Découverte par l'exemple



--------------------------------------------------------------------------------

## POO en Python – Création d'une classe

Pour définir une **classe** en Python, on utilise le mot clef
  `class` suivi du nom de la classe.
  
Tout comme pour les fonctions, tout ce qui est indenté après cette
  déclaration fera partie de la classe

    !python
    class Vehicule:
        pass

Pour définir des **attributs** de classe on initialise des variables dans
 le bloc de code de la classe

    !python
    class Vehicule:
        identifiant = None
        couleur = 'blanc'
        
Pour créer une **instance** de classe, on crée une variable en
appelant la classe comme s'il s'agissait d'une fonction

    !python
    v1 = Vehicule()


--------------------------------------------------------------------------------

## POO en Python – Attributs de classe

Attention, les attributs de classe ne sont peut-être pas ce que vous
 croyez…

_Quelle sera la couleur des 3 véhicules v1, v2 et v3 à la fin
de ce programme ?_
 
    !python
    class Vehicule:
        identifiant = None
        couleur = 'blanc'    
    
    v1 = Vehicule()
    v2 = Vehicule()
    # Je repeins v1 en Rouge
    v1.couleur = 'rouge'
    # Maintenant la couleur par défaut des véhicules sera le bleu
    Vehicule.couleur = 'bleu'
    v3 = Vehicule()
    print("Couleur de v1: %s" % v1.couleur)
    print("Couleur de v2: %s" % v2.couleur)
    print("Couleur de v3: %s" % v3.couleur) 

--------------------------------------------------------------------------------

## POO en Python – Attributs de classe

_Quelle sera la couleur des 3 véhicules v1, v2 et v3 à la fin de ce programme ?_


    !python
    class Vehicule:
        identifiant = None
        couleur = 'blanc'    
        
    v1 = Vehicule()
    print("Couleur de v1: %s" % v1.couleur)
    v2 = Vehicule()
    print("Couleur de v2: %s" % v2.couleur)
    v1.couleur = 'rouge' # Je repeins v1 en Rouge
    print("Couleur de v1: %s" % v1.couleur) # rouge
    print("Couleur de v2: %s" % v2.couleur) # blanc, semble logique
    Vehicule.couleur = 'bleu' # la couleur par défaut des véhicules sera le bleu
    v3 = Vehicule()
    print("Couleur de v1: %s" % v1.couleur)
    print("Couleur de v2: %s" % v2.couleur)
    print("Couleur de v3: %s" % v3.couleur)

<!-- -->    
    Couleur de v1: blanc
    Couleur de v2: blanc
    Couleur de v1: rouge
    Couleur de v2: blanc
    Couleur de v1: rouge
    Couleur de v2: bleu
    Couleur de v3: bleu


--------------------------------------------------------------------------------

## POO en Python – Attributs de classe

C'est déroutant n'est-ce pas ?

On se serait attendu à ce que les 3 véhicules soient bleus ou que v2 reste blanc, 
mais pas vraiment à ce résultat.

### Que s'est-il passé ?

Quand vous définissez des attributs dans une classe, ce sont des
 **attributs de classe**, c'est à dire qu'ils ne sont pas spécifiques pour
 chaque instance, mais **partagés entre toutes les instances**.

C'est l'équivalent du mot clef `static` en C++ et Java.

Un peu comme les variables locales dans une fonction, pour qu'un
 attribut soit considéré comme **un attribut d'instance**, il convient de
 l'affecter à l'instance :
    
    !python
    v1.couleur = 'rouge'    


--------------------------------------------------------------------------------

## POO - Attributs de classe et d'instance

Quand vous créez une **instance** de la **classe** `Vehicule`, telle que
 définie précédemment, vous créez juste une **variable** de ce **type**.

Quand vous écrivez `print(v1.couleur)`, Python procède comme suit :

- Il regarde si un attribut `couleur` a été affecté localement
 à `v1`
    - Si oui, il retourne cet attribut d'instance
- Sinon, il regarde si la classe de `v1` possède un tel attribut
    - Si oui, il retourne sa valeur
    - Si non, il génère une erreur


--------------------------------------------------------------------------------

## POO – Attributs de classe et d'instance


![](images/mro-1.png)

----------------------------------------------------------------

## POO – Attributs de classe et d'instance

![](images/mro-2.png)


--------------------------------------------------------------------------------

## POO – Attributs de classe et d'instance

### Questions :

- Aurait-on pu affecter un attribut à `v1` qui ne soit pas un attribut de
 la classe Vehicule ?
- Doit-on affecter manuellement chaque attribut de la classe à chaque
 instance créée pour qu'il puisse avoir une valeur spécifique à
 l'instance ?
 
Quid s'il y en a 50, ce n'est pas très utilisable...

**À quoi servent les attributs de classe ?**


--------------------------------------------------------------------------------

## POO – Attributs de classe et d'instance

**Aurait-on pu affecter un attribut à v1 qui ne soit pas un attribut de
 la classe Vehicule ?**

Oui, évidemment… Il n'y a que rarement besoin
 de partager des attributs entre instances.

Mais Python va plus loin, il vous permet de créer des moutons à 5
 pattes ou des trèfles à 4 feuilles...

    !python
    v1.nb_portes = 5
    print(dir(v1))
    print(dir(v2))
    [... ,'couleur', 'identifiant', 'nb_portes']
    [... ,'couleur', 'identifiant']

- Dans ce cas, l'instance v1 possède un attribut que ne possèdent pas
 les autres instances.
- Pour les puristes de l'objet, c'est une hérésie
- Pour les autres c'est plutôt cool.
La réalité n'étant jamais
 parfaite, c'est effectivement pratique...


--------------------------------------------------------------------------------

## POO en Python – Constructeur

**Doit-on affecter manuellement chaque attribut de la classe à chaque
 instance créée pour qu'il puisse avoir une valeur spécifique à
 l'instance ?**
  
**Non, évidemment… Sinon ce serait ingérable**

- Pour cela il existe une fonction spéciale, nommée `__init__`
- Elle est appelée implicitement par Python chaque fois que vous créez
 une instance
- On appelle ce type de fonction un **constructeur**
- Elle permet d'initialiser votre instance lors de sa création avec des
 valeurs par défaut
- Le constructeur peut accepter des paramètres.
    - Son premier paramètre, obligatoire, représente l'instance. Par
      convention il est nommé `self`. C'est l'équivalent de
      `this` en Java et C++
- Contrairement à d'autres langages comme Java et C++, Python n'accepte
 qu'un seul constructeur


--------------------------------------------------------------------------------

## POO en Python – Constructeur

    !python
    class Vehicule:
        
        # Attribut directement sous la classe = attribut de classe 
        # = attribut statique
        couleur = 'blanc'
        
        def __init__(self, couleur=None, identifiant=None):
            self.identifiant = identifiant
            if couleur is None:
                # Si paramètre couleur = None, on utilise la couleur de la classe
                self.couleur = Vehicule.couleur
            else:
                # On affecte à l'attribut couleur la valeur du paramètre couleur
                self.couleur = couleur
                
    v4 = Vehicule()
    v5 = Vehicule(identifiant='1024 AB 02', couleur='vert')
    
<!-- -->

    v4: identifiant=None, couleur=blanc
    v5: identifiant=1024 AB 02, couleur=vert


--------------------------------------------------------------------------------

## POO – Attributs de classe et d'instance

### A quoi servent les attributs de classe ?

- Ils peuvent servir à définir des constantes utiles/partagées par
 toutes les instances : par exemple `Moto.nombre_roues = 2`
- On les utilise souvent pour créer des compteurs permettant de
 connaître le nombre d'instances créées dans une classe.
- Ils peuvent aussi servir à définir des valeurs par défaut pour
 certains attributs de la classe.

--------------------------------------------------------------------------------

## POO – Attributs de classe et d'instance

### Exercices

- Utilisez les attributs de classe pour compter le nombre de Vehicules
 créés dans un attribut nommé `nb_vehicules_crees`.
- Affichez la valeur de cet attribut après avoir créé quelques
 instances.


--------------------------------------------------------------------------------

## POO en Python – Méthodes

Les **méthodes** d'une classe sont les actions que peuvent réaliser les
 objets de la classe, ou plus précisément **les actions qui peuvent
 être appliquées aux instances de la classe**.

- Pour définir une méthode, on crée **une fonction dans la classe**
- Le premier paramètre de la fonction représente l'instance courante
 sur laquelle s'applique la fonction
    - Par convention ce paramètre est nommé `self`
- Il existe des méthodes de statiques en Python.

<https://docs.python.org/3/library/functions.html#staticmethod>


--------------------------------------------------------------------------------

## POO en Python – Méthodes

Pour invoquer une méthode sur une instance on écrit : `instance.methode(params)`

Le paramètre `self` ne doit pas être passé en argument.

<!-- -->

    !python
    class Vehicule:
    
        couleur = 'blanc'
        
        def afficher(self):
            print("Identifiant: %s" % self.identifiant)

    v4 = Vehicule()    
    v4.afficher()

--------------------------------------------------------------------------------

## POO en Python – Méthodes

Écrire

    !python
    v1.avancer(distance=10)

est équivalent à écrire

    !python
    Vehicule.avancer(v1, distance=10)

D'ailleurs les 2 syntaxes sont autorisées.


--------------------------------------------------------------------------------

## POO en Python – Méthodes spéciales

Il existe tout un tas de **méthodes spéciales** en Python.

Ces méthodes permettent de personnaliser les comportements des
 objets. 

Par exemple, d'utiliser les **opérateurs** mathématiques '+, -, *, /'
 entre des objets de votre classe :
    
    !python
    limousine = voiture1 + voiture2 

Ou encore de convertir automatiquement votre instance en chaîne de
 caractères lorsque vous voulez l'afficher:

    !python
    print('Ma voiture est :%s' % vehicule1)

Ces méthodes sont toutes celles qui sont encadrées par des double
 *underscore* (`__`) lorsque vous appelez la fonction `dir` sur
 votre objet.
 


--------------------------------------------------------------------------------

## POO en Python – Méthodes spéciales 

Parmi ces méthodes, les plus utilisées sont:

- `__str__` : pour convertir votre objet en chaine
Exemple : `print("mon objet :%s" % mon_objet)`
- `__bool__` : (`__nonzero__` en Python 2)
permet de savoir si votre objet est évalué comme valant `True` ou `False` dans
 une expression booléenne
- `__del__` : le **destructeur**. Cette méthode est appelée quand votre objet est
 détruit.
Exemple : `del v1` ou `v1 = None`
- `__add__`, `__sub__`, `__mul__` : pour utiliser les
 opérateurs mathématiques `+`, `-` et `*` entre 2 objets

Vous pouvez toutes les retrouver ici :<br />
<https://docs.python.org/3/reference/datamodel.html> 


--------------------------------------------------------------------------------

## POO en Python – Méthodes

### Exercices

#### Exercice 1
- Définissez une méthode `afficher` qui affiche tous les attributs d'un véhicule.
- Implémentez la méthode `__str__` pour qu'elle renvoie
 l'identifiant de votre véhicule.<br /> 
 Utilisez-la dans la méthode `afficher`.

#### Exercice 2 :
- Ajoutez un attribut de classe `nb_vehicules_en_service` qui
 compte le nombre d'instances actives de la classe
- Ajoutez un attribut d'instance qui indique le numéro d'ordre de
 création de chaque véhicule

#### Exercice 3 :
- Implémentez les méthodes `demarrer`, `avancer`,
 `arreter` et `suivre_itinéraire` de la classe `Vehicule` en
 vous inspirant de leur version procédurale.


--------------------------------------------------------------------------------

## POO en Python - Héritage

Pour indiquer qu'une classe **hérite** d'une autre classe, on liste entre
 parenthèses après le nom de la classe le nom de
 sa classe parent.

    !python
    class Voiture(Vehicule):


Une classe peut hériter de plusieurs classes. C'est l'**héritage multiple**.
Elles sont alors séparées par des virgules :

    !python
    class VoitureAmphibie(Voiture, Bateau):

Lorsqu'une classe hérite d'une autre classe, elle dispose
 instantanément de toutes ses méthodes et attributs, sans qu'il soit
 nécessaire de les redéfinir dans la classe fille.


--------------------------------------------------------------------------------

## POO en Python - Héritage

    !python
    class Vehicule:
    
        couleur = 'blanc'
        
        def __init__(self, couleur=None, identifiant=None):
            self.identifiant = identifiant
            if couleur is None:
                self.couleur = Vehicule.couleur
            else:
                self.couleur = couleur
                
        def afficher(self):
            print("Identifiant: %s" % self.identifiant)
            print("Couleur: %s" % self.couleur)
                
    class Voiture(Vehicule):
        pass

    voit1 = Voiture()
    voit2 = Voiture("rouge", "2048 cd 04")
    voit2.afficher()

<!-- -->
    
    Identifiant: 2048 cd 04
    Couleur: rouge


--------------------------------------------------------------------------------

## POO en Python – Héritage, surcharge

Pour modifier le comportement d'un objet dans une classe fille vous
 devez **redéfinir** la méthode de cet objet dans la **classe dérivée**.

- Si vous redéfinissez une méthode dans une classe fille, c'est cette
 méthode qui sera appelée au lieu de celle de la classe parent.
- Vous pouvez toujours faire référence à la méthode de la classe
 parent en l'appelant directement via le nom de la classe
 parent. Exemple : `Vehicule.afficher(v1)`.
- Ou via le mot clef `super`
    - `super().afficher()` (Python 3)
    - `super(Voiture, self).afficher()` (Python 2 et 3)
- Le mot clef `super` est préférable à l'appel par le nom de la
 classe parent comme nous le verrons.


--------------------------------------------------------------------------------

## POO en Python – Héritage, surcharge

Personnalisons le constructeur des voitures pour qu'il accepte un
 nouveau paramètre : le nombre de portes.
     
     !python
     class Voiture(Vehicule):
        def __init__(self, nb_portes=5):
            self.nb_portes = nb_portes
        
     voit1 = Voiture()
     voit2 = Voiture("rouge", "2048 cd 04")
     voit2.afficher()
     
<!-- --> 

    !pytb
    Traceback (most recent call last):
      File "/home/makina/FormationPython/poo-initiation.py", line 25, in <module>
        voit2 = Voiture("rouge", "2048 cd 04")
    TypeError: __init__() takes from 1 to 2 positional arguments but 3 were given



--------------------------------------------------------------------------------

## POO en Python – Héritage, surcharge

**Que s'est-il passé ?**

- Nous avons redéfini le constructeur dans la classe `Voiture`.
- Python appelle maintenant ce dernier quand il crée une nouvelle
 `Voiture` car la fonction `__init__` existe maintenant dans la
 classe `Voiture`
- Auparavant il cherchait la fonction `__init__` dans la classe
 Voiture, et ne la trouvant pas il utilisait celle de la classe parent
 `Vehicule`
- La nouvelle définition du constructeur `__init__` n'appelle pas
 implicitement sa version dans la classe parent et ne définit qu'un seul
 paramètre, `nb_portes`.
- Python génère donc une erreur sur la création de la seconde voiture
 car un paramètre de trop est passé au constructeur qui n'accepte plus
 qu'un nombre de portes dans sa version actuelle.


--------------------------------------------------------------------------------

## POO en Python – Héritage, surcharge

Pour corriger cela nous pouvons ajouter 2 nouveaux paramètres au
 constructeur de la classe `Voiture` : ceux de la classe `Vehicule`
 
    !python
    class Voiture(Vehicule):
        def __init__(self, nb_portes=5, couleur=None, identifiant=None):
            self.nb_portes = nb_portes
            # copie du code de la classe Vehicule
            self.identifiant = identifiant
            if couleur is None:
                self.couleur = Vehicule.couleur
            else:
                self.couleur = couleur
                
    voit1 = Voiture()
    voit2 = Voiture("rouge", "2048 cd 04")
    voit2.afficher()
    
**Mais c'est une très mauvaise idée :**

- A quoi sert la programmation objet si nous dupliquons le code de la
 classe parent ?
- Si la classe parent accepte 50 attributs (poids, longueur, hauteur,
 …) faut-il vraiment tous les reprendre ?


--------------------------------------------------------------------------------

## POO en Python – Héritage, surcharge

Pour ne pas dupliquer il convient d'**appeler explicitement le
 constructeur de la classe parent** en début de notre constructeur pour
 être certain que tous les attributs de celle-ci sont bien initialisés
 au cas ou nous en aurions besoin dans l'initialisation de ceux de la
 classe fille.

    !python
    class Voiture(Vehicule):
        def __init__(self, nb_portes=5, couleur=None, identifiant=None):
            super().__init__(couleur, identifiant)
            #super(Voiture, self).__init__(couleur, identifiant) Python2
            #Vehicule.__init__(self, couleur, identifiant)
            self.nb_portes = nb_portes


La syntaxe utilisant `super` est préférable à celle utilisant `Vehicule` :

- `super` indique d'appeler la classe parent de `Voiture`, 
soit `Vehicule` actuellement
- Si vous décidez un jour que la classe `Voiture` ne doit plus
 hériter de `Vehicule` mais de `VehiculeARoues` héritant
 lui-même de `Vehicule` la syntaxe restera valide ; tandis que la
 syntaxe utilisant le nommage explicite de la classe parent vous obligera
 à modifier votre code.


--------------------------------------------------------------------------------

## POO en Python – Héritage, surcharge

### Spécificités Python 2

En Python 2 la syntaxe `super` n'est pas toujours disponible.

- En Python 3, toutes les classes n'ayant pas de classe parent héritent
 implicitement de la classe `object`.
    - C'est l'équivalent de
 `Object` en Java.
    - Ecrire `class Vehicule:` est équivalent à `class Vehicule(object):`
    - Ainsi, en Python 3, toutes les classes sont des sous-classes de la
 classe Python `object`, mère de toutes les créations.
- En Python 2 ce n'est pas le cas, vous pouvez avoir plusieurs classes
 dites `racine`.
    - Dans ce cas, en Python 2, si votre classe n'hérite pas de la classe
     `object` à un moment ou un autre, vous ne pourrez pas utiliser le
     mot clef `super`

**En Python 2, `super` ne fonctionne qu'avec des classes héritant de la classe `object`.**


--------------------------------------------------------------------------------

## POO en Python – Héritage, surcharge

Pour ne pas ressaisir tous les paramètres de la fonction
surchargée dans la classe fille en plus des nouveaux que vous
définissez, vous pouvez utiliser le **passage de paramètres par
expansion**.

    !python
    class Voiture(Vehicule):
        def __init__(self, nb_portes=5, *t_args, **d_args):
            super(Voiture, self).__init__(*t_args, **d_args)
            #Vehicule.__init__(self, *t_args, **d_args)
            self.nb_portes = nb_portes


Tous les langages objets ne savent pas gérer ceci et certains vous
 obligeront à saisir manuellement les paramètres requis par la classe
 parent. Cela complique la maintenabilité. 

Ce n'est pas un problème en Python !

![](images/shadock.png)

--------------------------------------------------------------------------------

## POO en Python – Héritage, surcharge

### Exercices

#### Exercice 1

- Surchargez la fonction `afficher` dans la classe voiture pour
 qu'elle affiche le nombre de portes de la voiture en plus des attributs
 de la classe parent. 

Ne dupliquez pas le code.

#### Exercice 2

- Redéfinissez les fonctions `demarrer`, `avancer` et
 `arreter` dans la classe Voiture sans appeler les comportements de
 la classe parent.
- Appelez la fonction `suivre_itineraire` que vous n'aurez pas
 surchargée sur une instance de la classe `Voiture`. 

Toutes les fonctions sont virtuelles en Python !


--------------------------------------------------------------------------------

## POO en Python – Héritage multiple

L'héritage multiple est un cas particulier de l'héritage où une
 classe fille hérite de plusieurs classes parents.

Ceci pose des problèmes de choix : si plusieurs classes parentes
 définissent une même méthode `afficher` mais pas leur classe
 fille, quelle(s) méthode(s) de quelle classe(s) parent(s) et dans quel
 ordre seront appelées en écrivant `fille1.afficher()` :

- Celle de la première classe parent ?
- Celle de la dernière ?
- Toutes ? Dans quel ordre ?

L'algorithme gérant ces cas de figures s'appelle **MRO**, pour **Method
 Resolution Order**.

ATTENTION : Il fonctionne différemment avec les *old-style-class* de
 Python2

Ce tutorial vous donnera tous les éléments pour bien
 comprendre cette problématique :

<http://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path>
 


--------------------------------------------------------------------------------

## POO en Python – Visibilité

Certains langages objets proposent des modificateurs de **visibilité
 des attributs et méthodes** entre classes parent/fille ou en dehors de la
 classe.
 
Généralement il s'agit de :

- `private`: les attributs et méthodes de ce type ne sont manipulables
 que dans la classe qui les définit
- `protected` : les attributs et méthodes de ce type ne sont
 manipulables que dans la classe qui les définit et ses classes filles
- `public` : les attributs et méthodes de ce type sont manipulables
 partout, notamment en dehors du bloc de la classe


--------------------------------------------------------------------------------

### POO en Python – Visibilité

En Python ces modificateurs de visibilité n'existent pas. 
Toutefois il existe des conventions :

- Préfixe "`__`" : si vous préfixez le nom de votre méthode ou
 attribut par 2 tirets bas, vous indiquez que vous souhaitez qu'il soit
 privé.
- Préfixe "`_`" : Si vous préfixez le nom de votre méthode ou
 attribut par 1 tiret bas, vous indiquez que vous souhaitez qu'il soit
 protégé.

Ces conventions ne sont pas universellement adoptées et certains développeurs
utilisent seulement le préfix `_` pour indiquer les attributs privés.

*Note : ne pas confondre le préfixe __ des méthodes privées avec les méthodes spéciales où le double underscore est à la fois préfixe et suffixe. Les méthodes spéciales ne sont pas des méthodes privées !*

--------------------------------------------------------------------------------

### POO en Python – Visibilité

    !python
    class TestVisibilite:
        __valeur_privee = None
        _valeur_protegee = None

        def _methode_protegee(self):
            print("Méthode protégée")

        def __methode_privee(self):
            print("Méthode privée")

        def set_valeur_privee(self, val):
            self.__valeur_privee = val

        def get_valeur_privee(self):
            return self.__valeur_privee

        def set_valeur_protegee(self, val):
            self._valeur_protegee = val

        def get_valeur_protegee(self,):
            return self._valeur_protegee
            
- Exercice : créez une instance de cette classe et amusez vous avec l'introspection 
pour observer comment python gère les attributs / méthodes privés et protégés.
- Qu'en déduisez-vous ?


--------------------------------------------------------------------------------

### POO en Python – Visibilité

La notion de « protégé » en python est uniquement
 conventionnelle.

Vous pouvez utiliser les méthodes protégées d'une bibliothèque,
 mais c'est une mauvaise pratique : elles peuvent être modifiées
 d'une version mineure à l'autre.

La notion de « privé » est implémentée pour éviter les
 collisions entre classes parentes et enfants, mais il reste aisé
 d'accéder aux éléments.

[https://turnoff.us/geek/python-private-methods/](https://turnoff.us/geek/python-private-methods/)


--------------------------------------------------------------------------------

### POO – Accesseurs/Manipulateurs

En programmation objet on utilise généralement des fonctions pour
 accéder aux attributs d'une instance (lecture/écriture) plutôt que de
 les manipuler directement.
 
On appelle ces fonctions des « **accesseurs/manipulateurs** » ou
 « **getters/setters** ».

L'idée est de déclarer tous les attributs de type « privé » et
 de n'utiliser que ces getters/setters pour y accéder :

- Cela permet d'effectuer des contrôles avant de modifier ou retourner
 une valeur(droit d'accès, dépassement de bornes, etc.)
- Cela vous permet de faire évoluer plus facilement vos données :
si vous décidez en interne de représenter une couleur non plus par son
 nom, mais par une composante RVB, vous pourrez changer son type sans
 impacter le code des développeurs utilisant votre API


--------------------------------------------------------------------------------

## POO – Accesseurs/Manipulateurs

L'idée est de déclarer tous les attributs de type « privé » et
 de n'utiliser que ces getter/setter pour y accéder :

    !python
    class Vehicule:
        couleur = 'blanc'
        
        def __init__(self, couleur=None, identifiant=None):
            self.identifiant = identifiant
            if couleur is None:
                self.__couleur = Vehicule.couleur
            else:
                self.__couleur = couleur
                
        def set_couleur(self, new_couleur):
            self.__couleur = new_couleur
            
        def get_couleur(self):
            return self.__couleur            
                        
    v1 = Vehicule("rouge", "Ma Ferrari")
    print('Identifiant de v1:' + v1.get_couleur())
    # Je repeins v1
    v1.set_couleur("Rouge flammes")


--------------------------------------------------------------------------------

## POO en Python – Properties

- Pour simplifier l'accès aux attributs privés par des
 getters/setters, Python propose une mécanique nommée les
 « **properties** ».
- Elle permet d'utiliser vos attributs par de faux noms qui appellent de
 manière transparente les getters et setters que vous avez définis. Mais
 vous continuez à utiliser une syntaxe plus naturelle.


--------------------------------------------------------------------------------

### POO en Python – Properties

    !python
    class Vehicule:
    
        def __init__(self, couleur=None, identifiant=None):
            self.identifiant = identifiant
            if couleur is None:
                self.__couleur = Vehicule.couleur
            else:
                self.__couleur = couleur
    
        def get_couleur(self):
            return self.__couleur
    
        def set_couleur(self, value):
            self.__couleur = value
    
        def del_couleur(self):
            del self.__couleur
    
        couleur = property(get_couleur, set_couleur, del_couleur, "couleur's docstring")
    
    v1 = Vehicule("rouge", "Ma Ferrari")
    print('Identifiant de v1:' + v1.couleur)  # appelle v1.get_couleur()
    v1.couleur = "Rouge flammes" # appelle v1.set_couleur("Rouge flammes")
    del v1.couleur  # appelle v1.del_couleur()



--------------------------------------------------------------------------------

## POO en Python – Pour aller plus loin

Le modèle objet de Python est décrit de manière exhaustive dans la
 documentation, chapitre "DataModel "
 
<https://docs.python.org/3/reference/datamodel.html>
 
Plusieurs évolutions posant parfois des soucis de compatibilité ont
 été introduites entre la version 2 & 3, notamment au niveau des
 destructeurs, des méthodes spéciales et du MRO. **Soyez vigilants lors  des migrations**.

Python offre une mécanique pour simuler les **classes abstraites**, ce
 sont des classes pour lesquelles on ne peut pas créer d'instance. 
On  peut juste des dériver.

<https://docs.python.org/3/library/abc.html>

Le décorateur `@property` offre une autre manière de définir des
 getter/setter.


--------------------------------------------------------------------------------

## POO en Python - TP

### Exercice 1

Permettre le déplacement de la voiture par sur une grille.

- Permettre de préciser la position de la voiture sur une grille par des coordonnées x, y, à la "construction" de celle-ci.
- Modifier la méthode 'avancer' pour qu'elle permette de déplacer la voiture sur cette grille.
- Puis ajouter des fonctions pour tourner ! change_direction('N') → va vers le nord

### Si vous avez fini :

Modifier la méthode `suivre_itineraire` pour qu’elle prenne en paramètre des coordonnées à atteindre.

Exécuter la méthode doit faire se déplacer la voiture à cette destination.
