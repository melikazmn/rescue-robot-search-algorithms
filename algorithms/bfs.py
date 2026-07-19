from collections import deque
from utils import reconstruct_path
import time


def bfs(grid):
    start_time = time.perf_counter()

    queue = deque()
    queue.append(grid.start)

    visited = set()
    visited.add(grid.start)
    visited_nodes = 0

    parent = {}

    while queue:

        current = queue.popleft()
        visited_nodes += 1

        if current == grid.goal:
            path = reconstruct_path(parent, grid.start, grid.goal)

            execution_time = time.perf_counter() - start_time

            return {
                "algorithm": "BFS",
                "path_found": True,
                "path": path,
                "path_length": len(path) - 1,
                "visited_nodes": visited_nodes,
                "execution_time": execution_time,
            }


        for neighbor in grid.get_neighbors(current):

            if neighbor not in visited:
                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

        # No path found
    execution_time = time.perf_counter() - start_time

    return {
        "algorithm": "BFS",
        "path_found": False,
        "path": [],
        "path_length": 0,
        "visited_nodes": visited_nodes,
        "execution_time": execution_time,
    }
