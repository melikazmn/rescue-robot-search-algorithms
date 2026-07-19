class Grid:
    def __init__(self, filename):
        self.cols = 0
        self.rows = 0
        self.grid = []
        self.start = None
        self.goal = None

        self.load_map(filename)

    def load_map(self, filename):
        with open(filename, "r") as file:
            for row_index, line in enumerate(file):

                row = list(line.strip())
                self.grid.append(row)

                for col_index, cell in enumerate(row):

                    if cell == "S":
                        self.start = (row_index, col_index)

                    elif cell == "G":
                        self.goal = (row_index, col_index)

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])


    def is_valid(self, row, col):
        if row < 0 or row >= self.rows:
            return False

        if col < 0 or col >= self.cols:
            return False

        if self.grid[row][col] == "X":
            return False

        return True

    def get_neighbors(self, position):
        row, col = position

        directions = [
            (-1, 0),  # Up
            (1, 0),  # Down
            (0, -1),  # Left
            (0, 1)  # Right
        ]

        neighbors = []

        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            if self.is_valid(new_row, new_col):
                neighbors.append((new_row, new_col))

        return neighbors


