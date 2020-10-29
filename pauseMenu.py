import pygame
import csv
import os.path
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
def saveGame(tablero):
    f=open('par1.csv','w') #Abro un archivo par1 y pongo en modo escribir
    for line in tablero:
        for character in line:
            f.write(character) #Guardo tod en la linea
            f.write(',')#Separo cada uno con comas
        f.write('\n') #Cambio de línea
    f.close()
def loadGame():
    tablero=[]
    try:
        f = open('par1.csv')
        f.close()
    except FileNotFoundError:
        return 0
    with open('par1.csv') as archivo:
        lector=csv.reader(archivo,delimiter=',')
        for renglon in lector:
            line=[]
            for element in renglon:
                line.append(element)
            tablero.append(line)
    return tablero
def pause(board):
    pygame.init()
    win=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Pause")
    win.fill((0,20,200))
    continueButton=Boton(250-75,250-60,30,150,(255,0,255))
    saveButton=Boton(250-75,250-15,30,150,(255,0,255))
    menuButton=Boton(250-75,250+30,30,150,(255,0,255))
    font=pygame.font.Font('freesansbold.ttf',15)
    text=font.render('Continue game',True,(20,20,20),continueButton.color)
    font2=pygame.font.Font('freesansbold.ttf',15)
    text2=font.render('Save game',True,(20,20,20),saveButton.color)
    font3=pygame.font.Font('freesansbold.ttf',15)
    text3=font.render('Return to menu',True,(20,20,20),menuButton.color)
    textRect=text.get_rect()
    textRect.center=(250,205)
    text2Rect=text.get_rect()
    text2Rect.center=(250,250)
    text3Rect=text.get_rect()
    text3Rect.center=(250,295)
    colorText=(0,0,0)
    colorText2=(0,0,0)
    colorText3=(0,0,0)
    running=True
    action=1
    while running:
        pygame.time.delay(10)
        pygame.display.update()
        
        for event in pygame.event.get():
            position=pygame.mouse.get_pos()
            if event.type== pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEMOTION:
                if saveButton.checkClick(position):
                    saveButton.color=(0,0,0)
                    colorText2=(200,200,200)
                elif menuButton.checkClick(position):
                    menuButton.color=(255,0,0)
                    colorText3=(200,200,200)
                elif continueButton.checkClick(position):
                    continueButton.color=(0,0,0)
                    colorText=(200,200,200)
                    continueButton
                else:
                    saveButton.color=(255,0,255)
                    colorText=(0,0,0)
                    menuButton.color=(255,0,255)
                    colorText2=(0,0,0)
                    continueButton.color=(255,0,255)
                    colorText3=(0,0,0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if saveButton.checkClick(position):
                    saveGame(board)
                elif continueButton.checkClick(position):
                    running=False

                elif menuButton.checkClick(position):
                    running=False
                    action=0
        win.fill((0,20,200))
        pygame.draw.rect(win,continueButton.color,(continueButton.x,continueButton.y,continueButton.ancho,continueButton.alto))
        text=font.render('Continue Game',True,colorText,continueButton.color)
        pygame.draw.rect(win,saveButton.color,(saveButton.x,saveButton.y,saveButton.ancho,saveButton.alto))
        text2=font.render('Save game',True,colorText2,saveButton.color)
        pygame.draw.rect(win,menuButton.color,(menuButton.x,menuButton.y,menuButton.ancho,menuButton.alto))
        text3=font.render('Back to menu',True,colorText3,menuButton.color)
        win.blit(text,textRect)  
        win.blit(text2,text2Rect)
        win.blit(text3,text3Rect)
    return action