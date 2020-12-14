import pygame as pg


class Cell:
    def __init__(self, initial_state, cell, surface, k):
        self.state = initial_state
        self.next_state = initial_state
        self.cell = cell
        self.game_surface = surface
        self.advance()
        self.neighbours = []
        self.k = k

    def calculate_next_state(self):
        live_count = 0
        for i in self.neighbours:
            if i.state:
                live_count += 1
        if live_count == self.k and not self.state:
            self.next_state = True
        else:
            if self.state:
                if not 1 < live_count < 4:
                    self.next_state = False
            else:
                self.next_state = self.state

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def advance(self):
        self.state = self.next_state
        if self.state:
            pg.draw.rect(self.game_surface, (0, 0, 0), self.cell)
        else:
            pg.draw.rect(self.game_surface, (255, 255, 255), self.cell)
        pg.display.update(self.cell)
