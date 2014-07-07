import pygame
import math
import sys
import random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WIDTH = 640
HEIGHT = 480
SIZE = 5

def scrunch_and_add(a_list, direction):
    # Take a list of numbers.
    # Scrunch them all together, and add them if neighbor is identical
    
    new_list = []
    added_list = []
    for thing in a_list:
        if thing > 0:
            new_list.append(thing)
            
    x = 0
    while x < len(new_list):
        if x + 1 < len(new_list):
            if new_list[x] == new_list[x+1]:
                added_list.append(new_list[x] * 2)
                x += 1
            else:
                added_list.append(new_list[x])
        else:
            added_list.append(new_list[x])
        x += 1
        
    if direction == "right":
        added_list.reverse()
    
    for space in range(4 - len(added_list)):
        added_list.append(0)
        
    if direction == "right":
        added_list.reverse()
        
    return added_list
        
        
    

class Board:

    def __init__(self):
        self.grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.spawn_a_two()
        self.spawn_a_two()
        print self
        
    def __str__(self):
        out = ""
        for row in self.grid:
            out += str(row) + "\n"
        return out
        
    def spawn_a_two(self):
        found_a_zero = False
        for row in self.grid:
            for thing in row:
                if thing == 0:
                    found_a_zero = True
        if found_a_zero == False:
            print "Game Over"
            return
        row = random.randint(0,3)
        column = random.randint(0,3)
        if self.grid[row][column] == 0:
            self.grid[row][column] = 2
        else:
             self.spawn_a_two()

    def update(self):
        pass

    def draw(self, screen):
        pass
        
    def move(self, way):
        original = list(self.grid)
        if way == "left":
            new_grid = self.left

        if original != new_grid:
            self.grid = new_grid
            self.spawn_a_two()

    def left(self):
        new_grid = list(self.grid)
        for index, row in enumerate(new_grid):                
            new_grid[index]=scrunch_and_add(row,"left")
        return(new_grid)              
        

    def right(self):
        for index, row in enumerate(self.grid):
            self.grid[index]=scrunch_and_add(row,"right")  
        self.spawn_a_two()

    def up(self):
        for c in range(4):
            column = []
            for row in self.grid:
                column.append(row[c])
            column = scrunch_and_add(column,"left")

            for index, thing in enumerate(column):
                self.grid[index][c] = thing
        
        self.spawn_a_two()

    def down(self):
        for c in range(4):
            column = []
            for row in self.grid:
                column.append(row[c])
            column = scrunch_and_add(column,"right")
            for index, thing in enumerate(column):
                self.grid[index][c] = thing
                
        self.spawn_a_two()



class Game:

    def __init__(self):
        self.board = Board()
        self.running = True

    def main(self, screen):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        
                    if event.key == pygame.K_LEFT:
                        self.board.move("left")
                        print self.board
                        
                    if event.key == pygame.K_RIGHT:
                        self.board.right()
                        print self.board
                        
                    if event.key == pygame.K_UP:
                        self.board.up()
                        print self.board
                        
                    if event.key == pygame.K_DOWN:
                        self.board.down()
                        print self.board
                        
            
            #self.update()
            #self.draw(screen)

        pygame.quit()
        sys.exit()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((200, 200, 200))
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")
    Game().main(screen)
