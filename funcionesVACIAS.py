from principal import *
from configuracion import *
import random
from funcionesSeparador import *
import math

def musica(): #definimos la funcion de musica
    pygame.mixer.music.load("sound_1.mp3")#desde el pygame, utilizamos su funciÃ³n mixer para cargar un sonido o tema en este caso sound_1.mp3 extraido de un juego de kirby
    pygame.mixer.music.play(-1)#mixer.music.play -1 el parametro sirve para colocarlo en un bucle infinito

def sonidoTrue(): #variable sonido True si el usuario ingresa una palabra correcta
    sonido = pygame.mixer.Sound("Pass.wav")#desde el pygame, utilizamos su funciÃ³n mixer para cargar un sonido  Pass.wav extraido del juego de sonic
    sonido.play(0)#a la variable sonido la reproducimos una sola vez

def sonidoFalse():
    sonido = pygame.mixer.Sound("Miss.wav")
    sonido.play(0)

def lectura(archivo, salida):#en esta funcion tomamos 2 parametros el
    lista=archivo.readlines()#el parametro de archivo abre el documento en modo de lectura, y ahora lo almcenamos en una lista
    for elemento in lista:  #recorremos cada elemento en la lista
        tam=len(elemento)#a cada elemento medimos el tamaÃ±o del string
        f = elemento[:tam -1]#y a ese strin le restamos 1 caracter, para que se elimine el salto de linea '\n' con el que se cargÃ³ en la lista "lista" y lo guardamos en una variable f
        salida.append(f)#a esa variable f la almacenamos en el final de la lista creada por el segundo parametro
def nuevaPalabra(silabas):
    palabra=random.choice(silabas) #elige una opciÃ³n al azar de la lista que recibe como parametro
    return palabra#devuelta la palabra aleatoria

def silabasTOpalabra(silaba):#convierte una palabra en silabas en un string completo, ignora el caracter "-" y los anida en una variable nueva llamada "palabra" y la retorna al final
    palabra=""
    for character in silaba:
        if(character!="-"):
            palabra=palabra+character
    return palabra

#Opcional
def palabraTOsilaba(palabra):
    nueva=separador(palabra)
    return nueva



def dameUltimaSilaba(enSilabas):
    contGuion=0
    ultima=""
    ultimaAlReves=""
    tamPal=len(enSilabas)-1
    for letra in enSilabas:
        if(letra=="-"):
            contGuion=contGuion+1
    if(contGuion>=1):
        for posicion in range(tamPal,-1,-1):
            if(enSilabas[posicion]!="-"):
                ultimaAlReves=ultimaAlReves+enSilabas[posicion]
            else:
                for letra in ultimaAlReves:
                    ultima=letra+ultima
                return ultima
    else:
        return enSilabas

def damePrimeraSilaba(enSilabas):
    primera=""
    tamPrimerSilaba=len(enSilabas)
    if(tamPrimerSilaba>2):
        for posicion in range(tamPrimerSilaba-1):
            if(posicion>=0 and posicion<=4):
                if(enSilabas[posicion]!="-"):
                    primera=primera+enSilabas[posicion]
                else:
                    return primera
    else:
        if(tamPrimerSilaba>=0 and tamPrimerSilaba<=2):
            for posicion in range(tamPrimerSilaba-1):
                if(posicion>=0 and posicion<=3):
                    if(enSilabas[posicion]!="-"):
                        primera=primera+enSilabas[posicion]
                    else:
                        return primera
        primera=enSilabas
        return primera

