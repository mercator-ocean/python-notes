# Installation de jupyter


## Au moyen de pip (+virtualenv)

Placez vous dans l'environnement virtuel de votre choix (cf. [notes sur virtualenv|https://github.com/mercator-ocean/python-notes/blob/master/virtualenv.md#pour-se-placer-dans-lenvironnement-virtuel])

```sh
pip install jupyter
```

### Mise à jour de librairies

Pour installer proprement jupyter, il est nécessaire, en plus de l'installation de celui-ci, de mettre à jour les librairies ***backports.ssl_match_hostname*** et ***IPython*** (qui semblent mal gérées par pip install). Pour cela, exécuter ces commandes:

```sh
pip install -U backports.ssl_match_hostname
pip install -U IPython
```
