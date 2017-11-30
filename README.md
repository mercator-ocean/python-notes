# Formation Python initiation MO/Makina

Ce dossier contient toute la documentation et les ressources nécessaires à la bonne configuration de son poste de travail en vue de la formation python initiation.

## 1. Besoins pour la formation

### Environnement de travail

La formation inclue une partie TP avec développement d'une application. Cette partie nécessite de mettre en place une connection à un px, afin de bénéficier de votre environnement linux personnel.

La connection se fait au moyen de l'utilitaire XMing disponible sur les postes windows. Pour configurer cette connection veuillez suivres les instructions fournies sur le [portail wiki info](https://wikiinfo.mercator-ocean.fr/dokuwiki/doku.php?id=user:4windows:1logiciels:xming&s[]=xming) -section ***Création de fichiers xlaunch***.

Pour les besoins de configuration de l'environnement, il est préférable de travailler directement depuis son px.

### Environnement python
Une fois connecté à votre px, une configuration propre de l'environnement python doit être faite, ainsi que l'installation de certains plugins/outils.

Les besoins essentiels sont les suivants:
1. Librairies pythons:
   * NetCDF4, PyYaml, Matplotlib, numpy
2. Un notebook, soit:
   * l'interpréteur Ipython et son notebook
   * Jupyter notebook (plus récent)
4. Une IDE (interface de développement) python
   * PyCharm
   * Autre (anaconda-navigator, gedit, pydev-eclipse,  ...)
   
### Accès aux ressources:

