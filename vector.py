import math

class Vector2D:
    def __init__(self, x=0, y=0):
        """Inicializa el vector con las coordenadas x e y."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Permite sumar dos vectores."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """Permite restar dos vectores."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __repr__(self):
        """Devuelve una representación en cadena del vector."""
        return f"Vector2D({self.x}, {self.y})"

    def distancia(self, otro):
        """Devuelve la distancia entre dos vectores."""
        return math.sqrt((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2)

    def como_tupla(self):
        """Convierte el vector en una tupla (x, y)."""
        return (self.x, self.y)

    def rotar(self, theta):
        """Rota el vector en el plano 2D por un ángulo 'theta' dado en radianes."""
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        
        # Aplicación de la fórmula de rotación
        x_nueva = self.x * cos_theta - self.y * sin_theta
        y_nueva = self.x * sin_theta + self.y * cos_theta
        
        return Vector2D(x_nueva, y_nueva)

    def __str__(self):
        """Representación del vector en forma de cadena."""
        return f"({self.x}, {self.y})"

