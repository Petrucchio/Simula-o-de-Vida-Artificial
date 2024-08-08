import random

def initialize_random_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = [random.choice([0, 1]) for _ in range(cols)]
        grid.append(row)
    return grid

def count_live_neighbors(grid, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    live_neighbors = 0
    for dr, dc in directions:
        neighbor_row, neighbor_col = row + dr, col + dc
        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
            live_neighbors += grid[neighbor_row][neighbor_col]
    return live_neighbors

def get_next_generation(grid):
    next_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            live_neighbors = count_live_neighbors(grid, row, col)
            if grid[row][col] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    next_grid[row][col] = 0
                else:
                    next_grid[row][col] = 1
            else:
                if live_neighbors == 3:
                    next_grid[row][col] = 1
    return next_grid

def display_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print()

def main():
    rows, cols = 10, 10  # Defina o tamanho desejado da grade
    grid = initialize_random_grid(rows, cols)
    number_of_iterations = 10  # Defina o número desejado de iterações

    for _ in range(number_of_iterations):
        display_grid(grid)
        grid = get_next_generation(grid)

if __name__ == "__main__":
    main()
