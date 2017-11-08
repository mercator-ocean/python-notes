# Virtualenv

Virtualenv est un utilitaire permettant de faire des déployer localement (cad. sans privilèges ROOT sur une machine) une instance de python.

Concrètement, virtualenv va __copier l'installation python du système dans un répertoire local__ pointé par la variable ```WORKON_HOME``` (cf. section suivante)


### Configuration et déclaration du wrapper

Pour une utilisation facilité de virtualenv, ajoutez à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes:

```sh
export WORKON_HOME=$HOME/.virtualenv
source /usr/bin/virtualenvwrapper.sh
```

### Création d'un environnement virtuel

Pour créer un environnement virtuel, utiliser la commande ```mkvirtualenv```.

On peut y accoler l'option ```--system-site-packages``` qui permet de copier les librairies déjà présentes dans l'install python du système (et donc celles dans le PYTHONPATH)

Pour créer un environnement virtuel nommé **jupyter**:

```sh
mkvirtualenv --system-site-packages jupyter
```

Concrètement, ceci va créer un répertoire ```$WORKON_HOME/jupyter```, dans lequel vous trouverez la copie de l'installation python du système, cad. les exécutables et les librairies.

```md
**NOTE**: Cette commande va activer automatiquement l'environnement que l'on vient de créer (**son nom est indiqué devant le prompt**)
```

### Vérification

```sh
which python
```

La dernière commande vous renvoie le chemin vers l'exécutable python utilisé par l'environnement, cad. ```$WORKON_HOME/jupyter/bin/python``` (au lieu de ```/usr/bin/python```).


### Pour se placer dans l'environnement virtuel

Utiliser ```workon``` - le nom de l'env. apparaît alors au début du prompt:

```sh
workon jupyter
```

### Pour désactiver votre environnement virtuel

```sh
deactivate
```
(**CTRL+D**) fonctionne aussi.



### Pour désinstaller un environnement virtuel

Pour désinstaller l'environnement virtuel **jupyter**:

```sh
rmvirtualenv jupyter
```
