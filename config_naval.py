import random
import pygame








run = True
estado = "menu"
tam_celda = 40
ancho = 800
alto= 600
puntaje = 0
puntaje2= -10
puntaje3 = 40



primero = ""
segundo = ""
tercero = ""
puntaje_primero = 0
puntaje_segundo = 0
puntaje_tercero = 0

jugador = ""
jugador2 = "Jose"
jugador3 = "Raul"
 
coordenadas_naves = {}

naves = {
    "submarinos": (4, 1,),
    "destructores": (3, 2,),
    "cruceros": (2, 3,),
    "acorazado": (1, 4,),
}

