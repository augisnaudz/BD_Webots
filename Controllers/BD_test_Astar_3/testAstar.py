import heapq

# A* algorithm
def astar(maze, start, end):
    # Define possible movements: up, down, left, right
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Define heuristic function (Manhattan distance)
    def heuristic(node):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])

    # Initialize data structures
    visited = set()
    queue = []
    heapq.heappush(queue, (0, start))
    cost_so_far = {}
    cost_so_far[start] = 0

    # A* algorithm implementation
    while queue:
        current = heapq.heappop(queue)[1]
        current = tuple(current)  # Convert to tuple

        if current == end:
            break

        for movement in movements:
            dx, dy = movement
            next_node = (current[0] + dx, current[1] + dy)

            if next_node[0] < 0 or next_node[0] >= len(maze) or next_node[1] < 0 or next_node[1] >= len(maze[0]):
                continue

            if maze[next_node[0]][next_node[1]] == 1:
                continue

            new_cost = cost_so_far[current] + 1

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node)
                heapq.heappush(queue, (priority, next_node))

    # Reconstruct the path
    path = []
    current = end
    while current != start:
        path.append(current)
        next_cost = cost_so_far[current] - 1
        for movement in movements:
            dx, dy = movement
            next_node = (current[0] + dx, current[1] + dy)
            if next_node in cost_so_far and cost_so_far[next_node] == next_cost:
                current = next_node
                break
    path.append(start)
    path.reverse()

    return path



# Example usage
maze = [[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0], 
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (0, 0)
end = (19, 19)

path = astar(maze, start, end)
print(path)
print(len(path))