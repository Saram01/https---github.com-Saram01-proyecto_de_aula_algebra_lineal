import pygame
import random
from vector import Vector2D
from transformaciones import rotar_vector
from jugador import Jugador
from orbe import Orbe

# Inicialización
game_config = {
    "ANCHO": 800,
    "ALTO": 600,
    "niveles": [
        {"nivel": 1, "puntos_meta": 15, "vidas": None, "pared_dania": False, "inmunidad": False, "trampa": False},
        {"nivel": 2, "puntos_meta": 20, "vidas": 3, "pared_dania": True, "inmunidad": False, "trampa": False},
        {"nivel": 3, "puntos_meta": 25, "vidas": 3, "pared_dania": True, "inmunidad": True, "trampa": False},
        {"nivel": 4, "puntos_meta": 30, "vidas": 3, "pared_dania": True, "inmunidad": True, "trampa": True},
        {"nivel": 5, "puntos_meta": 35, "vidas": 3, "pared_dania": True, "inmunidad": True, "trampa": True}
    ]
}

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((game_config["ANCHO"], game_config["ALTO"]))
pygame.display.set_caption("Juego Vectorial")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 30)

nivel_actual = 0
puntos = 0
jugador = Jugador(Vector2D(400, 300))
orbes = [Orbe("normal", game_config["ANCHO"], game_config["ALTO"])]

# Configurar nivel
def configurar_nivel(nivel_info):
    global jugador, orbes, puntos
    puntos = 0
    jugador = Jugador(Vector2D(400, 300))
    if nivel_info["vidas"]:
        jugador.vidas = nivel_info["vidas"]
    orbes = [Orbe("normal", game_config["ANCHO"], game_config["ALTO"])]
    if nivel_info["inmunidad"]:
        orbes.append(Orbe("inmunidad", game_config["ANCHO"], game_config["ALTO"]))
    if nivel_info["trampa"]:
        orbes.append(Orbe("trampa", game_config["ANCHO"], game_config["ALTO"]))

# Animación de choque
def animacion_choque(screen, jugador):
    for i in range(6):
        color = (255, 50, 50) if i % 2 == 0 else (255, 200, 200)
        pygame.draw.circle(screen, color, jugador.pos.como_tupla(), jugador.radio + i)
        pygame.display.flip()
        pygame.time.delay(50)

# Bucle de niveles
while nivel_actual < len(game_config["niveles"]):
    nivel_info = game_config["niveles"][nivel_actual]
    configurar_nivel(nivel_info)
    running = True

    while running:
        screen.fill((25, 25, 35))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                nivel_actual = len(game_config["niveles"])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: jugador.mover(-5, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: jugador.mover(5, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]: jugador.mover(0, -5)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: jugador.mover(0, 5)

        jugador.velocidad = rotar_vector(jugador.velocidad, 0.03)
        jugador.actualizar()

        choco = jugador.rebote(game_config["ANCHO"], game_config["ALTO"])
        if choco and nivel_info["pared_dania"] and not jugador.inmune:
            # Animación de choque
            jugador.perder_vida()
            if jugador.vidas > 0:
                animacion_choque(screen, jugador)
            else:
                # Si el jugador ha perdido todas las vidas, mostrar mensaje de derrota
                mensaje_derrota = font.render("¡Has perdido! Presiona R para reiniciar.", True, (255, 0, 0))
                screen.blit(mensaje_derrota, (game_config["ANCHO"] // 2 - 150, game_config["ALTO"] // 2))
                pygame.display.flip()
                esperando_reinicio = True
                while esperando_reinicio:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            esperando_reinicio = False
                            running = False
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                            # Reiniciar el nivel o el juego
                            jugador.vidas = nivel_info["vidas"] if nivel_info["vidas"] else 3  # Restablecer vidas
                            puntos = 0
                            nivel_actual = 0  # Reiniciar al primer nivel
                            esperando_reinicio = False
                            running = False
                            # El bucle reiniciará el nivel
                break  # Salir del bucle de niveles si se ha perdido

        if jugador.inmune:
            jugador.actualizar_inmunidad()

        # Verificar la colisión con orbes y generar nuevos orbes
        orbes_a_eliminar = []
        for orbe in orbes:
            if jugador.pos.distancia(orbe.pos) < jugador.radio + orbe.radio:
                if orbe.tipo == "normal":
                    puntos += 1
                    orbes_a_eliminar.append(orbe)
                    jugador.color = [random.randint(100, 255) for _ in range(3)]
                elif orbe.tipo == "inmunidad":
                    jugador.activar_inmunidad(600)  # 10 segundos
                    orbes_a_eliminar.append(orbe)
                elif orbe.tipo == "trampa":
                    jugador.vidas -= 1
                    orbes_a_eliminar.append(orbe)

        # Eliminar orbes que han sido recolectados y generar nuevos orbes
        for orbe in orbes_a_eliminar:
            orbes.remove(orbe)
            # Crear nuevo orbe aleatorio
            nuevo_orbe = Orbe("normal", game_config["ANCHO"], game_config["ALTO"])
            orbes.append(nuevo_orbe)

        # Dibujar paredes a partir del nivel 2
        if nivel_info["nivel"] >= 2:
            grosor_pared = 10 + nivel_info["nivel"]
            pygame.draw.rect(screen, (255, 0, 0), (0, 0, game_config["ANCHO"], grosor_pared))  # Superior
            pygame.draw.rect(screen, (255, 0, 0), (0, game_config["ALTO"] - grosor_pared, game_config["ANCHO"], grosor_pared))  # Inferior
            pygame.draw.rect(screen, (255, 0, 0), (0, 0, grosor_pared, game_config["ALTO"]))  # Izquierda
            pygame.draw.rect(screen, (255, 0, 0), (game_config["ANCHO"] - grosor_pared, 0, grosor_pared, game_config["ALTO"]))  # Derecha

        pygame.draw.circle(screen, jugador.color, jugador.pos.como_tupla(), jugador.radio)
        for orbe in orbes:
            color = (0, 180, 255) if orbe.tipo == "normal" else (255, 255, 0) if orbe.tipo == "inmunidad" else (255, 50, 50)
            pygame.draw.circle(screen, color, orbe.pos.como_tupla(), orbe.radio)

        # HUD
        vidas_txt = f"Vidas: {jugador.vidas}" if nivel_info["vidas"] else "Vidas: ∞"
        texto = font.render(f"Nivel: {nivel_info['nivel']}  Puntos: {puntos}  {vidas_txt}", True, (255, 255, 255))
        screen.blit(texto, (10, 10))

        if puntos >= nivel_info["puntos_meta"]:
            nivel_actual += 1
            running = False

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
print("Juego finalizado.")

