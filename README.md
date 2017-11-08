# Formation Python MO/Makina

Ce dossier contient toute la documentation et les ressources nécessaires à la bonne configuration de son poste de travail en vue de la formation python initiation.

## 1. Besoins pour la formation

### Environnement de travail

La formation inclue une partie TP avec développement d'une application. Cette partie nécessite de mettre en place une connection à un px, afin de bénéficier de votre environnement linux personnel.

La connection se fait au moyen de l'utilitaire XMing disponible sur les postes windows. Pour configurer cette connection veuillez suivres les instructions fournies sur le [portail wiki info](https://wikiinfo.mercator-ocean.fr/dokuwiki/doku.php?id=user:4windows:1logiciels:xming&s[]=xming) -section ***Création de fichiers xlaunch***.

Pour les besoins de configuration de l'environnement, il est préférable de travailler directement depuis son px.

### Environnement python
Une fois connecté à votre px, une configuration propre de l'environnement python doit être faite, ainsi que l'installation de certains plugins/outils.

Nous proposons ici soit:
* de déployer une distribution python complète, indépendante du système, anaconda
* de configurer nous même l'environnement

Les besoins essentiels sont les suivants:
1. Librairies pythons:
   * NetCDF4, PyYaml, Matplotlib, numpy
2. Un notebook, soit:
   * l'interpréteur Ipython et son notebook
   * Jupyter (notebook) - **ATTENTION: soit l'un soit l'autre de préférence**
4. Une IDE (interface de développement) python
   * PyCharm
   * Autre (anaconda-navigator, gedit, pydev-eclipse,  ...)

## 2. Configuration de l'environnement

Connectez vous d'abord à votre px (via Xming si vous êtes à distance).

### Configuration du notebook IPython et lancement.

Une installation du notebook jupyter est déjà disponible par défaut avec le module IPython.

Pour cela, ajouter à votre fichier ```.bashrc``` (à la fin de celui-ci) les lignes suivantes:

```sh
module load ipython/ipython-2.4
```

Pour lancer le notebook IPython, regardez la section ***Lancer le notebook*** (4e chapitre).

```Markdown
**ATTENTION**: une fois le test réalisé, __il est préférable de commenter la ligne dans le **.bashrc**__ afin d'éviter tout conflit avec le reste de la configuration
```

### PYTHONPATH (.bashrc)
L'environnement python se base sur la variable ```PYTHONPATH```, celle-ci étant initialisée dans le ```$HOME/.bashrc``` . Pour les besoins de la formation, nous partirons d'un environnement le **plus vierge possible** (cad. débarassé de tout le superflu déjà installé...!!)

Pour cela, ajouter à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes:

```sh
unset PYTHONPATH
export PYTHONPATH=/home/modules/versions/64/centos7/pyyaml/pyyaml-3.12/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/netcdf4python/netcdf4python-1.0.7_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/matplotlib/matplotlib-2.0.0_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/numpy/numpy-1.9.1_gnu4.8.2/lib64/python2.7/site-packages
```



## 3. Installation des logiciels


Tous les programmes d'installation (linux) sont disponible sous ce répertoire:
```/home/rdussurget/FormationPython/ressources/```

### Installation de PyCharm (IDE Python)
```pycharm-community-2017.2.4.tar.gz```

Ce programme peut-être dézippé sur votre home (ou autre) et installé en standalone sans avoir besoin d'un accès root.

__Pour le lancer:__
```sh
/mon/chemin/vers/pycharm/bin/pycharm.sh
```


### Installation d'Anaconda2-5
```Anaconda2-5.0.1-Linux-x86_64.sh```

**[INSTALLATION OPTIONNELLE!]**

Anaconda est une suite logicielle complète comprenant l'IDE anaconda, le gestionnaire de packages conda (permettant notamment d'installer des librairies de calcul numérique optimisées) & le notebook jupyter

Ce programme d'installation installe la suite complète (ce qui prend un peu plus de temps et d'espace que le notebook jupyter seulement - **2.7Go** au lieu de **91Mo**).

Vous pouvez exécuter ce programme, et celui-là se chargera de vous proposer un répertoire d'installation sur votre home, eg. /home/username/softwares/anaconda (attention, l'install prend un certain temps).

Une fois installé, l'installateur modifiera votre path pour y inclure les exécutable de l'IDE (anaconda-navigator), conda & le notebook jupyter (voir section ***4. Pour lancer un notebook Jupyter***).

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

### Pour lancer un notebook Jupyter

Le notebook Jupyter, s'il est lancé via IPython, démarre un service html sur le px à partir duquel vous l'exécutez. Une fois le service lancé, vous pourrez accéder au notebook en ouvrant votre navigateur.

