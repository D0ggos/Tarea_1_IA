import pygame
import sys
import time
import os
from resolver_dfs import resolver_dfs
from resolver_costo_uniforme import resolver_costo_uniforme

# --- Constantes ---
WIDTH, HEIGHT = 800, 600
GRID_OFFSET = 100
CELL_SIZE = 50
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinto Saltarín")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

# --- Variables globales ---
laberinto = []
start = end = None
filas = columnas = 0
camino_solucion = []
algoritmo_usado = "DFS"  # o "Costo uniforme"

# --- Funciones de lógica ---
def cargar_laberinto_desde_archivo():
    global laberinto, start, end, filas, columnas, camino_solucion

    ruta = input("Ingresa la ruta del archivo de laberinto (ej: laberinto.txt): ").strip()
    if not os.path.isfile(ruta):
        print("Archivo no encontrado.")
        return

    with open(ruta) as f:
        lineas = f.read().strip().split("\n")
    if not lineas:
        return
    header = list(map(int, lineas[0].split()))
    filas, columnas, si, sj, gi, gj = header
    start, end = (si, sj), (gi, gj)
    laberinto = [list(map(int, lineas[i + 1].split())) for i in range(filas)]
    camino_solucion = []

def resolver_laberinto():
    global camino_solucion
    if not laberinto:
        print("No hay laberinto cargado.")
        return

    if algoritmo_usado == "DFS":
        camino_solucion = resolver_dfs(laberinto, start, end)
    elif algoritmo_usado == "Costo uniforme":
        camino_solucion = resolver_costo_uniforme(laberinto, start, end)

    if camino_solucion is None:
        print("Resultado: No hay solución.")
    else:
        print(f"Resultado: Solución encontrada en {len(camino_solucion) - 1} movimientos.")
        animar_solucion(camino_solucion)

# --- Visualización animada ---
def animar_solucion(camino):
    for (i, j) in camino:
        dibujar_grilla(destacar=(i, j))
        pygame.display.flip()
        pygame.time.wait(1000)

# --- Dibujar UI ---
def dibujar_grilla(destacar=None):
    screen.fill(WHITE)
    for i in range(filas):
        for j in range(columnas):
            x = GRID_OFFSET + j * CELL_SIZE
            y = GRID_OFFSET + i * CELL_SIZE
            color = GRAY
            if (i, j) == start:
                color = GREEN
            elif (i, j) == end:
                color = RED
            elif (i, j) == destacar:
                color = YELLOW
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)
            valor = font.render(str(laberinto[i][j]), True, BLACK)
            screen.blit(valor, (x + 15, y + 15))

def dibujar_boton(x, y, texto, activo=False):
    color = BLUE if not activo else RED
    pygame.draw.rect(screen, color, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.draw.rect(screen, BLACK, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    label = font.render(texto, True, WHITE)
    screen.blit(label, (x + 10, y + 10))

# --- Loop principal ---
def main():
    global algoritmo_usado
    running = True
    while running:
        screen.fill(WHITE)
        dibujar_grilla()
        dibujar_boton(50, 20, "Cargar laberinto")
        dibujar_boton(280, 20, "Resolver laberinto")
        dibujar_boton(550, 20, "Algoritmo: " + algoritmo_usado, activo=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 50 + BUTTON_WIDTH and 20 <= y <= 20 + BUTTON_HEIGHT:
                    cargar_laberinto_desde_archivo()
                elif 280 <= x <= 280 + BUTTON_WIDTH and 20 <= y <= 20 + BUTTON_HEIGHT:
                    resolver_laberinto()
                elif 550 <= x <= 550 + BUTTON_WIDTH and 20 <= y <= 20 + BUTTON_HEIGHT:
                    algoritmo_usado = "Costo uniforme" if algoritmo_usado == "DFS" else "DFS"

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
