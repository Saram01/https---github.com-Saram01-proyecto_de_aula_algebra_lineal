import pygame
from vector import Vector2D
from transformaciones import rotar_vector

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
reloj = pygame.time.Clock()

# Posición inicial del objeto
posicion = Vector2D(300, 200)
direccion = Vector2D(1, 0)  # hacia la derecha
angulo = 0  # grados

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Rotar dirección
    angulo += 1
    direccion_rotada = rotar_vector(direccion, angulo)

    # Mover objeto
    posicion += direccion_rotada * 2

    pantalla.fill((30, 30, 30))
    pygame.draw.circle(pantalla, (255, 0, 0), (int(posicion.x), int(posicion.y)), 10)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
