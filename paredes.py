'''
crear paredes
'''
import random as rnd
#constantes
def imprimirTablero(tablero):
    for line in tablero:
        for element in line:
            print(element,end = "\t")
        print()

#generar clase
class rectangulo:
    #inicializar
    def __init__(self, x,y,ancho,alto):
        self.x=x
        self.y=y
        self.xF=x+ancho
        self.yF=y+alto
        #checar si esta en el bloque
    def checkIfInBlock(self,x,y):
        if x in range(self.x, self.xF+1) and y in range(self.y,self.yF+1):
            return True
        else:
            return False
def ponerBloque(tablero, bloque):
    for y in range(len(tablero)):
        for x in range(len(tablero[0])):
            if bloque.checkIfInBlock(x,y):
                tablero[y][x]='a'
    return tablero

