"""Simulation of Conway's Game of Life."""

import os
import time
import numpy


def make_grid(rows, cols, live_cells):
    """Construct a rows x cols grid with the given live cells.

    The grid is represented as a (rows+2) x (cols+2) numpy array of
    8-bit integers, representing cell locations from (-1, -1) to
    (row+1, col+1). Live cells contain a 1, while dead cells contain a
    0.

    >>> make_grid(3, 4, [])
    array([[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]], dtype=int8)
    >>> make_grid(3, 4, [(0, 1), (1, 2), (2, 2), (2, 3)])
    array([[0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0, 0]], dtype=int8)
    """
    grid = numpy.zeros(shape=(rows + 2, cols + 2), dtype=numpy.int8)
    for row, col in live_cells:
        grid[row + 1, col + 1] = 1
    return grid


def print_grid(grid, interactive=False):
    """Print a grid.

    If interactive is true, then inserts a slight delay between
    printing each timestep.
    """
    if interactive:
        time.sleep(0.05)
        os.system("clear")
    rows, cols = grid.shape
    print("-" * cols)
    for i in range(1, rows - 1):
        print("|", end="")
        for j in range(1, cols - 1):
            print("*" if grid[i, j] else " ", end="")
        print("|")
    print("-" * cols)
    print()


def timestep(current_grid, next_grid):
    """Simulate a single timestep of the Game of Life.

    current_grid is the input grid, next_grid is the output.

    >>> grid1 = make_grid(3, 4, [(0, 1), (1, 2), (2, 2), (2, 3)])
    >>> grid2 = make_grid(3, 4, [])
    >>> timestep(grid1, grid2)
    >>> grid1
    array([[0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0, 0]], dtype=int8)
    >>> grid2
    array([[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0, 0]], dtype=int8)
    """
    interior_rows = range(1, current_grid.shape[0] - 1)
    interior_cols = range(1, current_grid.shape[1] - 1)

    #              N       E       S       W       NE       SE      SW       NW
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    lives = {}
    for row in interior_rows:
        for col in interior_cols:
            lives[(row, col)] = 0
            for neighbor in neighbors:
                lives[(row, col)] += current_grid[row + neighbor[0], col + neighbor[1]]

    alive = (0, 0, 1, 1, 0, 0, 0, 0, 0)
    dead = (0, 0, 0, 1, 0, 0, 0, 0, 0)
    for row in interior_rows:
        for col in interior_cols:
            if current_grid[row, col] == 1:
                next_grid[row, col] = alive[lives[(row, col)]]
            else:
                next_grid[row, col] = dead[lives[(row, col)]]


def simulate(rows, cols, steps, live_cells, interactive=False):
    """Simulate full Game of Life.

    Simulates on a rows x cols grid for the given number of steps, with
    the given sequence of initial live cells.
    """
    start = make_grid(rows, cols, live_cells)
    end = make_grid(rows, cols, [])
    for _ in range(steps):
        timestep(start, end)
        start, end = end, start
        print_grid(start, interactive)
