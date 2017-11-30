class Vehicule:

    couleur = 'blanc'
    nb_vehicules_en_service = 0
    compteur_vehicules = 0
    numero_vehicule = None

    def __init__(self, couleur=None, identifiant=None):
        Vehicule.nb_vehicules_en_service += 1
        Vehicule.compteur_vehicules += 1
        self.numero_vehicule = Vehicule.compteur_vehicules
        self.identifiant = identifiant
        if couleur is None:
            # Si paramètre couleur = None, on utilise la couleur de la classe
            self.couleur = Vehicule.couleur
        else:
            # On affecte à l'attribut couleur la valeur du paramètre couleur
            self.couleur = couleur

    def __del__(self):
        Vehicule.nb_vehicules_en_service -= 1

    @staticmethod
    def affiche_nb_vehicules_en_service():
        return Vehicule.nb_vehicules_en_service

v1 = Vehicule()
v2 = Vehicule()
del v2
v3 = Vehicule()
print('nb_vehicules_en_service', Vehicule.nb_vehicules_en_service)
print('numero v3', v3.numero_vehicule)
v3.affiche_nb_vehicules_en_service()
Vehicule.affiche_nb_vehicules_en_service()
