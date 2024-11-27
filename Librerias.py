import random
import pygame
from config_naval import*




def dibujar_grilla(ventana, grilla):
    for fila in range(10):
        for columna in range(10):
            x = 100 + columna * tam_celda
            y = 100 + fila * tam_celda
            
            'Determina el color de la casilla'
            if grilla[fila][columna] == 0 or grilla[fila][columna] == 1 :  
                color = (255, 255, 255)
            elif grilla[fila][columna] == -2:  
                color = (255, 0, 0)
            elif grilla[fila][columna] == -1:
                color = (0, 0, 255)

            'Dibujar el rectángulo de la celda'
            pygame.draw.rect(ventana, color, (x, y, tam_celda - 2, tam_celda - 2))


def verificar_posicion(grilla, fila, columna, tamaño, orientacion):
    "Verificar si el barco cabe dentro de la grilla"
    valido = True

    if orientacion == "horizontal":
        if columna + tamaño > 10:
            valido= False
    elif orientacion == "vertical":
        if fila + tamaño > 10:
            valido = False

    "Verificar que no haya barcos en las posiciones del barco o alrededor"
    for i in range(-1, 2):  
        for j in range(-1, tamaño + 1):  
            if orientacion == "horizontal":
                fila_check = fila + i
                columna_check = columna + j
            elif orientacion == "vertical":
                fila_check = fila + j
                columna_check = columna + i

            "Verificar si la posición está dentro de los límites"
            if 0 <= fila_check < 10 and 0 <= columna_check < 10:
                if grilla[fila_check][columna_check] != 0:  
                    valido = False

    return valido



'Sirve para colocar las naves en las posiciones validadas'
def colocar_nave(grilla, fila, columna, tamaño, orientacion):

    id_nave = len(coordenadas_naves) + 1
    coordenadas_naves[id_nave] = []


    if orientacion == "horizontal":
        for i in range(tamaño):
            grilla[fila][columna + i] = 1
            coordenadas_naves[id_nave].append((fila, columna + i))

    elif orientacion == "vertical":
        for i in range(tamaño):
            grilla[fila + i][columna] = 1
            coordenadas_naves[id_nave].append((fila +i, columna))


'Coloca todas las naves en el tablero'
def colocar_todas_las_naves(grilla):
    
    for tipo in naves:
        cantidad, tamaño = naves[tipo]

        for _ in range(cantidad):
            colocado = False

            while not colocado:
                fila = random.randint(0, 9)
                columna = random.randint(0, 9)
                orientacion = random.choice(["horizontal", "vertical"])

                if verificar_posicion(grilla, fila, columna, tamaño, orientacion):
                    colocar_nave(grilla, fila, columna, tamaño, orientacion)
                    
                    colocado = True

            

    return grilla



'Recorre la matriz (tablero) y muestra los valores'
def mostrar_tablero(grilla):

    for i in range(len(grilla)):

        for j in range(len(grilla[i])):

            print(grilla[i][j], end=" ")
            
        print("")


'crea el texto para ir sumando el puntaje '
def crear_marcador(ventana, texto, tamanaño, x, y):
    fuente = pygame.font.SysFont("serif",tamanaño)
    text_surface = fuente.render(texto,True,(0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midleft = (x,y)
    ventana.blit(text_surface,text_rect)


def nueva_grilla(filas,columnas):

    grilla= []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = 0
            fila += [valor]
        grilla += [fila]  

    return grilla
    


'crea un archivo con el nombre del jugador y su puntaje'

def crear_archivo_puntaje(puntaje):
    archivo = open('puntaje.txt','w')

    archivo.write(f"Jugador: {jugador}\nTu Puntaje es: {puntaje}\nJugador 2: {jugador2}\nTu Puntaje es:{puntaje2}\nJugador 3: {jugador3}\nTu Puntaje es:{puntaje3}  ")

    archivo.close()
  

'permite al usuario escribir'
def ingresar_jugador(event):
   
    global jugador

    if event.key == pygame.K_BACKSPACE:
        jugador = jugador[:-1]  
    elif event.key == pygame.K_RETURN:
        print(f"Texto ingresado: {jugador}")  
    else:
        jugador += event.unicode


'crea una caja de color gris en donde el usuario ingresa su nombre'
def boton_jugador(ventana,tamaño):

    font = pygame.font.SysFont("serif",tamaño)
    boton_texto = pygame.Rect(300, 200, 200, 50)    
    pygame.draw.rect(ventana, (169,169,169), boton_texto)
    text_surface = font.render(jugador, True, (0,0,0))
    ventana.blit(text_surface, (boton_texto.x + 5, boton_texto.y + 5))

def crear_grilla(filas, columnas):

    grilla= []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = 0
            fila += [valor]
        grilla += [fila]  

    return grilla


    

    