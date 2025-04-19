from node import Node

def resolver_dfs(grid, start, goal):

    movement_value = grid[start[0]][start[1]]
    print(grid)
    print(start)
    
    root = Node(movement_value, start[0], start[1], [])
    stack = [root]
    visited = set()
    path = []

    while stack:
        current_node = stack.pop()
        visited.add((current_node.x, current_node.y))

        if (current_node.x, current_node.y) == end:
            path.append(current_node)
            break
        
        down_movement = current_node.x + movement_value
        up_movement = current_node.x - movement_value
        right_movement = current_node.y + movement_value
        left_movement = current_node.y - movement_value

        if (grid[down_movement, current_node.y] != None):
            current_node.neighbors.append(Node(grid[down_movement][current_node.y], down_movement, current_node.y, []))

        if (grid[current_node.x, right_movement] != None):
            current_node.neighbors.append(Node(grid[current_node.x][right_movement], current_node.x, right_movement, []))

        if (grid[current_node.x, left_movement] != None):
            current_node.neighbors.append(Node(grid[current_node.x][left_movement], current_node.x, left_movement, []))

        if (grid[up_movement, current_node.y] != None):
            current_node.neighbors.append(Node(grid[up_movement][current_node.y], up_movement, current_node.y, []))

        for neighbor in current_node.neighbors:
            if neighbor not in visited:
                neighbor_node = Node(grid[neighbor[0]][neighbor[1]], neighbor[0], neighbor[1], [])
                stack.append(neighbor_node)
                visited.add(neighbor)
    return path