import math
from vector import Vector2D

def rotar_vector(v, angulo_grados):
    rad = math.radians(angulo_grados)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    x = v.x * cos_a - v.y * sin_a
    y = v.x * sin_a + v.y * cos_a
    return Vector2D(x, y)
