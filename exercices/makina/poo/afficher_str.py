class Vehicule:

    couleur = 'blanc'
    nb_vehicules_crees = 0

    def __init__(self, couleur=None, identifiant="WW"):
        Vehicule.nb_vehicules_crees += 1
        self.identifiant = identifiant
        if couleur is None:
            # Si paramètre couleur = None, on utilise la couleur de la classe
            self.couleur = Vehicule.couleur
        else:
            # On affecte à l'attribut couleur la valeur du paramètre couleur
            self.couleur = couleur

    def afficher(self):
        print("Véhicule {0} immatriculé {1}".format(self.couleur, self))

    def __str__(self):
        return self.identifiant


v1 = Vehicule(identifiant="4858 VK 67", couleur="rouge")
v1.afficher()

# Situations où __str__ est appelée
print("Mon véhicule est immatriculé %s" % v1)
print("Mon véhicule est immatriculé {0}".format(v1))
print(f"Mon véhicule est immatriculé {v1}")
print(v1)
