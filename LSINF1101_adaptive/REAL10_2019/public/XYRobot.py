from graphics import * # un bibliothèque pour dessiner des figures simple sur un plan XY
import math            # nous avoins besoin des fonctions cos et sin pour notre calcul de la position d'un point

class XYRobot :
    
    def __init__(self,n) :
        self.__nom__ = n           # nom du robot
        self.__x = 0               # position x du robot
        self.__y = 0               # position y du robot
        self.__angle = 0           # angle en degres radius
        self.__win = GraphWin()    # fenêtre graphique sur le chemin du robot sera tracé
        
    def __str__(self) :
        """Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant les coordonnées position du robot."""
        return str(self.getnom())+"@("+str(round(self.getx()))+","+str(round(self.gety()))+") angle: "+str(self.getangle())

    def getnom(self) :
        return self.__nom__

    def getx(self) :
        return self.__x
    
    def gety(self) :
        return self.__y
    
    def getanglerad(self) :
        """returns the angle in radials"""
        return self.__angle

    def getangle(self) :
        """returns the angle in degrees"""
        return ( self.__angle * 180 / math.pi ) % 360
        
    def setx(self,x) :
        self.__x = x
        
    def sety(self,y) :
        self.__y = y

    def position(self) :
        return (self.getx(),self.gety())

    def __drawFrom(self,oldx,oldy) :
        line = Line(Point(oldx,oldy),Point(self.getx(),self.gety()))
        line.draw(self.__win)
        
    def __move(self,distance,sense) :
        """ méthode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            si sense = 1  il avance de distance pixels
            si sense = -1 il recule de distance pixels
        """
        oldx = self.getx()
        oldy = self.gety()
        orientationx = math.cos(self.getanglerad())
        orientationy = math.sin(self.getanglerad())
        self.setx(oldx + orientationx * distance * sense)
        self.sety(oldy + orientationy * distance * sense)
        self.__drawFrom(oldx,oldy)

    def moveforward(self,distance) :
        """ fait avancer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.__move(distance,1)

    def movebackward(self,distance) :
        """ fait reculer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.__move(distance,-1)

    def __turn(self,direction) :
        """ méthode auxiliaire pour les méthodes turnright() et turnleft()
            si direction = 1 elle change l'angle du robot de 90 degrés vers la droite (dans le sens des aiguilles d'une montre)
            si direction = -1 elle change l'angle du robot de 90 degrés vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.__angle = self.__angle + direction * math.pi/2
        
    def turnright(self) :
        """ fait tourner le robot de 90 degrés vers la droite (dans le sens des aiguilles d'une montre)
        """
        self.__turn(1)

    def turnleft(self) :
        """ fait tourner le robot de 90 degrés vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.__turn(-1)

# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)

r2d2 = XYRobot("R2-D2")

# first move to position (100,100) facing East, to be more or less in the center of the window
r2d2.moveforward(100)
r2d2.turnright()
r2d2.moveforward(100)
r2d2.turnleft()

print(r2d2)
#R2-D2@(100, 100) angle: 0.0
r2d2.moveforward(50)
r2d2.turnleft()
print(r2d2)
#R2-D2@(150, 100) angle: 270.0
r2d2.moveforward(50)
r2d2.turnleft()
print(r2d2)
#R2-D2@(150.0, 50.0) angle: 180.0
r2d2.moveforward(50)
r2d2.turnleft()
print(r2d2)
#R2-D2@(100.0, 50.0) angle: 90.0
r2d2.moveforward(50)
print(r2d2)
#R2-D2@(100, 100) angle: 90.0
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)