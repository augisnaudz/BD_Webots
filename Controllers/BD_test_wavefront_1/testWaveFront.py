def wavefront(maze, start, goal):
    queue = [goal]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    distances = [[-1 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    distances[goal[0]][goal[1]] = 0

    while queue:
        current_x, current_y = queue.pop(0)
        visited.add((current_x, current_y))

        for dx, dy in directions:
            next_x, next_y = current_x + dx, current_y + dy

            if not (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0])):
                continue

            if maze[next_x][next_y] == 1 or (next_x, next_y) in visited:
                continue

            distances[next_x][next_y] = distances[current_x][current_y] + 1
            queue.append((next_x, next_y))

        visited.add((current_x, current_y))

    # Build the path from the distances matrix
    path = [start]
    current_x, current_y = start
    while (current_x, current_y) != goal:
        min_distance = float('inf')
        min_x, min_y = current_x, current_y

        for dx, dy in directions:
            next_x, next_y = current_x + dx, current_y + dy

            if not (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0])):
                continue

            if maze[next_x][next_y] == 1:
                continue

            if distances[next_x][next_y] < min_distance:
                min_distance = distances[next_x][next_y]
                min_x, min_y = next_x, next_y

        path.append((min_x, min_y))
        current_x, current_y = min_x, min_y

    return path