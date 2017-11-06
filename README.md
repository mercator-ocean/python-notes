# FormationPython
Stuff for MO



## Besoins pour la formation

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

## Configuration de l'environnement

### PYTHONPATH (.bashrc)
L'environnement python se base sur la variable PYTHONPATH, celle-ci étant initialisée dans le _$HOME/.bashrc_ . Pour les besoins de la formation, nous partirons d'un environnement le **plus vierge possible**.

```

```




### pip (gestionnaire de packages)


Pip a besoin de passer le proxy pour télécharger les packages.
Il est donc nécessaire de configurer l'environnement pour pouvoir le faire;

```
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

```
export WORKON_HOME=$HOME/.virtualenv
source /usr/bin/virtualenvwrapper.sh
```


## Initialisation de l'environnement virtuel pour la formation


```
mkvirtualenv --system-site-packages jupyter
pip install jupyter
```

### notes sur 


## Installation des logiciels


Tous les programmes d'installation (linux) sont disponible sous ce répertoire:
/home/rdussurget/FormationPython/ressources/

* Installation de PyCharm (IDE Python)
pycharm-community-2017.2.4.tar.gz

Ce programme peut-être dézippé sur votre home (ou autre) et installé en standalone sans avoir besoins d'un accès root.

* Installation d'Anaconda2-5 (suite complète comprenant l'IDE anaconda, le gestionnaire de packages conda & le notebook jupyter)
Anaconda2-5.0.1-Linux-x86_64.sh

Ce programme d'installation installe la suite complète (ce qui prend un peu plus de temps et d'espace que le notebook jupyter seulement).
Vous pouvez exécuter ce programme, et celui-là se chargera de vous proposer un répertoire d'installation sur votre home, eg. /home/username/softwares/anaconda (attention, l'install prend un certain temps).

* Installation de jupyter notebook seulement (avec pip + virtualenv)
D'abord, initialiser un environnement virtuel avec virtualenv+pip (cf. section "mkvirtualenv --system-site-packages jupyter
pip install jupyter").









