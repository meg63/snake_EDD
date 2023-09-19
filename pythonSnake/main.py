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

# Fuente para el mensaje de juego perdido
fuente = pygame.font.Font(None, 36)

# Función para dibujar la serpiente en la pantalla
def dibujar_serpiente(serpiente):
    for segmento in serpiente:
        pygame.draw.rect(ventana, verde, (segmento[0] * tamanio_celda, segmento[1] * tamanio_celda, tamanio_celda, tamanio_celda))

# Función para mover la serpiente y manejar el crecimiento
def mover_serpiente(serpiente, direccion, comida):
    cabeza = list(serpiente[0])

    if direccion == "izquierda":
        cabeza[0] -= 1
    elif direccion == "derecha":
        cabeza[0] += 1
    elif direccion == "arriba":
        cabeza[1] -= 1
    elif direccion == "abajo":
        cabeza[1] += 1

    serpiente.insert(0, cabeza)

    if cabeza == comida:
        return True  # La serpiente comió comida (crecimiento)
    else:
        serpiente.pop()
        return False

# Función para verificar si la serpiente ha chocado contra una pared
def verificar_colision_pared(serpiente):
    cabeza = serpiente[0]
    return cabeza[0] < 0 or cabeza[0] > ancho_tablero or cabeza[1] < 0 or cabeza[1] > alto_tablero

# Lista de coordenadas que representa la serpiente (inicial)
serpiente = [(6, 6), (5, 6)]

# Posición inicial de la comida (ejemplo)
comida = (9, 9)

# Dirección inicial de la serpiente
direccion = "derecha"

# Estado del juego
jugando = True
perdio = False

# Bucle principal del juego
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    if not perdio:
        # Control de la dirección de la serpiente (puedes modificar esto)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            direccion = "izquierda"
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            direccion = "derecha"
        elif pygame.key.get_pressed()[pygame.K_UP]:
            direccion = "arriba"
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            direccion = "abajo"

        # Mover la serpiente y verificar si comió comida
        if mover_serpiente(serpiente, direccion, comida):
            # Generar nueva posición de comida
            comida = (random.randint(0, ancho_tablero - 1), random.randint(0, alto_tablero - 1))

        # Verificar colisión con la pared
        if verificar_colision_pared(serpiente):
            perdio = True

    # Dibujar el tablero
    ventana.fill(negro)
    for fila in range(ancho_tablero):
        for columna in range(alto_tablero):
            pygame.draw.rect(ventana, blanco, (columna * tamanio_celda, fila * tamanio_celda, tamanio_celda, tamanio_celda), 1)

    if perdio:
        # Mostrar mensaje de juego perdido
        mensaje = fuente.render("¡Has perdido!", True, blanco)
        ventana.blit(mensaje, (ancho // 2 - 100, alto // 2 - 18))
    else:
        # Dibujar la serpiente en pantalla
        dibujar_serpiente(serpiente)
        # Dibujar la comida en pantalla
        pygame.draw.rect(ventana, blanco, (comida[0] * tamanio_celda, comida[1] * tamanio_celda, tamanio_celda, tamanio_celda))

    pygame.display.update()

# Finalizar pygame
pygame.quit()





