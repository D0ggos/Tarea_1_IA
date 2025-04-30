import pygame
import sys
import os
from solve_dfs import solve_dfs
from solve_ucs import solve_ucs_cell_value, solve_ucs_step_value
from gridFunctions import draw_grid, draw_button, animar_solucion


mazes = []
actual_maze = 0
maze = []
start = end = None
rows = columns = 0
solution_path = []
selected_algorithm = "DFS"
results = []

def load_maze():
    global maze, start, end, rows, columns, solution_path
    
    if not mazes or actual_maze >= len(mazes):
        return
    
    lab = mazes[actual_maze]
    maze = lab["grid"]
    start = lab["start"]
    end = lab["end"]
    rows = lab["rows"]
    columns = lab["columns"]
    solution_path = lab["solution"]
    print("ola")

def load_file():
    global mazes, maze, start, end, rows, columns, solution_path, results, actual_maze
    
    ruta = "./example.txt"
    if not os.path.isfile(ruta):
        print("Archivo no encontrado.")
        return
    
    mazes = []
    results = []
    
    with open(ruta) as f:
        lineas = f.readlines()
    
    i = 0
    while i < len(lineas):
        line = lineas[i].strip()
        if line == "0":
            break
        try:
            header = list(map(int, line.split()))
            if len(header) != 6:
                i += 1
                continue
            rows, columns, si, sj, gi, gj = header
            lab_actual = []
            
            for j in range(1, rows + 1):
                if i + j >= len(lineas):
                    break
                fila = list(map(int, lineas[i + j].strip().split()))
                if len(fila) != columns:
                    break
                lab_actual.append(fila)
            
            if len(lab_actual) == rows:
                mazes.append({
                    "grid": lab_actual,
                    "start": (si, sj),
                    "end": (gi, gj),
                    "rows": rows,
                    "columns": columns,
                    "solution": None
                })
                results.append(None)
            i += rows + 1
        except ValueError:
            i += 1

    if mazes:
        actual_maze = 0
        load_maze()
        
        print(f"Se cargaron {len(mazes)} laberintos.")
    else:
        print("No se encontraron laberintos válidos en el archivo.")

def change_maze(direccion):
    global actual_maze
    
    if not mazes:
        return
    
    if direccion == "siguiente":
        actual_maze = (actual_maze + 1) % len(mazes)
    else:
        actual_maze = (actual_maze - 1) % len(mazes)
    
    load_maze()

def solve():
    global solution_path, results

    if not maze:
        print("No hay laberinto cargado.")
        return

    if selected_algorithm == "DFS":
        solution = solve_dfs(maze, start, end)
    elif selected_algorithm == "Costo uniforme (celda)":
        solution = solve_ucs_cell_value(maze, start, end)
    elif selected_algorithm == "Costo uniforme (salto)":
        solution = solve_ucs_step_value(maze, start, end)
    else:
        solution = None

    print(solution)
    mazes[actual_maze]["solution"] = solution
    solution_path = solution

    if solution is None:
        results[actual_maze] = "No hay solución"
        print("Resultado: No hay solución.")
    else:
        results[actual_maze] = str(len(solution) - 1)
        print(f"Resultado: Solución encontrada en {len(solution) - 1} movimientos.")
        animar_solucion(solution, maze, rows, columns, start, end, actual_maze, results)

def main():
    global selected_algorithm
    
    running = True
    while running:
        draw_grid(maze, rows, columns, start, end, solution_path, actual_maze, results)
        
        btn_width = 200
        total_width = 3 * btn_width + 20
        start_x = (1200 - total_width) // 2
        
        draw_button(start_x, 20, "Cargar laberinto")
        draw_button(start_x + btn_width + 10, 20, "Resolver laberinto")
        draw_button(start_x + 2 * (btn_width + 10), 20, selected_algorithm, activo=True)
        
        nav_btn_width = 200
        draw_button(50, 520, "< Anterior")
        draw_button(1200 - 50 - nav_btn_width, 520, "Siguiente >")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if start_x <= x <= start_x + btn_width and 20 <= y <= 20 + 40:
                    load_file()
                elif start_x + btn_width + 10 <= x <= start_x + 2 * btn_width + 10 and 20 <= y <= 20 + 40:
                    solve()
                elif start_x + 2 * (btn_width + 10) <= x <= start_x + 3 * btn_width + 20 and 20 <= y <= 20 + 40:
                    if selected_algorithm == "DFS":
                        selected_algorithm = "Costo uniforme (celda)"
                    elif selected_algorithm == "Costo uniforme (celda)":
                        selected_algorithm = "Costo uniforme (salto)"
                    else:
                        selected_algorithm = "DFS"
                
                
                if 50 <= x <= 50 + nav_btn_width and 520 <= y <= 520 + 40:
                    change_maze("anterior")
                elif 1200 - 50 - nav_btn_width <= x <= 1200 - 50 and 520 <= y <= 520 + 40:
                    change_maze("siguiente")
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()