* Si vous utilisez le **notebook IPython**
```sh
ipython notebook --ip=<MON PX>.mercator-ocean.fr
```

* Si vous utilisez le **notebook Jupyter**
```sh
jupyter notebook --ip=<MON PX>.mercator-ocean.fr
```

Le serveur jupyter devrai vous indiquer en ligne de commande si le service est fonctionnel.

Puis connectez vous à l'URL suivante (directement à partir de votre poste windows si vous êtes connectés à votre px via XMing):  [http://**<MONPX>**.mercator-ocean.fr:8888](http://MONPX.mercator-ocean.fr:8888)

Et laissez vous guider.

## 5. Pour avoir un environnement "dernier cri"

```Markdown
**__OPTIONNEL__**:
à tester, mais si vous ne réusissez pas, retourner à la configuration simple avec **IPython seulement**.
```

Pour bénéficier des dernières version des librairies python et notamment de jupyter (et ipython indépendamment), vous pouvez l'installer par vous même en utilisant pip et virtualenv.

### pip (gestionnaire de packages)

Pip est un gestionnaire de packages disponible en ligne de commande et branché sur la centrale en ligne [PiPy](https://pypi.python.org). Il va nous permettre de faire une installation locale de jupyter (si utilisé en dehors d'Anaconda)

Pip a besoin de passer le proxy pour télécharger les packages. Il est donc nécessaire de configurer l'environnement pour pouvoir le faire.

Ajoutez à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes (**ATTENTION**, remplacer ***<login>*** par votre login et ***<password>*** par votre mot de passe du **__proxy__**):

```Markdown
#Set proxy for pip (and others!)
HTTP_PROXY=http://***<login>***:***<password>***@proxy.mercator-ocean.fr:8080
http_proxy=$HTTP_PROXY
HTTPS_PROXY=https://***<login>***:***<password>***@proxy.mercator-ocean.fr:8080
https_proxy=$HTTPS_PROXY

export HTTP_PROXY
export HTTPS_PROXY
export https_proxy
export http_proxy
```

Pour vérifier que l'installation de pip fonctionne, rechercher un module sur pipy:

```sh
pip search pip
```

***doit vous retourner des proposition de package, et non pas une erreur de type proxyError***

### virtualenv (environnements virtualisés pour python)

Virtualenv est un utilitaire permettant de faire des déployer localement (cad. sans privilèges ROOT sur une machine) une instance de python. Pour une utilisation facilité de virtualenv, ajoutez à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes:

```sh
export WORKON_HOME=$HOME/.virtualenv
source /usr/bin/virtualenvwrapper.sh
```

### Installation de jupyter


1. Vérification de l'environnement.

Avant tout, il est __impératif de contrôler l'environnement__, notamment le **PYTHONPATH** qui ne doit pas contenir de **__référence explicite__** à IPython

```sh
echo $PYTHONPATH
```

2. Création de l'environnement.

Initialiser un environnement "jupyter"

```sh
mkvirtualenv --system-site-packages jupyter
```

Ceci va créer un répertoire ```$WORKON_HOME/jupyter```, dans lequel est déployé une instance locale de python avec tous ses modules à partir de l'installation python du système.

   * **Notes sur l'utilisation de virtualenv**
Pour vous placer dans votre environnement (si vous n'y êtes pas déjà!)
```sh
workon jupyter
which python
```
La dernière commande vous renvoie le chemin vers l'exécutable python utilisé par l'environnement, cad. ```$WORKON_HOME/jupyter/bin/python``` (au lieu de ```/usr/bin/python```).

Pour désactiver votre environnement virtuel
```sh
deactivate
```
(**CTRL+D**) fonctionne aussi.

2. Installation de jupyter

```sh
pip install jupyter
```

3. Mise à jour de librairies

Pour installer proprement jupyter, il est nécessaire, en plus de l'installation de celui-ci, de mettre à jour les librairies ***backports.ssl_match_hostname*** et ***IPython*** (qui semblent mal gérées par pip install). Pour cela, exécuter ces commandes:

```sh
pip install -U backports.ssl_match_hostname
pip install -U IPython
```

4. Lancement de jupyter

cf. Section ***4. Pour lancer un notebook Jupyter***

```sh
jupyter notebook --ip=px-147.mercator-ocean.fr &
```
Créer un notebook, et tenter de le lancer. **Si le notebook retourne des erreurs de type "Kernel died"**, l'installation de jupyter a échoué, probablement à cause d'un conflit dans l'environnement.

**Si celui-ci n'est pas résolvable, retourner à la solution du notebook jupyter**






