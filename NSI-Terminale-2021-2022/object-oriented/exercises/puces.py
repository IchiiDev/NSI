import random

class Puce():

    def __init__(self, nom, couleur, pos = 0):
        self.__nom = nom
        self.__couleur = couleur
        self.__pos = pos

    def getName(self):
        return self.__nom

    def getColor(self):
        return self.__couleur

    def getPosition(self):
        return self.__pos

    def setPosition(self, pos):
        self.__pos = pos

    def forward(self):
        self.__pos += random.randint(1, 3)
        return self.__pos

class Course:

    def __init__(self, taille=10):
        self.__puces = []
        self.__taille = taille
        self.__round = 0

    def addPuce(self, puce):
        self.__puces.append(puce)
        return self

    def getRound(self):
        return self.__round
    
    def nextRound(self):
        self.__round += 1
        print(f"-----------------\nRound {self.getRound()}")
        for puce in self.__puces:
            name = puce.getName()
            message = f"Case {puce.getPosition()}" if puce.forward() < self.__taille else "Arrivée !"
            print(f"{name}: {message}")
        print("-----------------")


if __name__ == "__main__":
    puce1 = Puce("Dolly", "rouge")
    puce2 = Puce("Bella", "bleue")
    puce3 = Puce("Alexis", "vert")
    puce4 = Puce("Baptiste", "jaune")

    course = Course().addPuce(puce1).addPuce(puce2).addPuce(puce3).addPuce(puce4)

    [course.nextRound() for _ in range(5)]