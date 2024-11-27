import pygame
from config_naval import *
from Librerias import* #dibujar_grilla, colocar_todas_las_naves, mostrar_tablero,marcador, nueva_grilla,crear_archivo_puntaje



pygame.init()

ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Batalla Naval")

'Musica de Fondo'
pygame.mixer.music.load("Proyecto_pygame/Density-_-Time-MAZE-♫-NO-COPYRIGHT-8-bit-Music.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.03)
acierto = pygame.mixer.Sound("Proyecto_pygame2/boom3.wav")
fallo = pygame.mixer.Sound("Proyecto_pygame2/WR_gun_water_impact01.ogg")



'asigna a las variables la imagen de los botones'
inicio_img = pygame.image.load('Proyecto_pygame2/jugar.png').convert_alpha()
salir_img= pygame.image.load('Proyecto_pygame2/salir.png').convert_alpha()
nivel_img= pygame.image.load('Proyecto_pygame2/nivel.png').convert_alpha()
puntaje_img= pygame.image.load('Proyecto_pygame2/puntaje.png').convert_alpha()
reiniciar_img = pygame.image.load('Proyecto_pygame2/reiniciar.png').convert_alpha()
volver_img = pygame.image.load('Proyecto_pygame2/atras.png').convert_alpha()
volumen_img = pygame.image.load('Proyecto_pygame2/mute-volume-control.png').convert_alpha()
icono_img = pygame.image.load('Proyecto_pygame2/DALL·E-2024-11-27-12.43.png').convert_alpha()

'asigna imagen al fondo'
fondo_img = pygame.image.load('Proyecto_pygame/fondo_agua.png').convert_alpha()
fondo_img = pygame.transform.scale(fondo_img,(ancho,alto))
volumen_img = pygame.transform.scale(volumen_img,(40,40))
icono_img = pygame.transform.scale(icono_img,(150,150))


'asigna una posicion a las imagenes'
rect_inicio = inicio_img.get_rect()
rect_inicio.x = 335
rect_inicio.y = 250
rect_salir = salir_img.get_rect()
rect_salir.x = 335
rect_salir.y = 445
rect_nivel = nivel_img.get_rect()
rect_nivel.x = 335
rect_nivel.y = 315                                                                                 #Punto F e I 
rect_puntaje = puntaje_img.get_rect()
rect_puntaje.x = 335
rect_puntaje.y = 380
rect_reiniciar = reiniciar_img.get_rect()
rect_reiniciar.x = 550
rect_reiniciar.y = 500
rect_volver = volver_img.get_rect()
rect_volver.x = 100
rect_volver.y = 515
rect_volver2 = volver_img.get_rect()
rect_volver2.x = 100
rect_volver2.y = 500
rect_volumen = volumen_img.get_rect()
rect_volumen.x = 100
rect_volumen.y = 500
rect_icono= icono_img.get_rect()
rect_icono.x = 325
rect_icono.y = 40

font = pygame.font.SysFont("serif",50)





while run == True:



    if estado == "menu":
        'Le da imagen y posicion (fondo - botones)'
        ventana.blit(fondo_img,(0,0))
        ventana.blit(inicio_img,rect_inicio)
        ventana.blit(salir_img,rect_salir)
        ventana.blit(nivel_img,rect_nivel)
        ventana.blit(puntaje_img,rect_puntaje)
        ventana.blit(volumen_img,rect_volumen)
        ventana.blit(icono_img,rect_icono)
        boton_jugador(ventana,30)
        
        

    elif estado == "grilla":
        
        ventana.blit(fondo_img,(0,0)) 
        ventana.blit(reiniciar_img,rect_reiniciar)
        crear_marcador(ventana,str(puntaje),50,625,200)
        dibujar_grilla(ventana,grilla)
        ventana.blit(volver_img,rect_volver)
        
        
 
    elif estado == "grilla_reiniciada":
 
        
        puntaje = 0
        colocar_todas_las_naves(grilla)
        mostrar_tablero(grilla)
        print("-------------------")
        estado = "grilla"
        

    elif estado == "ver_puntaje":
        ventana.blit(fondo_img,(0,0))
        
        crear_archivo_puntaje(puntaje) 
        ventana.blit(volver_img,rect_volver2)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN and estado == "menu":
            ingresar_jugador(event)



        'detectar clicks en la grilla'
        if event.type == pygame.MOUSEBUTTONDOWN and estado == "grilla":
            coordenadas_click = pygame.mouse.get_pos()
            columna = (coordenadas_click[0] - 100) // tam_celda
            fila = (coordenadas_click[1] - 100) // tam_celda

            if rect_reiniciar.collidepoint(coordenadas_click) == True:  
                
                crear_archivo_puntaje(puntaje) 
                estado = "grilla_reiniciada"
                grilla = nueva_grilla(10,10)

            if rect_volver.collidepoint(coordenadas_click) == True :

                crear_archivo_puntaje(puntaje)    
                estado = "menu"
                
            'Verificar que el clic esté dentro de la grilla'
            if 0 <= fila < 10 and 0 <= columna < 10:

           
                if grilla [fila][columna] == 1:
                    grilla [fila][columna] = -2
                    print([fila],[columna])
                    acierto.play()
                    puntaje += 5  

                elif grilla [fila][columna] == 0:
                    grilla [fila][columna] = -1
                    puntaje -= 1     
                    fallo.play()

                elif grilla[fila][columna] in [-1,-2]:
                    print(f"La celda [{fila}, {columna}] ya fue golpeada.")

                naves_hundidas = []  
                for id_nave, coordenadas in coordenadas_naves.items():
                    contador_golpes = 0  

                    for fila_nav, columna_nav in coordenadas:
                        if grilla[fila_nav][columna_nav] == -2:  
                            contador_golpes += 1

                    
                    if contador_golpes == len(coordenadas):
                        print(f"Nave {id_nave} hundida.")
                        puntaje += len(coordenadas) * 10  
                        naves_hundidas.append(id_nave)  

                
                for id_nave in naves_hundidas:
                    coordenadas_naves.pop(id_nave)
                            



        'Detecta cuando presionamos el boton'
        if event.type == pygame.MOUSEBUTTONDOWN and estado == "menu":
            coordenadas_click = pygame.mouse.get_pos()

            if  rect_inicio.collidepoint(coordenadas_click) == True:
                
                estado = "grilla"
                grilla = nueva_grilla(10,10)
                puntaje = 0
                grilla = colocar_todas_las_naves(grilla)
                mostrar_tablero(grilla)
                
                print("-------------------")
                
            if rect_salir.collidepoint(coordenadas_click) == True:
                run = False

            if rect_puntaje.collidepoint(coordenadas_click) == True:
                estado = "ver_puntaje"

                crear_archivo_puntaje(puntaje)
            
            if rect_nivel.collidepoint(coordenadas_click) == True:
                print("WIP - no creo llegar")

            if rect_volumen.collidepoint(coordenadas_click) == True:
                pygame.mixer.music.set_volume(0)
                


        if event.type == pygame.MOUSEBUTTONDOWN and estado == "ver_puntaje":
            coordenadas_click = pygame.mouse.get_pos()

            if rect_volver2.collidepoint(coordenadas_click)== True:
                estado = "menu"


    pygame.display.update()


pygame.quit()