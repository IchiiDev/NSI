import math
import matplotlib.pyplot as plt
import numpy as np
import turtle as t

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

    def getY(self, x):
        alpha = self.alpha * math.pi / 180
        return -1 / 2 * self.G * x ** 2 / ((math.cos(alpha))**2 * self.v ** 2) + math.tan(alpha) * x * self.h


    def tracerTrajectoire(self, xmax, n):
        """
        Représenter la trajectoire
        xmax : valeur maximale pour tracer la courbe
        n : nombre de points sur la courbe
        """
        liste_X = np.linspace(0, xmax, n)
        liste_Y = [ self.getY(x) for x in liste_X]
        plt.figure()
        plt.plot(liste_X, liste_Y)
        plt.grid()
        plt.xlabel("Distance d")
        plt.ylabel("Hauteur y")
        plt.legend()
        plt.show()
                
    def animerTrajectoire(self, xmax, n, e):
        """
        Animer la trajectoire
        xmax : valeur maximale pour tracer la courbe
        n : nombre de points sur la courbe
        e : coefficient de mise à l'échelle
        """
        liste_X = np.linspace(0, xmax, n)
        liste_Y = [ self.getY(x) for x in liste_X]
        t.speed("slowest")
        t.up()
        t.goto(liste_X[0] * e, liste_Y[0] * e)
        t.down()
        for k in range(1, n):
            t.goto(liste_X[k] * e, liste_Y[k] * e)
        t.done()

