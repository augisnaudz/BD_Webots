import heapq

class Node:
    def __init__(self, x, y, cost, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def astar(start, goal, grid):
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, start)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.x == goal.x and current_node.y == goal.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        closed_set.add((current_node.x, current_node.y))

        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x = current_node.x + x
            next_y = current_node.y + y

            if not (0 <= next_x < len(grid) and 0 <= next_y < len(grid[0])):
                continue

            if grid[next_x][next_y] == 1:
                continue

            if (next_x, next_y) in closed_set:
                continue

            new_cost = current_node.cost + 1
            heuristic = abs(next_x - goal.x) + abs(next_y - goal.y)
            priority = new_cost + heuristic
            heapq.heappush(open_set, Node(next_x, next_y, priority, current_node))

    return None