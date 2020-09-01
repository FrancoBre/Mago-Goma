import random
import pygame
from pygame.locals import *
from principal import *
from configuracion import *
from High_Score_Module import *
from funcionesVACIAS import *

class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (255, 255, 255))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 200, 200))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = (ANCHO/2)-50
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(1)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    "Representa un menÃº con opciones para un juego"

    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('dejavu.ttf', 20)
        x = (ANCHO/2)-50
        y = (ALTO/2)-50
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la funciÃ³n asociada a la opciÃ³n.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor estÃ© entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opciÃ³n del menÃº."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)

def comenzar_nuevo_juego():
    print (" FunciÃ³n que muestra un nuevo juego.")
    principal()


def mostrar_opciones():
    print (" FunciÃ³n que muestra otro menÃº de opciones.")

def records():
                    X = ANCHO
                    Y = ALTO
                    WHITE = (255, 255, 255)
                    BLACK = (0, 0, 0)

                    font = pygame.font.Font("dejavu.ttf", 16)
                    screen = pygame.display.set_mode((X, Y))
                    pygame.display.set_caption("El juego del Mago Goma...")
                    fondo = pygame.image.load("fondo.jpg").convert()
                    screen.blit(fondo,(0,0))

                    show_top10(screen, 'score_file.txt')

                    txt_surf = font.render("Ready to continue...", True, WHITE)
                    txt_rect = txt_surf.get_rect(center=(X//2, Y//2))
                    screen.blit(txt_surf, txt_rect)
                    pygame.display.flip()
                    totaltime = 0
                    puntos=0

def salir_del_programa():
    print (" Gracias por utilizar este programa.")
    pygame.quit()
    sys.exit(0)


def mostrar_menu():

    global salir
    salir = False

    global opciones
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("configuracion", mostrar_opciones),
        ("Mejores records", records),
        ("Salir", salir_del_programa)
        ]

    pygame.font.init()
    pygame.display.set_caption("El juego del Mago Goma...")
    global screen
    screen = pygame.display.set_mode((ANCHO, ALTO))
    global fondo
    fondo = pygame.image.load("fondo.jpg").convert()
    global menu
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)

if __name__ == "__main__":
    musica()
    mostrar_menu()