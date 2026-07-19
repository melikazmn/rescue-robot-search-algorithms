def reconstruct_path(parent, start, goal):

    path = []

    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)

    path.reverse()

    return path