import pygame
import random

# Inicialización de pygame
pygame.init()

# Dimensiones del tablero
ancho_tablero = 13
alto_tablero = 13

# Tamaño de cada celda en el tablero
tamanio_celda = 30  # Puedes ajustar esto según tus preferencias

# Configuración de la pantalla
ancho = ancho_tablero * tamanio_celda
alto = alto_tablero * tamanio_celda
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake Game")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 255, 0)
rojo = (255, 0, 0)

def posicion_inicial(serpiente, manzana):
    serpiente=[(6,6),(6,7),(6,8)]
    manzana=(10,2)
    serpiente_pantalla(serpiente)
    manzana_pantalla(manzana)

def serpiente_pantalla(serpiente):
    for segmento in serpiente:
        pygame.draw.rect(ventana, verde,
                         (segmento[0] * tamanio_celda, segmento[1] * tamanio_celda, tamanio_celda, tamanio_celda))
def manzana_pantalla(manzana):
    pygame.draw.rect(ventana,rojo,
                     (manzana[0] * tamanio_celda, manzana[1] * tamanio_celda, tamanio_celda, tamanio_celda))
def ventana_principal():
    pass





def terminar_juego():
    pass
    #si alguna de las coordenadas

def moverse(direccion):
    pass
    #print(direccion)
    #Definir una variable que sea coordenada sigueinte
    #si tiene 14, terminar juego
    #si la coordenada ya existe, terminar juego
    #si cumple, añadir a la serpiente
    #Si la coordenada a la que se mueve es igual a la corrdenada de manzana, llamar manzana
def manzana_nueva(serpiente):
    # Crear una lista de todas las coordenadas posibles en el tablero
    todas_coordenadas = [(x, y) for x in range(13) for y in range(13)]

    # Filtrar las coordenadas para eliminar las que están ocupadas por la serpiente
    coordenadas_disponibles = [coord for coord in todas_coordenadas if coord not in serpiente]

    # Verificar si hay coordenadas disponibles
    if coordenadas_disponibles:
        # Elegir dos coordenadas aleatorias de las disponibles
        manzana = random.choice(coordenadas_disponibles)
        return manzana
    else:
        # No hay coordenadas disponibles, el juego está lleno
        return None


    #que aparezca aleatoriamente pero que no este dentro
    #dentro de las coordenadas de la serpiente
# Estado del juego
jugando = True
perdio = False
direccion=""
serpiente=[(6,6),(6,7),(6,8)]
manzana=(10,2)
# Bucle principal del juego
while jugando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        # Control de la dirección de la serpiente (puedes modificar esto)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            direccion = "izquierda"
            moverse(direccion)
            manzana=manzana_nueva(serpiente)

        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            direccion = "derecha"
            moverse(direccion)
        elif pygame.key.get_pressed()[pygame.K_UP]:
            direccion = "arriba"
            moverse(direccion)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            direccion = "abajo"
            moverse(direccion)

    # Dibujar el tablero
    ventana.fill(negro)
    for fila in range(ancho_tablero):
        for columna in range(alto_tablero):
            pygame.draw.rect(ventana, blanco, (columna * tamanio_celda, fila * tamanio_celda, tamanio_celda, tamanio_celda), 1)
    serpiente_pantalla(serpiente)
    manzana_pantalla(manzana)


    pygame.display.update()

pygame.quit()
