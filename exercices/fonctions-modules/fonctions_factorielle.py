# Implementer une fonction `factorielle(n)` en utilisant la recursivite


def factorielle(n):
    if n > 1:
        return n * factorielle(n - 1)
    else:
        return 1


print(factorielle(5))
