'''
Crea la ventana y reproduce sonidos
'''
import time as tm
import math as mt

import pygame

from generarTaberloDistancia import *
from iniciarNivel import *
from nivelPosible import *
from paredes import *
from pauseMenu import *
class Board:
    def __init__(self, board):
        self. board=board
        self.i=[0,0]
        self.o=[0,0]
    def findInO(self):
        for m in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[m][c]=='i':
                    self.i=[c,m]
                elif self.board[m][c]=='o':
                    self.o=[c,m]
        self.p=self.i
    def findMaxNum(self):
        self.maxD=mt.sqrt((len(self.board))**2+(len(self.board[0]))**2)
        self.maxD=int(self.maxD//1)
    def ready(self):
        self.board[self.i[1]][self.i[0]]=' '
        #self.board[self.o[1]][self.o[0]]=' '
    def printMove(self,player1):
        self.board[self.p[1]][self.p[0]]=' '
        self.board[player1.y][player1.x]='p'
        self.p=[player1.x,player1.y]
def getGoodLevel():
#creo mi tableros
    goodLevel= False
    contador=0
    while not(goodLevel):
        obstBoard= iniciar()
        goodLevel= getBoard(obstBoard)
        contador+=1
    return obstBoard

def startLevel(board_2):
    if board_2==0:
        obstacles=getGoodLevel()
    else:
        obstacles=board_2
    obstacleB=Board(obstacles)
    obstacleB.findInO()
    obstacleB.findMaxNum()
    distance= crearTablero(len(obstacles),len(obstacles[0]),obstacleB.o[0],obstacleB.o[1])
    pygame.init()
    #genero lista de sonidos
    sonidos=['do.wav','dos.wav','re.wav','res.wav','mi.wav','mis.wav','fa.wav','fa2.wav','sol.wav','sols.wav','la.wav','las.wav','si.wav','sis.wav','doo.wav','dos2.wav']
    usedSounds=[]
    for i in range(obstacleB.maxD):
        usedSounds.append(pygame.mixer.Sound(sonidos[i]))
    jugador=Player(obstacleB.i[0],obstacleB.i[1])
    window= pygame.display.set_mode((int(len(obstacleB.board)*50-40),int(len(obstacleB.board[0])*50-40)))
    window.fill((0,20,200))
    pygame.display.set_caption("Level")
    running=True
    while ([jugador.x,jugador.y]!=obstacleB.o) and running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        key= pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:
            jugador.moveUp()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            jugador.moveLeft()
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            jugador.moveDown()
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            jugador.moveRight()
        if key[pygame.K_ESCAPE]:
            action=pause(obstacleB.board)
            if action==0:
                running=False

        jugador.checkIfValid(obstacleB.board)
        obstacleB.printMove(jugador)
        window.fill((0,20,200))
        usedSounds[distance[jugador.y][jugador.x]].play()
        pygame.draw.rect(window,(200,0,200),(jugador.x*50,jugador.y*50,10,10))
        pygame.display.update()
    #pygame.quit()
if __name__ == "__main__":

    startLevel()

