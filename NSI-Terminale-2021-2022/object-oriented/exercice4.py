class Velo:

    def __init__(self):
        self.__couleur = "Rouge"
        self.__roues = 2
        self.__pos = 0

    def obtenir_pos(self):
        return self.__pos

    def modifier_pos(self, pos):
        self.__pos = pos

    def avancer(self, dis):
        self.__pos += dis

    pos = property(obtenir_pos, modifier_pos)
