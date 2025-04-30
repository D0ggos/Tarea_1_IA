import heapq


def solve_ucs_cell_value(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, (row, col), path = heapq.heappop(priority_queue)

        if (row, col) == end:
            return path

        if (row, col) in visited:
            continue
        visited.add((row, col))

        move_val = grid[row][col]
        directions = [
            (row + move_val, col),
            (row - move_val, col),
            (row, col + move_val),
            (row, col - move_val)
        ]

        for new_row, new_col in directions:
            if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                new_cost = cost + grid[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                heapq.heappush(priority_queue, (new_cost, (new_row, new_col), new_path))

    return None

def solve_ucs_step_value(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, (row, col), path = heapq.heappop(priority_queue)

        if (row, col) == end:
            return path

        if (row, col) in visited:
            continue
        visited.add((row, col))

        move_val = grid[row][col]
        directions = [
            (row + move_val, col),
            (row - move_val, col),
            (row, col + move_val),
            (row, col - move_val)
        ]

        for new_row, new_col in directions:
            if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                new_cost = cost + 1  # Costo unitario por salto
                new_path = path + [(new_row, new_col)]
                heapq.heappush(priority_queue, (new_cost, (new_row, new_col), new_path))

    return None