'''
crea obstaculos y genera el mapa de distancia para coordenadas validas
'''
from paredes import *
from generarTaberloDistancia import *
import random as rnd
def iniciar():
    ancho=10
    alto=10

    #genero tablero vacio

    tableroObst=[]
    for y in range(alto):
        linea=[]
        for x in range(ancho):
            linea.append(' ')
        tableroObst.append(linea)

    numberObst=rnd.randint(3,5)
    obstacles=[]
    intervaloX=int((ancho/numberObst)//1)
    intervaloY=int((alto/numberObst)//1)
    for i in range(numberObst):
        x=rnd.randint(int(intervaloX*(i)),int(intervaloX*(i+1)))
        y=rnd.randint(int(intervaloY*(i)),int(intervaloY*(i+1)))
        ancho2=rnd.randint(1,5)
        alto2=rnd.randint(1,5)
        obstacles.append(rectangulo(x,y,ancho2,alto2))
        tableroObst=ponerBloque(tableroObst, obstacles[i])
    #imprimirTablero(tableroObst)
    puntoValido=False
    while not(puntoValido):

        xObj=rnd.randint(0,ancho-1)
        yObj=rnd.randint(0,alto-1)
        for obstaculo in obstacles:
            if not(obstaculo.checkIfInBlock(xObj,yObj)):
                puntoValido=True
    tableroObst[yObj][xObj]='o'
    return tableroObst
