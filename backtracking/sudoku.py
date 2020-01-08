# pass by backtracking

# assigning initial values to the grid
initial_grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

# a grid with no solution
no_solution = [
    [5, 0, 6, 5, 0, 8, 4, 0, 3],
    [5, 2, 0, 0, 0, 0, 0, 0, 2],
    [1, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

def is_safe(grid, row, column, n):
    for i in range(9):
        if grid[row][i] == n or grid[i][column] == n:
            return False

    for i in range(3):
        for j in range(3):
            if grid[(row - row % 3) + i][(column - column % 3) + j] == n:
                return False
    return True

def is_completed(grid):
    return all(all(cell != 0 for cell in row) for row in grid)


def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j


def sudoku(grid):
    if is_completed(grid):
        return grid

    row, column = find_empty_location(grid)

    for digit in range(1, 10):
        if is_safe(grid, row, column, digit):
            grid[row][column] = digit

            if sudoku(grid):
                return grid

            grid[row][column] = 0

    return False


def print_solution(grid):
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


if __name__ == "__main__":
    # make a copy of grid so that you can compare with the unmodified grid
    for grid in (initial_grid, no_solution):
        grid = list(map(list, grid))
        solution = sudoku(grid)
        if solution:
            print("grid after solving:")
            print_solution(solution)
        else:
            print("Cannot find a solution.")
