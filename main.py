import pygame as pg
import time
import random
from sys import exit

from cell import Cell

# TODO: GET USER INPUT WORKING TO FOR USER INITIALISATION

SIZE_OF_CELL = 20
SIZE_OF_WINDOW = 1000
NUMBER_OF_CELLS_PER_ROW = int(SIZE_OF_WINDOW/SIZE_OF_CELL)
NUMBER_OF_ITERATIONS = 500


def run_game(cells):
    for i in range(0, NUMBER_OF_ITERATIONS):
        time.sleep(0.0001)
        for i in range(0, NUMBER_OF_CELLS_PER_ROW):
            for j in range(0, NUMBER_OF_CELLS_PER_ROW):
                cells[i][j].calculate_next_state()
        for i in range(0, NUMBER_OF_CELLS_PER_ROW):
            for j in range(0, NUMBER_OF_CELLS_PER_ROW):
                cells[i][j].advance()
    time.sleep(15)


def associate_neighbours(cells):
    for i in range(0, NUMBER_OF_CELLS_PER_ROW):
        for j in range(0, NUMBER_OF_CELLS_PER_ROW):
            next_neighbours = list()
            if i == 0 == j:
                next_neighbours.append(cells[i+1][j])
                next_neighbours.append(cells[i][j+1])
                next_neighbours.append(cells[i+1][i+1])
            elif i == 0 and j == NUMBER_OF_CELLS_PER_ROW-1:
                next_neighbours.append(cells[i][j-1])
                next_neighbours.append(cells[i+1][j-1])
                next_neighbours.append(cells[i+1][j])
            elif i == NUMBER_OF_CELLS_PER_ROW-1 and j == 0:
                next_neighbours.append(cells[i-1][j])
                next_neighbours.append(cells[i-1][j+1])
                next_neighbours.append(cells[i][j+1])
            elif i == NUMBER_OF_CELLS_PER_ROW-1 == j:
                next_neighbours.append(cells[i-1][j])
                next_neighbours.append(cells[j-1][j-1])
                next_neighbours.append(cells[i][j-1])
            else:
                if i == 0:
                    next_neighbours.append(cells[i][j-1])
                    next_neighbours.append(cells[i-1][j+1])
                    next_neighbours.append(cells[i+1][j])
                    next_neighbours.append(cells[i+1][j+1])
                    next_neighbours.append(cells[i][j+1])
                elif j == 0:
                    next_neighbours.append(cells[i-1][j])
                    next_neighbours.append(cells[i-1][j+1])
                    next_neighbours.append(cells[i][j+1])
                    next_neighbours.append(cells[i+1][j+1])
                    next_neighbours.append(cells[i+1][j])
                elif i == NUMBER_OF_CELLS_PER_ROW-1:
                    next_neighbours.append(cells[i-1][j-1])
                    next_neighbours.append(cells[i-1][j])
                    next_neighbours.append(cells[i-1][j+1])
                    next_neighbours.append(cells[i][j-1])
                    next_neighbours.append(cells[i][j+1])
                elif j == NUMBER_OF_CELLS_PER_ROW-1:
                    next_neighbours.append(cells[i-1][j])
                    next_neighbours.append(cells[i-1][j-1])
                    next_neighbours.append(cells[i][j-1])
                    next_neighbours.append(cells[i+1][j-1])
                    next_neighbours.append(cells[i+1][j])
                else:
                    next_neighbours.append(cells[i-1][j-1])
                    next_neighbours.append(cells[i-1][j])
                    next_neighbours.append(cells[i-1][j+1])
                    next_neighbours.append(cells[i][j-1])
                    next_neighbours.append(cells[i][j+1])
                    next_neighbours.append(cells[i+1][j-1])
                    next_neighbours.append(cells[i+1][j])
                    next_neighbours.append(cells[i+1][j+1])
            cells[i][j].set_neighbours(next_neighbours.copy())


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
                game_surface
            )
    return cells


def main():
    pg.display.init()
    display_window = pg.display.set_mode(size=(SIZE_OF_WINDOW, SIZE_OF_WINDOW), display=pg.NOFRAME)
    game_surface = pg.display.get_surface()
    cells = generate_cell_array(game_surface)
    associate_neighbours(cells)
    run_game(cells)


if __name__ == "__main__":
    main()
