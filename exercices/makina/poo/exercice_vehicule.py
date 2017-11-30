
class Voiture:
    # vous avez besoin d'attributs
    def __init__(self, position_depart):
        self.position = position_depart

    def demarrer(self):
        """"""

    def avancer(self):
        """
        Fait avancer la voiture d'une case dans la grille
        On ne peut pas avancer si on n'a pas démarré (ou qu'on s'est arrêté)
        :return:
        """

    def arreter(self):
        """"""

    def suivre_itineraire(self, destination):
        """
        :param destination: liste (x, y)
        :return:
        """
        # appeler demarrer, avancer, tourner et arreter
        # pour déplacer la position du vehicule jusqu'à la destination indiquée

    def tourner(self, direction):
        """
        change la direction de la voiture*. ça ne la fait pas avancer
        :param direction: 'N'|'S'|'E'|'W'
        :return:
        """

v1 = Voiture([0, 0])

v1.suivre_itineraire([3, 4])
assert v1.position == [3, 4]
