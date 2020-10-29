'''
CRear ventana de menu e inciar nivel
'''
import pygame
import time as tm
from gameMechanics import *
class Boton:
    def __init__(self, x, y, alto , ancho, color):
        self.x=x
        self.y=y
        self.alto=alto
        self.ancho=ancho
        self.color=color
    def checkClick(self, pos):
        if pos[0] in range(self.x,self.x+self.ancho) and pos[1] in range(self.y,self.y+self.alto):
            return True
        else:
            return False
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Menu Project 1")
win.fill((0,20,200))
startButton=Boton(250-45,250-60,30,90,(255,0,255))
loadButton=Boton(250-45,250-15,30,90,(255,0,255))

quitButton=Boton(250-45,250+30,30,90,(255,0,255))
font=pygame.font.Font('freesansbold.ttf',15)
text=font.render('Start game',True,(20,20,20),startButton.color)
font2=pygame.font.Font('freesansbold.ttf',15)
text2=font.render('Quit game',True,(20,20,20),quitButton.color)
text3=font.render('Load game',True,(20,20,20),loadButton.color)
textRect=text.get_rect()
textRect.center=(250,205)
text2Rect=text.get_rect()
text2Rect.center=(250,295)
text3Rect=text.get_rect()
text3Rect.center=(250,250)
colorText=(0,0,0)
colorText2=(0,0,0)
colorText3=(0,0,0)
text4=font.render('There\'s no saved games',True,(0,0,0),(255,20,30))
text4Rect=text.get_rect()
text4Rect.center=(250,250)
running=True
errorCarga=0
while running:
    pygame.time.delay(10)
    pygame.display.update()
    
    for event in pygame.event.get():
        position=pygame.mouse.get_pos()
        if event.type== pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEMOTION:
            if startButton.checkClick(position):
                startButton.color=(0,0,0)
                colorText=(200,200,200)
            elif quitButton.checkClick(position):
                quitButton.color=(255,0,0)
                colorText2=(200,200,200)
            elif loadButton.checkClick(position):
                loadButton.color=(0,0,0)
                colorText3=(200,200,200)
            else:
                startButton.color=(255,0,255)
                colorText=(0,0,0)
                quitButton.color=(255,0,255)
                colorText2=(0,0,0)
                loadButton.color=(255,0,255)
                colorText3=(0,0,0)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if startButton.checkClick(position):
                startLevel(0)
                win.fill((0,20,200))
                startButton.color=(255,0,255)
                colorText=(0,0,0)
                win=pygame.display.set_mode((500,500))
            elif quitButton.checkClick(position):
                running=False
            elif loadButton.checkClick(position):
                board=loadGame()
                if board == 0:
                    errorCarga=1
                else:
                    startLevel(board)
    win.fill((0,20,200))
    if errorCarga==1:
        win.fill((0,20,200))
        pygame.draw.rect(win,(255,20,30),(250-100,250-70,200,140))
        text4=font.render('There\'s no saved games',True,(0,0,0),(255,20,30))
        text4Rect=text.get_rect()
        text4Rect.center=(205,250)
        win.blit(text4,text4Rect)
        pygame.display.update()
        tm.sleep(1.5)
        errorCarga=0
    pygame.draw.rect(win,startButton.color,(startButton.x,startButton.y,startButton.ancho,startButton.alto))
    text=font.render('Start game',True,colorText,startButton.color)
    pygame.draw.rect(win,quitButton.color,(quitButton.x,quitButton.y,quitButton.ancho,quitButton.alto))
    text2=font.render('Quit game',True,colorText2,quitButton.color)
    pygame.draw.rect(win,loadButton.color,(loadButton.x, loadButton.y, loadButton.ancho, loadButton.alto))
    text3=font.render('Load game',True,colorText3, loadButton.color)
    win.blit(text,textRect)  
    win.blit(text2,text2Rect)
    win.blit(text3,text3Rect)
pygame.quit()