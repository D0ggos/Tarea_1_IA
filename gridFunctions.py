import pygame


WIDTH, HEIGHT = 1200, 600
CELL_SIZE = 40
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 24)

def draw_grid(maze, rows, columns, start, end, solution_path, actual_maze, results, destacar=None):
    screen.fill(WHITE)

    if not maze:
        mensaje = font.render("No hay laberinto cargado. Presiona 'Cargar laberinto'.", True, BLACK)
        screen.blit(mensaje, (WIDTH // 2 - 200, HEIGHT // 2))
        return
    
    titulo = font.render(f"Laberinto {actual_maze + 1} de {len(results)}", True, BLACK)
    titulo_rect = titulo.get_rect(center=(WIDTH // 2, 100))
    screen.blit(titulo, titulo_rect)
    
    if results[actual_maze]:
        estado = font.render(f"Resultado: {results[actual_maze]}", True, BLACK)
        estado_rect = estado.get_rect(center=(WIDTH // 2, 480))
        screen.blit(estado, estado_rect)
    
    maze_width = columns * CELL_SIZE
    maze_height = rows * CELL_SIZE
    
    grid_offset_x = (WIDTH - maze_width) // 2
    grid_offset_y = (HEIGHT - maze_height) // 2 - 20 
    
    for i in range(rows):
        for j in range(columns):
            x = grid_offset_x + j * CELL_SIZE
            y = grid_offset_y + i * CELL_SIZE
            
            color = GRAY
            if (i, j) == start:
                color = GREEN
            elif (i, j) == end:
                color = RED
            elif (i, j) == destacar:
                color = YELLOW
            elif solution_path and (i, j) in solution_path:
                color = ORANGE
                
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)
            valor = font.render(str(maze[i][j]), True, BLACK)
            valor_rect = valor.get_rect(center=(x + CELL_SIZE//2, y + CELL_SIZE//2))
            screen.blit(valor, valor_rect)

def draw_button(x, y, texto, activo=False, ancho=BUTTON_WIDTH):
    color = BLUE if not activo else RED
    pygame.draw.rect(screen, color, (x, y, ancho, BUTTON_HEIGHT))
    pygame.draw.rect(screen, BLACK, (x, y, ancho, BUTTON_HEIGHT), 2)
    label = font.render(texto, True, WHITE)
    label_rect = label.get_rect(center=(x + ancho//2, y + BUTTON_HEIGHT//2))
    screen.blit(label, label_rect)

def animar_solucion(path, maze, rows, columns, start, end, actual_maze, results):
    if not path:
        return
    
    for (i, j) in path:
        draw_grid(maze, rows, columns, start, end, path, actual_maze, results, destacar=(i, j))
        pygame.display.flip()
        pygame.time.wait(700)