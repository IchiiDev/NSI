import random

class Player():
    
    def __init__(self, name, robot=False):
        self.__name = name
        self.__isRobot = robot
        self.__score = 0
        self.__number = None
        self.__last_answer = None

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

    def setLastAnswer(self, answer):
        assert type(answer) == list
        self.__last_answer = answer

    def chooseAnswer(self, isFirstRound=False):
        if self.isRobot() == True:
            if isFirstRound == True:
                print(f"{self.getName()} chose a number...")
                return random.randint(1, 10)
            else:
                return
        else:    
            answer = int(input(f"{self.getName()}: "))
            if answer <= 10 and answer > 0:
                return answer
            else: 
                print("Please choose a number between 1 and 10")
                return self.chooseAnswer()

    def playerWon(self):
        self.__score += 1
        print(f"{self.getName()} Won ! Current score: {self.getScore()}")

class Game():

    def __init__(self, maxRound):
        self.__rounds = 0
        self.__maxRound = maxRound
        self.__players = []

    def setPlayers(self, players):
        [self.__players.append(player) for player in players]
        return self
    
    def nextRound(self):
        self.__rounds +=1 
        if self.__rounds > self.__maxRound: 
            self.__players[0].playerWon()
            return
        if self.__rounds == 1:
            number = self.__players[0].chooseAnswer()
            self.__players[0].setNumber(number)

            answer = self.__players[1].chooseAnswer()
            if answer == self.__players[0].getNumber():
                self.__players[1].playerWon()
                return
            elif answer > self.__players[0].getNumber():
                print("Lesser !")
                self.__players[1].setLastAnswer([answer, "-"])
                self.nextRound()
            else:
                print("Greater!")
                self.__players[1].setLastAnswer([answer, "-"])
                self.nextRound()
        else:
            answer = self.__players[1].chooseAnswer()
            if answer == self.__players[1].getNumber():
                self.__players[1].playerWon()
            elif answer > self.__players[0].getNumber():
                print("Lesser!")
                self.__players[1].setLastAnswer([answer, "-"])
                self.nextRound()
            else:
                print("Greater !")
                self.__players[1].setLastAnswer([answer, "-"])
                self.nextRound()

    def startGame(self):
        random.shuffle(self.__players)
        
        self.__rounds == 0
        [player.setNumber(None) for player in self.__players]
        self.nextRound()


if __name__ == "__main__":
    player1 = Player("Ethan")
    player2 = Player("Roger", True)

    game = Game(5).setPlayers([player1, player2])
    game.startGame()