# Configuration de pip (gestionnaire de packages)

Pip est un gestionnaire de packages disponible en ligne de commande et branché sur la centrale en ligne [PiPy](https://pypi.python.org). Il va nous permettre de faire une installation locale de jupyter (si utilisé en dehors d'Anaconda)

Pip a besoin de passer le proxy pour télécharger les packages. Il est donc nécessaire de configurer l'environnement pour pouvoir le faire.

Ajoutez à votre fichier .bashrc (à la fin de celui-ci) les lignes suivantes (**ATTENTION**, remplacer ***<login>*** par votre login et ***<password>*** par votre mot de passe du **__proxy__**):

```Markdown
#Set proxy for pip (and others!)
HTTP_PROXY=http://<login>:<password>@proxy.mercator-ocean.fr:8080
http_proxy=$HTTP_PROXY
HTTPS_PROXY=https://<login>:<password>@proxy.mercator-ocean.fr:8080
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

***==> doit vous retourner des proposition de package, et non pas une erreur de type proxyError***
