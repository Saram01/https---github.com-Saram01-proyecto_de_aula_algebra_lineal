import math
from vector import Vector2D

def rotar_vector(vector, theta):
    """
    Rota un vector 2D por un ángulo dado en radianes.

    :param vector: Instancia del objeto Vector2D a rotar.
    :param theta: Ángulo en radianes por el cual rotar el vector.
    :return: Un nuevo vector rotado.
    """
    return vector.rotar(theta)

def escalar_vector(vector, kx, ky):
    """
    Escala un vector 2D por los factores kx y ky en las direcciones x y y.

    :param vector: Instancia del objeto Vector2D a escalar.
    :param kx: Factor de escala en la dirección x.
    :param ky: Factor de escala en la dirección y.
    :return: Un nuevo vector escalado.
    """
    return vector.escalar(kx, ky)

def trasladar_vector(vector, dx, dy):
    """
    Traslada un vector 2D por los desplazamientos dx y dy.

    :param vector: Instancia del objeto Vector2D a trasladar.
    :param dx: Desplazamiento en la dirección x.
    :param dy: Desplazamiento en la dirección y.
    :return: Un nuevo vector trasladado.
    """
    return vector + Vector2D(dx, dy)




