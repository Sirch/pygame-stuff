import pygame
import sys

running = True
def run_game():
    global running
    dispatch = {
            pygame.QUIT : exit_game,
            pygame.KEYDOWN : "keydown",
            pygame.MOUSEBUTTONDOWN: "mousebuttondown",
            }
                
    pygame.init()

    SIZE = (640, 400)
    BG_COLOUR = pygame.Color("black")
    LINE_COLOUR = pygame.Color("white")
    
    screen = pygame.display.set_mode(SIZE)
    pos=(50,50)


    while running:
        screen.fill(BG_COLOUR)
        pygame.draw.rect(screen, LINE_COLOUR, (pos[0],pos[1],25,25), 1)
        pygame.display.update()

        for event in pygame.event.get():
            print event
            f = dispatch.get(event.type)
            if f is None:
                pass
            elif f is "keydown":
                print "escape pressed"
                keydown_handler(event.key)
            elif f is "mousebuttondown":
                pos = pygame.mouse.get_pos()
            else: f()
            
                


def keydown_handler(key):
    if key == pygame.K_ESCAPE:
        exit_game()

    
def exit_game():
    global running
    running = False
    

                
#        if event.type == pygame.QUIT:
#           running = False
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_ESCAPE:
#                running = False

if __name__ == "__main__":
    run_game()
    pygame.quit()
    sys.exit()


