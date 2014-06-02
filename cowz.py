import pygame
import math
import sys

class Cow:

    def __init__(self, pos):
        self.image = pygame.image.load("resources/small-cow.png")
        self.pos = list(pos)
        self.destination = list(pos)
        self.speed = 1
        self.vel = [0, 0]

    def update(self):
        if int(self.pos[0]) != int(self.destination[0]) \
           and int(self.pos[1]) != int(self.destination[1]):
            self.moove()

    def moove(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def set_destination(self, pos):
        x = pos[0] - self.image.get_rect().center[0]
        y = pos[1] - self.image.get_rect().center[1]
        self.destination=[x,y]
        delta_x = x - self.pos[0]
        delta_y = y - self.pos[1]
        hypot = math.sqrt((delta_x ** 2) + (delta_y ** 2))
        vel_x = delta_x / hypot
        vel_y = delta_y / hypot
        self.vel = [vel_x * self.speed, vel_y * self.speed] 

    def draw(self, screen):
        screen.blit(self.image, self.pos)

class Game:

    def __init__(self):
        self.running = True
        self.cow = Cow((320,240))

    def main(self, screen):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.cow.set_destination(pygame.mouse.get_pos())
            self.update()
            self.draw(screen)
        pygame.quit()
        sys.exit()

    def update(self):
        self.cow.update()

    def draw(self, screen):
        screen.fill((200, 200, 200))
        self.cow.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Cowz")
    Game().main(screen)
