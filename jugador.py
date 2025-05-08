import pygame
import random
from vector import Vector2D

class Jugador:
    def __init__(self, pos):
        self.pos = pos
        self.velocidad = Vector2D(0, 0)
        self.radio = 20
        self.color = (0, 255, 0)
        self.vidas = 3
        self.inmune = False
        self.tiempo_inmunidad = 0

    def mover(self, dx, dy):
        """Mueve al jugador en las direcciones indicadas"""
        self.pos.x += dx
        self.pos.y += dy

    def rebote(self, ancho, alto):
        """Detecta la colisión con las paredes y aplica el rebote"""
        if self.pos.x - self.radio <= 0 or self.pos.x + self.radio >= ancho:
            self.velocidad.x = -self.velocidad.x
            return True
        if self.pos.y - self.radio <= 0 or self.pos.y + self.radio >= alto:
            self.velocidad.y = -self.velocidad.y
            return True
        return False

    def actualizar(self):
        """Actualiza la posición del jugador y la velocidad"""
        self.pos += self.velocidad

    def activar_inmunidad(self, duracion):
        """Activa la inmunidad por un tiempo determinado"""
        self.inmune = True
        self.tiempo_inmunidad = pygame.time.get_ticks() + duracion

    def actualizar_inmunidad(self):
        """Desactiva la inmunidad después del tiempo indicado"""
        if self.inmune and pygame.time.get_ticks() >= self.tiempo_inmunidad:
            self.inmune = False

    def perder_vida(self):
        """Reduce las vidas si el jugador no está inmune"""
        if not self.inmune:
            self.vidas -= 1

    def animacion_rebote(self, screen):
        """Animación de rebote cuando el jugador toca la pared"""
        for i in range(6):
            color = (255, 100, 100) if i % 2 == 0 else (255, 200, 200)
            pygame.draw.circle(screen, color, self.pos.como_tupla(), self.radio + i*2)
            pygame.display.flip()
            pygame.time.delay(40)


