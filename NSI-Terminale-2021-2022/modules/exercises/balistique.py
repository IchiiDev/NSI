import math

class projectile:

    G = 9.81

    def __init__(self, alpha, v, h):
        self.alpha = alpha
        self.v = v
        self.h = h
        return
        
    def getDistance(self):
        return (self.v / self.G) * math.cos(self.alpha) * (self.v * math.sin(self.alpha) + math.sqrt((self.v * math.sin(self.alpha))**2 + 2 * self.G * self.h))

    def getFlightTime(self):
        return (self.v * math.sin(self.alpha) + math.sqrt((self.v * math.sin(self.alpha))**2 + 2 * self.G * self.h)) / self.G

    def getMaxHeight(self):
        return (self.v**2 * math.sin(self.alpha)**2) / 2 ** self.G
