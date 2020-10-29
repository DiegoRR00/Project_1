'''
Crear matiz de lejania
'''
import math as mt
#constantes
alto=13
ancho=13
xInicial=6
yInicial=6
def imprimirTablero(tablero):
    for line in tablero:
        for element in line:
            print(element,end = "\t")
        print()
def distancia(x,y,xInicial,yInicial):
    deltaX=abs(x-xInicial)
    deltaY=abs(y-yInicial)
    distancia=mt.sqrt(deltaX*deltaX+deltaY*deltaY)
    return distancia
#crear tablero
def crearTablero(alto, ancho, xInicial, yInicial):
    tablero=[]
    for i in range(alto):
        linea=[]
        for j in range(ancho):
            linea.append(0)
        tablero.append(linea)
    #pongo mi incial
    for y in range(alto):
        for x in range(ancho):
            dist=distancia(x,y,xInicial,yInicial)
            tablero[y][x]=int(dist//1)
    return tablero

