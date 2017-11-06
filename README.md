# FormationPython
Stuff for MO



## 1. Besoins pour la formation

La formation inclue une partie TP avec développement d'une application. Pour, cela une configuration propre de python doit être faite, ainsi que l'installation de certains plugins/outils.

Nous proposons ici soit:
* de déployer une distribution python complète, indépendante du système, anaconda
* de configurer nous même l'environnement

Les besoins essentiels sont les suivants:
1. Librairies pythons:
   * NetCDF4, PyYaml, Matplotlib, numpy
2. Jupyter (notebook)
3. Une IDE (interface de développement) python
   * PyCharm
   * Autre (gedit, pydev-eclipse, ...)

## 2. Configuration de l'environnement

### PYTHONPATH (.bashrc)
L'environnement python se base sur la variable PYTHONPATH, celle-ci étant initialisée dans le _$HOME/.bashrc_ . Pour les besoins de la formation, nous partirons d'un environnement le **plus vierge possible** (cad. débarassé de tout le superflu déjà installé...!!)

Pour cela, ajouter à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes:

```sh
unset PYTHONPATH
export PYTHONPATH=/home/modules/versions/64/centos7/pyyaml/pyyaml-3.12/lib64/python2.7/site-packages::/home/modules/versions/64/centos7/netcdf4python/netcdf4python-1.0.7_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/matplotlib/matplotlib-2.0.0_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/numpy/numpy-1.9.1_gnu4.8.2/lib64/python2.7/site-packages:/home/modules/versions/64/centos7/ipython/ipython-3.2.1_gnu4.8.2/lib/python2.7/site-packages
```

### Configuration de jupyter

Une installation du notebook jupyter est déjà disponible par défaut avec le module IPython.

Pour cela, ajouter à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes:

```sh
module load ipython/ipython-2.4
```

## 3. Installation des logiciels


Tous les programmes d'installation (linux) sont disponible sous ce répertoire:
/home/rdussurget/FormationPython/ressources/

### Installation de PyCharm (IDE Python)
pycharm-community-2017.2.4.tar.gz

Ce programme peut-être dézippé sur votre home (ou autre) et installé en standalone sans avoir besoins d'un accès root.

### Installation d'Anaconda2-5 (suite complète comprenant l'IDE anaconda, le gestionnaire de packages conda & le notebook jupyter)
Anaconda2-5.0.1-Linux-x86_64.sh

Ce programme d'installation installe la suite complète (ce qui prend un peu plus de temps et d'espace que le notebook jupyter seulement - **2.7Go** au lieu de **91Mo**).

Vous pouvez exécuter ce programme, et celui-là se chargera de vous proposer un répertoire d'installation sur votre home, eg. /home/username/softwares/anaconda (attention, l'install prend un certain temps).

### Installation de jupyter notebook seulement (pas si comliqué!)
Il est possible de bénéficier de la dernière version du notebook jupyter en utilisant un environnement virtuel (virtualenv) et l'installateur de packages pip. Pour cela, regardez la section 5 (***Pour avoir un environnement "dernier cri"***).

## 4. Lancement des utilitaires

### Python

Pour exécuter un script python (version 2.7 par défaut - mais version 3.2 disponible):

```sh
python monScript.py
```

### L'interpréteur IPython

Pour lancer IPython (interpréteur en ligne de commande intéractif):

```sh
ipython
```
Vous arriverez dans une invite de commande dans laquelle vous pourrez entrer et exécuter vos lignes de code.

### Pour lancer un notebook Jupyter

Le notebook Jupyter, s'il est lancé via IPython, démarre un service html sur le px à partir duquel vous l'exécutez. Une fois le service lancé, vous pourrez accéder au notebook en ouvrant votre navigateur.

```sh
ipython notebook --ip=<MON PX>.mercator-ocean.fr
```

Puis connectez vous à l'URL suivante [http://**<MONPX>**.mercator-ocean.fr:8888](http://MONPX.mercator-ocean.fr:8888)

Et laissez vous guider.

## 5. Pour avoir un environnement "dernier cri"

Pour bénéficier des dernières version des librairies python et notamment de jupyter, vous pouvez l'installer par vous même en utilisant pip et virtualenv.

### pip (gestionnaire de packages)

Pip est un gestionnaire de packages disponible en ligne de commande et branché sur la centrale en ligne [PiPy](https://pypi.python.org). Il va nous permettre de faire une installation locale de jupyter (si utilisé en dehors d'Anaconda)

Pip a besoin de passer le proxy pour télécharger les packages. Il est donc nécessaire de configurer l'environnement pour pouvoir le faire.

Ajoutez à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes:

```sh
#Set proxy for pip (and others!)
HTTP_PROXY=http://<login>:<psws>@proxy.mercator-ocean.fr:8080
http_proxy=$HTTP_PROXY
HTTPS_PROXY=http://<login>:<psws>@proxy.mercator-ocean.fr:8080
http_proxy=$HTTPS_PROXY

export HTTP_PROXY
export HTTPS_PROXY
export https_proxy
export http_proxy
```

### virtualenv (environnements virtualisés pour python)

Virtualenv est un utilitaire permettant de faire des déployer localement (cad. sans privilèges ROOT sur une machine) une instance de python. Pour une utilisation facilité de virtualenv, ajoutez à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes:

```sh
export WORKON_HOME=$HOME/.virtualenv
source /usr/bin/virtualenvwrapper.sh
```

### Installation de jupyter



1. Création de l'environnement.

Initialiser un environnement "jupyter"

```sh
mkvirtualenv --system-site-packages jupyter
```

Ceci va créer un répertoire **"jupyter"** sous **$WORKON_HOME/**, dans lequel est déployé une instance local de python avec tous ses modules à partir de l'installation python du système.

   * **Notes sur l'utilisation de virtualenv**
Pour vous placer dans votre environnement (si vous n'y êtes pas déjà!)
```sh
workon jupyter
which python
```
La dernière commande vous renvoie le chemin vers l'exécutable python utilisé par l'environnement.

Pour désactiver votre environnement virtuel
```sh
deactivate
```
(**CTRL+D**) fonctionne aussi.

2. Mise à jour de librairies
Pour installer proprement jupyter, il est nécessaire, en plus de l'installation de celui-ci, de mettre à jour les librairies ***backports.ssl_match_hostname*** et ***IPython***. Pour cela, exécuter ces commandes:

```sh
pip install -U backports.ssl_match_hostname
pip install -U IPython
```

3. Installation de jupyter

```sh
pip install jupyter
```

4. Lancement de jupyter

```sh
jupyter notebook --ip=px-147.mercator-ocean.fr &
```
Le serveur jupyter devrai vous indiquer en ligne de commande si le service est fonctionnel.






