def solve_dfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    # Usamos tuplas para representar posiciones (row, col)
    stack = [(start, [start])]  # (posición actual, camino hasta ahora)
    visited = set([start])
    
    while stack:
        (row, col), path = stack.pop()
        
        if (row, col) == goal:
            return path
        
        # Valor de movimiento en la celda actual
        move_val = grid[row][col]
        
        # Posibles movimientos: abajo, arriba, derecha, izquierda
        directions = [
            (row + move_val, col),  # Abajo
            (row - move_val, col),  # Arriba
            (row, col + move_val),  # Derecha
            (row, col - move_val)   # Izquierda
        ]
        
       
        for new_pos in directions:
            if is_valid(new_pos[0], new_pos[1]) and new_pos not in visited:
                visited.add(new_pos)
                new_path = path + [new_pos]
                stack.append((new_pos, new_path))
    
    return None