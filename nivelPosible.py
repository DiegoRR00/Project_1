'''
Comprobar que es un nivel posible
'''
from iniciarNivel import *
import time as tm
tConObst=iniciar()
class Player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.lastmove=0
    def moveUp(self):
        self.y-=1
        self.lastmove='w'
    def moveDown(self):
        self.y+=1
        self.lastmove='s'
    def moveLeft(self):
        self.x-=1
        self.lastmove='a'
    def moveRight(self):
        self.x+=1
        self.lastmove='d'
    def checkIfValid(self, tableroObst2):
        if not(self.x in range(0,len(tableroObst2[0]))):
            if self.x<0:
                self.x=0
            else:
                self.x=len(tableroObst2[0])-1
        if not(self.y in range(0,len(tableroObst2))):
            if self.y<0:
                self.y=0
            else:
                self.y=len(tableroObst2)-1
        if tableroObst2[self.y][self.x]=='a':
            if self.lastmove=='w':
                self.y+=1
            elif self.lastmove=='s':
                self.y-=1
            elif self.lastmove=='a':
                self.x+=1
            elif self.lastmove=='d':
                self.x-=1
    def printInTablero(self,tableroPre):
        tableroPre[self.y][self.x]='p'
        return tableroPre

def findXnY(tConObst,x0,y0,dif):
    validCoo=True
    while validCoo:
        x=rnd.randint(0,len(tConObst[0])-1)
        y=rnd.randint(0,len(tConObst)-1)
        if tConObst[y][x]!='a' and distancia(x,y,x0,y0)>dif:
            validCoo=False  
    return x,y
def findXnYObj(tConObst):
    for y in range(len(tConObst)):
        for x in range(len(tConObst[0])):
            if tConObst[y][x]=='o':
                return x,y
def isNotTrapped(tConObst,x,y):
    #crear caso donde est[e en extremo]
    if y!=0:
        izq=tConObst[y-1][x]=='a'
    else:
        izq=True
    if y!=(len(tConObst))-1:
        der=tConObst[y+1][x]=='a'
    else:
        der=True
    if x!=0:
        arr=tConObst[y][x-1]=='a'
    else:
        arr=True
    if x!=(len(tConObst[0]))-1:
        abj=tConObst[y][x+1]=='a'
    else:
        abj=True
    if der and izq and abj and arr:
        return True
    else:
        return False
def simpleDebug(jugador,tConObst):
    tiro=0
    while tiro<10:

        movement=input()
        if movement=='w':
            jugador.moveUp()
        elif movement=='a':
            jugador.moveLeft()
        elif movement=='s':
            jugador.moveDown()
        elif movement=='d':
            jugador.moveRight()
        else:
            tiro=15
        jugador.checkIfValid(tConObst)
        tConObst=jugador.printInTablero(tConObst)
        imprimirTablero(tConObst)
        print()

class AIPlayer(Player):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.xAnt=x-1
        self.yAnt=y-1
        self.lastmove=0
    def imprimirTablero(self,tablero):
        for line in tablero:
            for element in line:
                print(element,end = "\t")
            print()
    def findWay(self,xObj,yObj,tableroObst):
        axis='x'
        move=True
        movements=0
        while (self.x!=xObj or self.y!=yObj) and movements<=30:
            
            if axis=='x':
                currentMove=False
                noMove=False
                #moverse en x
                if self.x<xObj:
                    self.yAnt=self.y
                    self.xAnt=self.x
                    self.moveRight()
                    self.checkIfValid(tableroObst)
                    currentMove=True
                elif self.x>xObj:
                    self.yAnt=self.y
                    self.xAnt=self.x
                    self.moveLeft()
                    self.checkIfValid(tableroObst)
                    currentMove=True
                
                noMove=(self.x==self.xAnt and self.y==self.yAnt)
                if self.x==xObj  or noMove:
                    help=False
                    if self.y<yObj:
                        if tableroObst[self.y+1][self.x]=='a':
                            help=True
                            yEval=self.y+1
                    elif self.y>yObj:
                        if tableroObst[self.y-1][self.x]=="a":
                            help=True
                            yEval=self.y-1
                    if help:
                        while tableroObst[yEval][self.x]=='a' and movements<30:
                            movements+=1
                            if not(self.x+1>len(tableroObst[0])-1):
                                if tableroObst[yEval][self.x+1]!='a' :
                                    move=False
                            if move:
                                self.yAnt=self.y
                                self.xAnt=self.x
                                self.moveRight()
                                self.checkIfValid(tableroObst)
                            else:
                                self.yAnt=self.y
                                self.xAnt=self.x
                                self.moveLeft()
                                self.checkIfValid(tableroObst)                            
                            if self.xAnt==self.x:
                                move=not(move)
                        axis='y'
                if self.xAnt==self.x or self.x==xObj:
                    axis='y'
                if currentMove:
                    movements+=1
                #moverse en y
            elif axis=='y':
                currentMove=False
                if self.y<yObj:
                    
                    self.yAnt=self.y
                    self.xAnt=self.x
                    self.moveDown()
                    self.checkIfValid(tableroObst)
                    currentMove=True
                elif self.y>yObj:
                    self.yAnt=self.y
                    self.xAnt=self.x
                    self.moveUp()
                    self.checkIfValid(tableroObst)
                    currentMove=True
                elif self.y==yObj or (self.x==self.xAnt and self.y==self.yAnt):
                    help=False
                    if self.x<xObj:
                        if tableroObst[self.y][self.x+1]=='a':
                            help=True
                            xEval=self.x+1
                    elif self.x>xObj:
                        if tableroObst[self.y][self.x-1]=="a":
                            help=True
                            xEval=self.x-1
                    if help:
                        while tableroObst[self.y][xEval]=='a' and movements<30:
                            movements+=1
                            if not(self.y+1>len(tableroObst[0])-1):
                                if tableroObst[self.y+1][xEval]!='a' :
                                    move=False
                            if move:
                                self.yAnt=self.y
                                self.xAnt=self.x
                                self.moveUp()
                                self.checkIfValid(tableroObst)
                            else:
                                self.yAnt=self.y
                                self.xAnt=self.x
                                self.moveDown()
                                self.checkIfValid(tableroObst)                                
                            if self.yAnt==self.y:
                                move=not(move)
                        axis='x'
                if self.yAnt==self.y or self.y==yObj:
                    axis='x'
                if currentMove:
                    movements+=1


            self.yAnt=self.y
            self.xAnt=self.x


        if movements>30:
            return False
        else:
            return True
def main1(tConObst):
    x,y=findXnY(tConObst,0,0,0)
    jugador=Player(x,y)
    simpleDebug(jugador,tConObst)
def getBoard(tConObst):
    xo,yo=findXnYObj(tConObst)
    x,y=findXnY(tConObst,xo,yo,5)
    if isNotTrapped(tConObst,xo,yo):
        return False
    tConObst[yo][xo]='o'
    tConObst[y][x]='i'
    imprimirTablero(tConObst)
    ai=AIPlayer(x,y)
    return ai.findWay(xo,yo,tConObst)
O=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],['a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', ' '],['a', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', ' '],[' ', 'a', 'a', 'a', 'a', 'a', ' ', ' ', ' ', ' '],[' ', ' ', 'a', 'a', ' ', 'a', 'a', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', ' ', ' '],[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'o', ' '],[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', ' ', ' '],[' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' ', ' ']]
if __name__ == "__main__":
    print(getBoard(O))