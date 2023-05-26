import queue

def wavefront_algorithm(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    wavefront = [[-1] * cols for _ in range(rows)]
    wavefront[end[0]][end[1]] = 0
    q = queue.Queue()
    q.put(end)

    while not q.empty():
        current_x, current_y = q.get()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = current_x + dx, current_y + dy

            if 0 <= next_x < rows and 0 <= next_y < cols and not visited[next_x][next_y] and maze[next_x][next_y] == 0:
                visited[next_x][next_y] = True
                q.put((next_x, next_y))
                wavefront[next_x][next_y] = wavefront[current_x][current_y] + 1

                if (next_x, next_y) == start:
                    break

    path = [start]
    current_x, current_y = start

    while (current_x, current_y) != end:
        min_wavefront = float('inf')
        next_x, next_y = current_x, current_y

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < rows and 0 <= ny < cols and wavefront[nx][ny] != -1 and wavefront[nx][ny] < min_wavefront:
                min_wavefront = wavefront[nx][ny]
                next_x, next_y = nx, ny

        path.append((next_x, next_y))
        current_x, current_y = next_x, next_y

    return path