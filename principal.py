import os, random, sys, math
import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACIAS import *
from menu_mejorado import *
from High_Score_Module import *

#Funcion principal
def principal():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("El juego del Mago Goma...")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        fondo = pygame.image.load("fondo.jpg").convert()

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        T_inicio=pygame.time.get_ticks()

        puntos = 0
        palabraUsuario = ""
        lemarioEnSilabas=[]
        listaPalabrasDiccionario=[]

        archivo= open("lemario.txt","r")
        archivo2= open ("lemarioSilabas.txt","r")

        #lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario)

        #lectura del archivo en silabas
        lectura(archivo2, lemarioEnSilabas)

        #elige una al azar
        palabraEnSilabas=nuevaPalabra(lemarioEnSilabas)
        palabraActual=silabasTOpalabra(palabraEnSilabas)

        dibujar(screen, palabraUsuario, palabraActual, puntos,segundos)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #pasa la palabra a silabas
                        palabraUsuarioEnSilabas=palabraTOsilaba(palabraUsuario)
                        #chequea si es correcta y suma o resta puntos
                        puntos += procesar(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario)
                        #busca la ultima silaba y busca una palabra que empiece asi
                        silaba=dameUltimaSilaba(palabraUsuarioEnSilabas)
                        palabraEnSilabas=buscarPalabraQueEmpieceCon(silaba,lemarioEnSilabas)
                        palabraActual=silabasTOpalabra(palabraEnSilabas)
                        palabraUsuario = ""

            #segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000
            segundos = TIEMPO_MAX - (pygame.time.get_ticks()-T_inicio)/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, palabraUsuario, palabraActual,puntos,segundos)

            pygame.display.flip()

        while 1:
            if(segundos>=TIEMPO_MAX):
                    X = ANCHO
                    Y = ALTO
                    WHITE = (255, 255, 255)
                    BLACK = (0, 0, 0)

                    font = pygame.font.Font("dejavu.ttf", 16)
                    screen = pygame.display.set_mode((X, Y))
                    pygame.display.set_caption("El juego del Mago Goma...")
                    screen = pygame.display.set_mode((ANCHO, ALTO))
                    fondo = pygame.image.load("fondo.jpg").convert()
                    screen.blit(fondo,(0,0))
                    my_score = puntos
                    highscore(screen, 'score_file.txt', my_score)
                    txt_surf = font.render("Ready to continue...", True, WHITE)
                    txt_rect = txt_surf.get_rect(center=(X//2, Y//2))
                    screen.blit(txt_surf, txt_rect)
                    pygame.display.flip()
                    #pygame.quit()
                    return
            else:
                #Esperar el QUIT del usuario
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                        X = ANCHO
                        Y = ALTO
                        WHITE = (255, 255, 255)
                        BLACK = (0, 0, 0)

                        font = pygame.font.Font("dejavu.ttf", 16)
                        screen = pygame.display.set_mode((X, Y))
                        pygame.display.set_caption("El juego del Mago Goma...")
                        screen = pygame.display.set_mode((ANCHO, ALTO))
                        fondo = pygame.image.load("fondo.jpg").convert()
                        screen.blit(fondo,(0,0))
                        my_score = puntos
                        highscore(screen, 'score_file.txt', my_score)
                        txt_surf = font.render("Ready to continue...", True, WHITE)
                        txt_rect = txt_surf.get_rect(center=(X//2, Y//2))
                        screen.blit(txt_surf, txt_rect)
                        pygame.display.flip()
                        #pygame.quit()
                        return
        if (0>segundos):
             puntos=0
             segundos=0
             mostrar_menu()
        archivo.close()
        archivo2.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    comenzar_nuevo_juego()
