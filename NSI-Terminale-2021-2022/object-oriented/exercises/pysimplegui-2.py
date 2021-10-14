import random
from pprint import pprint

class Space:

    def __init__(self):
        self.__board = self.__initBoard()
        self.__players = []

    def __initBoard(self, size=10):
        return [[0 for _ in range(size)] for _ in range(size)]

    def getFullBoard(self):
        return self.__board

    def addPlayer(self, player):
        self.__players.append(player)
        return self

    def getPlayers(self):
        return self.__players

class Player():

    def __init__(self, name, startX, startY, textColor, bgColor, space):
        self.__name = name
        self.x = startX
        self.y = startY
        self.__textColor = textColor
        self.__bgColor = bgColor
        self.__space = space
    
    def nextMove(self):
        board = self.__space.getFullBoard()
        nextCoords = (self.x + random.randint(-1, 1), self.y + random.randint(-1, 1))
        for player in self.__space.getPlayer():
            if not player.canIMove(nextCoords): return
        if 0 <= nextCoords[0] < len(board)-1:
            self.x = nextCoords[0]
        else:
            self.x = len(board)-1 if nextCoords[0] >= 0 else 0

        if 0 <= nextCoords[1] < len(board)-1:
            self.y = nextCoords[1]
        else:
            self.y = len(board)-1 if nextCoords[1] >= 0 else 0
        
    def canIMove(self, coords):
        myCoords = (self.x, self.y)
        return False if myCoords == coords else True

space = Space()
pprint(space.getFullBoard())
player1 = Player("1", 5, 5, "white", "blue", space)
space.addPlayer(player1)
player1.nextMove()
