import pygame
import math
import sys
import random

COLOUR = 0
FLOODED = 1
WHITE = (255, 255, 255)
ORANGE = (255,119,0)
RED = (255, 0, 0)
GREEN = (31, 215, 25)
BLUE = (0,0,255)
BLACK = (0, 0, 0)
PINK = (255,119,226),
DARK_RED = (233, 28, 28)

# Some RGB colours.
# COLOURS = [
#     (255,119,226),
#     (255,119,0),
#     GREEN,
#     (0,255,243),
#     (113,21,218),
#     (255,239,52)
#     ]
    
COLOURS = [
        PINK,
        GREEN,
        (0,255,243),
        (113,21,218),
        (255,239,52),
        DARK_RED
        ]

WIDTH = 640
HEIGHT = 480
SIZE = 25

def off_grid(coords, length):
    '''
    Are these coordinates off a grid of a length
    '''
    if min(coords) < 0 or max(coords) == length:
        return True
    return False

class Board:

    def __init__(self, number_squares, rect):
        '''
        The board is a 2x2 square grid of squares with number_squares per side.
        rect is a pygame rect object for the flood game area.
        '''
        self.rect = rect
        self.box_size = [ float(x)/number_squares for x in rect.size ]
        self.grid = []
        self.adjacents = []
        # initialise the grid.
        for row in range(number_squares):
            row = []
            for column in range(number_squares):
                row.append([random.randrange(len(COLOURS)),False])
            self.grid.append(row)
        # start the flood in the top left
        self.grid[0][0][FLOODED] = True
        self.edges=[(0,0)]
        self.edges = self.find_adjacents(self.edges)

    def find_adjacents(self, flood):
        colour = self.grid[0][0][COLOUR]
        local_flood = list(flood)
        flood_edges =[]
        neighbors = [(-1,0),(+1,0),(0,-1),(0,+1)]
        for x,y in local_flood:
            adjacent_tiles_flooded_or_off_grid = 0
            for delta in neighbors:
                inspect_x = x + delta[0]
                inspect_y = y + delta[1]
                if off_grid([inspect_x, inspect_y], len(self.grid[0])):
                    adjacent_tiles_flooded_or_off_grid += 1
                else:
                    inspected_box_colour = self.grid[inspect_x][inspect_y][COLOUR]
                    inspected_box_flooded = self.grid[inspect_x][inspect_y][FLOODED]
                    if inspected_box_colour == colour:
                        adjacent_tiles_flooded_or_off_grid += 1
                        if not inspected_box_flooded:
                            self.grid[inspect_x][inspect_y][FLOODED] = True
                            local_flood.append([inspect_x,inspect_y])

            if adjacent_tiles_flooded_or_off_grid != 4:
                flood_edges.append([x,y])

        return flood_edges


    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 1)
        for idx_y, row in enumerate(self.grid):
            for idx_x, box in enumerate(row):
                box_rect = pygame.Rect((self.rect.left + idx_x * self.box_size[0],
                            self.rect.top + idx_y * self.box_size[1]),
                            self.box_size)
                pygame.draw.rect(screen, COLOURS[box[0]], box_rect, 0)

    def flood(self, rgb):
        colour_picked = COLOURS.index(rgb)
        if self.grid[0][0][COLOUR] == colour_picked:
            return
        self.edges = self.find_adjacents(self.edges)
        count = 0
        for idx_y, row in enumerate(self.grid):
            for idx_x, box in enumerate(row):
                if box[COLOUR] == colour_picked:
                    count += 1
                if box[FLOODED]:
                    count += 1
                    box[COLOUR] = colour_picked

        if count == SIZE ** 2:
            pass

        return count

class Game:

    def __init__(self):
        self.running = True
        self.board = Board(SIZE,pygame.Rect(200,30,400,400))
        self.buttons = []
        for idx, colour in enumerate(COLOURS):
             self.buttons.append([pygame.Rect(30,30+idx*50,40,40),colour])
        self.moves_left = SIZE * 2

    def main(self, screen):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_LEFT:
                        pass
                    if event.key == pygame.K_RIGHT:
                        pass
                    if event.key == pygame.K_UP:
                        pass
                    if event.key == pygame.K_DOWN:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_button_clicked(pygame.mouse.get_pos())
            self.update()
            self.draw(screen)
        pygame.quit()
        sys.exit()

    def check_button_clicked(self, pos):
        for button in self.buttons:
            if button[0].collidepoint(pos):
                count = self.board.flood(button[1])
                if count == SIZE ** 2:
                    print "WINNER"
                else:
                    self.moves_left -= 1
                    print self.moves_left


    def draw_buttons(self, screen):
        for button in self.buttons:
            pygame.draw.rect(screen, button[1], button[0], 0)
        

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)
        self.board.draw(screen)
        self.draw_buttons(screen)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flood")
    Game().main(screen)
