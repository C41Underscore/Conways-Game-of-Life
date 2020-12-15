import pygame as pg
import time
import random

from cell import Cell

# TODO: GET USER INPUT WORKING TO FOR USER INITIALISATION

SIZE_OF_CELL = 20
SIZE_OF_WINDOW = 1000
NUMBER_OF_CELLS_PER_ROW = int(SIZE_OF_WINDOW/SIZE_OF_CELL)
NUMBER_OF_ITERATIONS = 300
K = 3


def run_game(cells):
    for _ in range(0, NUMBER_OF_ITERATIONS):
        time.sleep(0.0001)
        for i in range(0, NUMBER_OF_CELLS_PER_ROW):
            for j in range(0, NUMBER_OF_CELLS_PER_ROW):
                cells[i][j].calculate_next_state()
        for i in range(0, NUMBER_OF_CELLS_PER_ROW):
            for j in range(0, NUMBER_OF_CELLS_PER_ROW):
                cells[i][j].advance()
    time.sleep(5)


def associate_neighbours(cells):
    for i in range(0, NUMBER_OF_CELLS_PER_ROW):
        for j in range(0, NUMBER_OF_CELLS_PER_ROW):
            next_neighbours = list()
            # left
            next_neighbours.append(cells[i][j-1 if j > 0 else NUMBER_OF_CELLS_PER_ROW-1])
            # right
            next_neighbours.append(cells[i][j+1 if j < NUMBER_OF_CELLS_PER_ROW-1 else 0])
            # above
            next_neighbours.append(cells[i-1 if i > 0 else NUMBER_OF_CELLS_PER_ROW-1][j])
            # below
            next_neighbours.append(cells[i+1 if i < NUMBER_OF_CELLS_PER_ROW-1 else 0][j])
            # left-top
            next_neighbours.append(
                cells[i-1 if i > 0 else NUMBER_OF_CELLS_PER_ROW-1][j-1 if j > 0 else NUMBER_OF_CELLS_PER_ROW-1]
            )
            # right-top
            next_neighbours.append(
                cells[i-1 if i > 0 else NUMBER_OF_CELLS_PER_ROW-1][j+1 if j < NUMBER_OF_CELLS_PER_ROW-1 else 0]
            )
            # left-bottom
            next_neighbours.append(
                cells[i+1 if i < NUMBER_OF_CELLS_PER_ROW-1 else 0][j-1 if j > 0 else NUMBER_OF_CELLS_PER_ROW-1]
            )
            # right-bottom
            next_neighbours.append(
                cells[i+1 if i < NUMBER_OF_CELLS_PER_ROW-1 else 0][j+1 if j < NUMBER_OF_CELLS_PER_ROW-1 else 0]
            )
            cells[i][j].set_neighbours(next_neighbours)


def generate_cell_array(game_surface):
    cells = [[[] for x in range(0, NUMBER_OF_CELLS_PER_ROW)] for i in range(0, NUMBER_OF_CELLS_PER_ROW)]
    for i in range(0, NUMBER_OF_CELLS_PER_ROW):
        for j in range(0, NUMBER_OF_CELLS_PER_ROW):
            cells[i][j] = Cell(
                bool(random.getrandbits(1)),
                pg.__rect_constructor(
                    i*SIZE_OF_CELL,
                    j*SIZE_OF_CELL,
                    SIZE_OF_CELL,
                    SIZE_OF_CELL
                ),
                game_surface,
                K
            )
    return cells


def main():
    pg.display.init()
    display_window = pg.display.set_mode(
        size=(SIZE_OF_WINDOW, SIZE_OF_WINDOW),
        display=pg.NOFRAME
    )
    game_surface = pg.display.get_surface()
    cells = generate_cell_array(game_surface)
    associate_neighbours(cells)
    run_game(cells)


if __name__ == "__main__":
    main()
