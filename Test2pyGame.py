import pygame

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (125, 125, 125)
LIGHT_BLUE_COLOR = (64, 128, 255)
GREEN_COLOR = (0, 200, 64)
YELLOW_COLOR = (225, 225, 0)
PINK_COLOR = (230, 50, 230)
PI = 3.14

pygame.init()

screen = pygame.display.set_mode((WIDTH_DISPLAY,HEIGHT_DISPLAY))

pygame.display.set_caption("Draw primitives")


clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
     
    
    pygame.draw.rect(screen, PINK_COLOR, (320, 320, 100, 150), 5)

    pygame.draw.arc(screen, WHITE_COLOR, (10, 50, 100, 100), 0, PI)
    pygame.draw.arc(screen, PINK_COLOR, (50, 30, 400, 150), PI, 2*PI, 3)
    pygame.draw.circle(screen, YELLOW_COLOR, (100, 400), 50,5)
    pygame.draw.circle(screen, PINK_COLOR, (100, 300), 50)
    pygame.draw.ellipse(screen, GREEN_COLOR, (200, 20, 280, 100))
    
#################################

 
    # pygame.draw.rect(screen, WHITE_COLOR, (20, 20, 100, 75))

################################################################

    # r1 = pygame.Rect((150, 20, 100, 75))
    # pygame.draw.rect(screen, YELLOW_COLOR, r1, 8)
    
    pygame.display.update()