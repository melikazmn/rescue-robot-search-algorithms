from grid import Grid
from algorithms.bfs import bfs


def main():
    grid = Grid("map.txt")

    result = bfs(grid)

    print(f"Algorithm      : {result['algorithm']}")
    print(f"Path Found     : {result['path_found']}")
    print(f"Path Length    : {result['path_length']}")
    print(f"Visited Nodes  : {result['visited_nodes']}")
    print(f"Execution Time : {result['execution_time']:.6f} seconds")
    print("Path:", result["path"])

if __name__ == "__main__":
    main()