# Lancement d'un notebook

Si vous avez configuré votre environnement et installé un notebook ([notes ici](https://github.com/mercator-ocean/python-notes/blob/master/README.md#2-configuration-de-lenvironnement))


Le notebook, s'il est lancé via IPython, démarre un service html sur le px à partir duquel vous l'exécutez. Une fois le service lancé, vous pourrez accéder au notebook en ouvrant votre navigateur.

* Si vous utilisez le **notebook IPython**
```sh
ipython notebook --ip=<MON PX>.mercator-ocean.fr
```

* Si vous utilisez le **notebook Jupyter**
```sh
jupyter notebook --ip=<MON PX>.mercator-ocean.fr
```

Le serveur jupyter devrai vous indiquer en ligne de commande si le service est fonctionnel.

Puis connectez vous à l'URL suivante (directement à partir de votre poste windows si vous êtes connectés à votre px via XMing):
[**http://\<MONPX\>.mercator-ocean.fr:8888**](http://MONPX.mercator-ocean.fr:8888) --> Remplace **\<MONPX\> par le nom de votre PX (e.g. px-137).

Et laissez vous guider.

## Arrêt d'un notebook

```sh
jupyter notebook --ip=<MON PX>.mercator-ocean.fr stop
```

## Lancement d'un notebook en arrière plan

Vous pouvez vous servir de la commande bash ```nohup``` pour détacher votre session notebook de votre terminal.

```sh
nohup jupyter notebook --ip=<MON PX>.mercator-ocean.fr > ~/notebook.log
```

Les informations du notebook seront loggées dans le fichier ~/notebook.log

## Erreurs

**Si le notebook retourne des erreurs de type "Kernel died"**: l'installation de jupyter a échoué, probablement à cause d'un conflit dans l'environnement.
