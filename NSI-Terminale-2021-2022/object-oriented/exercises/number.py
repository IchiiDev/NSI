import random

class Player():

    def __init__(self, name, robot=False):
        self.__name = name
        self.__points = 0
        self.__robot = robot
    
    def getName(self):
        return self.__name

    def chooseAnswer(self):
        if self.__robot == True:
            return random.randint(1, 10)
        else:    
            answer = int(input(f"{self.getName()}: "))
            if answer <= 10 and answer > 0:
                return answer
            else: 
                print("Please choose a number between 1 and 10")
                return self.chooseAnswer()
    
    def getPoints(self):
        return self.__points
    
    def playerWon(self):
        self.__points += 1
        print(f"{self.getName()} Won ! Current score: {self.getPoints()}")


class Game():
    
    def __init__(self):
        self.__round = 0
        self.__players = []

    def setPlayers(self, players):
        [self.__players.append(player) for player in players]
        return self

    def nextRound(self):
        self.__round += 1
        print(f"----------------------\nRound {self.__round}")
        random.shuffle(self.__players)
        answers = []
        for player in self.__players:
            answers.append(player.chooseAnswer())
        print(f"{self.__players[0].getName()}: {answers[0]} - {self.__players[1].getName()}: {answers[1]}")
        self.__players[1].playerWon() if answers[1] == answers[0] else self.__players[0].playerWon()
        print("----------------------")


if __name__ == "__main__":
    player1 = Player("Ethan", True)
    player2 = Player("Roger", True)

    game = Game().setPlayers([player1, player2])

    [game.nextRound() for _ in range(5)]
