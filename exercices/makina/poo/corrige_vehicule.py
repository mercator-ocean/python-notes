class Voiture:
    position = None
    moteur_tourne = False
    direction = 'S'
    __avance_direction = {'N': (0, 1),
                         'S': (0, -1),
                         'E': (-1, 0),
                         'O': (1, 0)}

    def __init__(self, position_depart):
        self.position = position_depart

    def demarrer(self):
        print("VROUMMMM")
        self.moteur_tourne = True

    def avancer(self):
        if not self.moteur_tourne:
            print("Hé, faudrait ptet penser à démarrer le moteur avant de vouloir avancer !")
            return
        print("Avance, direction: " + self.direction)
        changement_position = self.__avance_direction[self.direction]
        self.position[0] = self.position[0] + changement_position[0]
        self.position[1] = self.position[1] + changement_position[1]

    def arreter(self):
        print("Arrêt du moteur")
        self.moteur_tourne = False

    def suivre_itineraire(self, destination):
        """

        :param destination: tuple(x,y)
        :return:
        """
        # faire appel à démarrer, avancer, tourner, arrêter, pour déplacer la position du véhicule jusqu'à destination
        self.demarrer()
        while self.position != destination:
            if self.position[0] < destination[0]:
                self.tourner("O")
            elif self.position[0] > destination[0]:
                self.tourner("E")
            elif self.position[1] < destination[1]:
                self.tourner("N")
            elif self.position[1] > destination[1]:
                self.tourner("S")
            self.avancer()
        self.arreter()
        print("Vous êtes arrivés. Votre destination se trouve en face.")

    def tourner(self, direction):
        """

        :param direction:'N','S','E','O'
        :return:
        """
        self.direction = direction


v1 = Voiture([0, 0])
v1.suivre_itineraire([3, 4])

assert v1.position == [3, 4]
print(Voiture.__dict__)
print(v1.__avance_direction)
