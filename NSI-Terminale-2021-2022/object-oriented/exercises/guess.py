import random

class Player():
    
    def __init__(self, name, robot=False):
        self.__name = name
        self.__isRobot = robot
        self.__score = 0
        self.__number = None

    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score

    def isRobot(self):
        return self.__isRobot
        
    def setNumber(self, number):
        self.__number = number
    
    def getNumber(self):
        return self.__number

    def chooseAnswer(self):
        if self.isRobot() == True:
            return random.randint(1, 10)
        else:    
            answer = int(input(f"{self.getName()}: "))
            if answer <= 10 and answer > 0:
                return answer
            else: 
                print("Please choose a number between 1 and 10")
                return self.chooseAnswer()

    def playerWon(self):
        self.__points += 1
        print(f"{self.getName()} Won ! Current score: {self.getPoints()}")

class Game():

    def __init__(self):
        self.__rounds = 0
        self.__players = []

    def setPlayers(self, players):
        [self.__players.append(player) for player in players]
        return self
    
    def nextRound(self):
        self.__rounds +=1 