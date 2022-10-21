import pygame


#Initialize pygame
pygame.init()



#Set game constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
ROUND_TIME = 25


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_COLOR = (125, 55, 200)

FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont('gabriola', 28)

#Create game window
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Pygame Tutorial~~")


#The main gmae loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Fill the surface
    display_surface.fill(BLACK)
    
    #Update the display and tick the click
    pygame.display.update()
    clock.tick(FPS)


