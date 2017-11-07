
### Question
# Comment pourrait-on faire pour rendre le texte affiché paramétrable ?
import time


def execute_n_fois(n, procedure, delay=1, *args, **kwargs):
    for i in range(n):
        time.sleep(delay)
        procedure(*args, **kwargs)


def affiche_echo(texte="Echo"):
    print(texte)

execute_n_fois(5, affiche_echo, delay=4, texte="ECHO")