def esValida(palabraUsuario, palabraUsuarioEnSilabas, palabraEnSilabas, listaPalabrasDiccionario):
    #en esta funcion ejecutamos el desconfio incluido para determinar la validez de una palabra
    #tenemos una bandera inicializada en false
    #hacemos un for de palabra por palabra si el usuario ingreso una que exista en el lemario, si la palabra del usuario estÃ¡
    #la bandera se pasa a verdadero, ahora si la ultima silaba de la palabra actial, coincide con la primer silaba ingresada por el usuario
    #el deconfio funciona de manera que si el usuario no ingresa desconfio entra normalmente al condicional
    #de caso contrario, primero certificamos que el usuario ingresÃ³ desconfio porque lo necesitaba como palabra y no como desahogue que cree que no exista ninguna palabra mÃ¡s
    #si el usuario no lo ingreso de forma que es una respuesta, el programa toma una silaba mala
    #(ultima silaba de la palabra actual ejemplo: correr y no existe ninguna palabra en espaÃ±ol que empiece en RRER) por lo tanto si no encuentra
    #una palabra que comience con RRER, toma el desconfio vÃ¡lido y suma puntos al jugador.
    bandera=False
    if(palabraUsuario!="desconfio"):
        for palabra in listaPalabrasDiccionario:
            if (palabraUsuario==palabra):
                bandera=True
        if(bandera):
            primerSilabaUsuario=damePrimeraSilaba(palabraUsuarioEnSilabas)
            ultimaSilabaPalabra=dameUltimaSilaba(palabraEnSilabas)
            if (primerSilabaUsuario==ultimaSilabaPalabra):
                sonidoTrue() #Ejecuta la funcion la cual contiene el sonido Pass asignado si acerto la palabra
                return True
        else:
            sonidoFalse()
            return False
    else:
        for palabra in listaPalabrasDiccionario:
            if (palabraUsuario==palabra):
                bandera=True
        if(bandera):
            primerSilabaUsuario=damePrimeraSilaba(palabraUsuarioEnSilabas)
            ultimaSilabaPalabra=dameUltimaSilaba(palabraEnSilabas)
            if (primerSilabaUsuario==ultimaSilabaPalabra):
                sonidoTrue()
                return True
        else:
            silabaMala=dameUltimaSilaba(palabraEnSilabas)
            #en caso que sea desconfio de palabra intencional por el usuario (como forma de posible respuesta) agarra la Ãºltima sÃ­laba de la palabra actual (la cual se desconfia)
            # de la palabra en cuestion y verifica si existe una palabra que
            # comience con esta Ãºltima silaba no es vÃ¡lido el desconfio, caso contrario da puntos al jugador
            lemario_en_silabas=lemarioSilabasExpress()
            palabras_en_silaba_lemario=buscarPalabraQueEmpieceCon(silabaMala,lemario_en_silabas)
            primerSilabaPalabraLemario=damePrimeraSilaba(palabras_en_silaba_lemario)
            if(primerSilabaPalabraLemario==silabaMala):
                sonidoFalse()
                return False
            else:
                sonidoTrue()
                return True


def lemarioSilabasExpress(): #usamos esta funcion para llamar de forma expres al lemario en silabas y asÃ­ usarla en esValida caso que sea desconfio
    lemarioEnSilabas=open ("lemarioSilabas.txt","r")#abrimos el lemario en silabas en una lista
    salida=[]#creamos una lista vacia para cargar todo el lemario
    for palabra in lemarioEnSilabas:#recorremos palabra por palabra en silaba
        tam=len(palabra)#tomamos el tamaÃ±o de la palabra para poder quitarle el Ãºltimo caractÃ©r
        f = palabra[:tam -1]#eliminamos el ultimo caracter al elemento palabra, y lo almacenamos en una variable f
        salida.append(f)#aÃ±adimos el elemento sin el caracter de salto de linea a la lista creada anteriormente salida
    lemarioEnSilabas.close()#cerramos el archivo para que se complete la funciÃ³n
    return salida#retornamos la lista del lemario en silabas sin saltos de linea (caracter '\n') al final de cada palabra
def Puntos(palabraUsuario,validez):
    if(validez):
        puntos=2**len(dameUltimaSilaba(palabraTOsilaba(palabraUsuario)))#a la ultima silaba de la palabra ingresada por el usuario, saca un len de eso y lo eleva al cuadrado para retornar la variable puntos
    else:
        puntos=-(len(palabraUsuario))#almacena el tamaÃ±o de la palabra pero en numeros negativos para asi restarles al jugador
    return puntos#devuelve la variable puntos

def procesar(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario):
    return Puntos(palabraUsuario,esValida(palabraUsuario, palabraUsuarioEnSilabas, palabraEnSilabas, listaPalabrasDiccionario))

def buscarPalabraQueEmpieceCon(silaba,lemarioEnSilabas):
    palabrasIguales=[]#crea una lista
    for palabra in lemarioEnSilabas:#recorre al lemario en silabas palabra por palabra
        if (silaba==damePrimeraSilaba(palabra)):#si existe una palabra en el lemario que empiece con esta variable silaba
            palabrasIguales.append(palabra)#se la agrega a la lista
    if(len(palabrasIguales)==1):#si encuentra una sola coincidencia retorna esta palabara que encontrÃ³
        return palabrasIguales[0]
    if(len(palabrasIguales)>1):#si encuentra varias palabras que coinciden con la busqueda, devuelve cualquier elemento de la lista cwon
        palabra=random.choice(palabrasIguales)
        return palabra
    if(len(palabrasIguales)==0):
        return nuevaPalabra(lemarioEnSilabas) #en caso que no encuentre ninguna, retorna una nuevapalabra

