import random
from vector import Vector2D

class Orbe:
    def __init__(self, tipo, ancho, alto):
        self.tipo = tipo  # "normal", "inmortalidad", "trampa"
        self.radio = 10
        self.pos = Vector2D(random.randint(50, ancho - 50), random.randint(50, alto - 50))
        self.tiempo = 0  # solo usado para trampa o inmunidad

    def nuevo(self, ancho, alto):
        # Asegurarse de que los orbes no estén dentro de las paredes
        margen = 20  # Ajuste según el grosor de las paredes
        self.pos = Vector2D(random.randint(margen, ancho - margen), random.randint(margen, alto - margen))

    def desaparecer(self):
        # La animación para desaparecer el orbe puede ser simplemente reiniciar su posición
        self.nuevo(self.pos.x, self.pos.y)