Ce dépôt github contient:
* Le contenu de la formation Python-initiation
  * le [support de cours](https://github.com/mercator-ocean/python-notes/tree/master/suppots/makina)
  * les [exercices associés](https://github.com/mercator-ocean/python-notes/tree/master/exercices/makina)
  * et des exemples de [notebooks](https://github.com/mercator-ocean/python-notes/tree/master/notebooks/makina)
* Des exemples et ressources en plus qui s'enrichiront au fil du temps.

Toutes ces ressources sont aussi disponibles sur le réseau : ```/home/rdussurget/python-notes/ressources/```

Vous y trouverez en plus:
* les données du cours ```/home/rdussurget/python-notes/data/```
* les programmes d'installation d'anaconda & pycharm: ```/home/rdussurget/python-notes/ressources/```

Cela vous permettra de télécharger facilement ces données chez vous (si vous n'avez pas de compte github pour cloner le dépôt).

## 2. Configuration de l'environnement

Connectez vous d'abord à votre px (via Xming si vous êtes à distance).

Procédez à la configuration de base de votre PYTHONPATH (section **2.1**)

Ensuite, 3 façon de faire:
* Configuration du notebook IPython
* Installation d'Anaconda (inclue jupyter - mais volumineux)
* Installation de jupyter sous un environnement virtuel perso (léger, plus difficile)

### 2.1 Configuration python de base - PYTHONPATH (.bashrc)

L'environnement python se base sur la variable ```PYTHONPATH```, celle-ci étant initialisée dans le ```$HOME/.bashrc``` . Pour les besoins de la formation, nous partirons d'un environnement le **plus vierge possible** (seulement les librairies numpy, matplotlib, netCDF4, yaml).

Pour cela, ajouter à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes:

```sh
unset PYTHONPATH
export PYTHONPATH=/home/modules/versions/64/centos7/pyyaml/pyyaml-3.12/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/netcdf4python/netcdf4python-1.0.7_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/matplotlib/matplotlib-2.0.0_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/numpy/numpy-1.9.1_gnu4.8.2/lib64/python2.7/site-packages
```


### 2.2 Configuration du notebook IPython

Instructions [ICI](https://github.com/mercator-ocean/python-notes/blob/master/iPython-notebook.md).

**Attention** : afin d'éviter tout conflit __il est préférable de commenter la ligne dans le **.bashrc**__ si vous voulez configurer vous même votre environnement python afin d'éviter tout conflit.

### 2.3 Installation d'Anaconda (OPTIONELLE!)

Cf. **[section 3. Installation d'Anaconda2-5](https://github.com/mercator-ocean/python-notes/blob/master/README.md#installation-danaconda2-5)**

### 2.4 Installation de jupyter (OPTIONELLE!)

Pour bénéficier des __dernières versions__ des librairies python et notamment de jupyter (et ipython indépendamment), vous pouvez l'installer par vous même en utilisant pip (gestionnaire de packages python) et virtualenv (environnements python "*virtuels*").

#### a. Réinitialisation du PYTHONPATH

Afin de procéder à l'installation, veuillez vérifier que votre PYTHONPATH (```echo $PYTHONPATH```) ne contient que ce qui a été déclaré dans la section **2. Configuration python de base**.

#### b. Configuration de pip

Vous devez avoir un ```pip``` en état de marche.

Veuillez suivre les instruction de configuration [ici](https://github.com/mercator-ocean/python-notes/blob/master/pip-config.md).


#### c. virtualenv (environnements virtualisés pour python)

Pour installer la suite jupyter dans un environnement virtualisé, vous trouvez [ICI](https://github.com/mercator-ocean/python-notes/blob/master/virtualenv.md#cr%C3%A9ation-dun-environnement-virtuel) des notes sur virtualenv et son utilisation.

Veuillez notamment:
1. configurer virtualenv ([ici](https://github.com/mercator-ocean/python-notes/blob/master/virtualenv.md#configuration-et-d%C3%A9claration-du-wrapper))
2. créer un environnement virtuel python pour jupyter ([ici](https://github.com/mercator-ocean/python-notes/blob/master/virtualenv.md#cr%C3%A9ation-dun-environnement-virtuel))

#### d. Installation de jupyter

Cf. note [ICI](https://github.com/mercator-ocean/python-notes/blob/master/jupyter-install.md).


## 3. Installation des logiciels

Tous les programmes d'installation (linux) sont disponible sous ce répertoire:
```/home/rdussurget/python-notes/ressources/```

### Installation de PyCharm (IDE Python)
```pycharm-community-2017.2.4.tar.gz```

Ce programme peut-être dézippé sur votre home (ou autre) et installé en standalone sans avoir besoin d'un accès root.

__Pour le lancer:__
```sh
/mon/chemin/vers/pycharm/bin/pycharm.sh
```

### Installation d'Anaconda2-5
```Anaconda2-5.0.1-Linux-x86_64.sh```

Anaconda est une suite logicielle complète comprenant l'IDE anaconda, le gestionnaire de packages conda (permettant notamment d'installer des librairies de calcul numérique optimisées) & le notebook jupyter

Ce programme d'installation installe la suite complète (ce qui prend un peu plus de temps et d'espace que le notebook jupyter seulement - **2.7Go** au lieu de **91Mo**).

Vous pouvez exécuter ce programme, et celui-là se chargera de vous proposer un répertoire d'installation sur votre home, eg. /home/username/softwares/anaconda (attention, l'install prend un certain temps).

Une fois installé, l'installateur ***modifiera la variable path de votre fichier .bashrc*** pour y inclure les exécutable de l'IDE (anaconda-navigator), conda & le notebook jupyter (voir section ***4. Pour lancer un notebook Jupyter***).

### Installation de jupyter notebook seulement (pas si comliqué!)

Il est possible de bénéficier de la dernière version du notebook jupyter en utilisant un environnement virtuel (virtualenv) et l'installateur de packages pip. Pour cela, regardez la section 5 (***Pour avoir un environnement "dernier cri"***).


## 4. Lancement des utilitaires

### Python

Pour exécuter un script python (version 2.7 par défaut - mais version 3.2 disponible):

```sh
python monScript.py
```

L'appel à la commande ```python``` sans arguments lance l'interpréteur seul (difficilement exploitable).

### L'interpréteur IPython

Pour lancer IPython (interpréteur en ligne de commande intéractif):

```sh
ipython
```
Vous arriverez dans une invite de commande dans laquelle vous pourrez entrer et exécuter vos lignes de code.

### Pour lancer un notebook

cf. notes sur le [lancement du notebook](https://github.com/mercator-ocean/python-notes/blob/master/notebook-run.md)







