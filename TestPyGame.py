import pygame

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500
PI = 3.14

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (125, 125, 125)
LIGHT_BLUE_COLOR = (64, 128, 255)
GREEN_COLOR = (0, 200, 64)
YELLOW_COLOR = (225, 225, 0)
PINK_COLOR = (230, 50, 230)


pygame.init()

screen = pygame.display.set_mode((WIDTH_DISPLAY,HEIGHT_DISPLAY), pygame.RESIZABLE)


pygame.display.set_caption("Draw primitives")

clock = pygame.time.Clock()

done = True

while done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = False
            
    
    #pygame.draw.lines(screen, YELLOW_COLOR, True, [[10, 10], [140, 70], [280, 20]], 12)
    pygame.draw.lines(screen, YELLOW_COLOR, False, [[50, 250], [100, 100], [150, 250]], 4)
    pygame.draw.lines(screen, YELLOW_COLOR, True, [[200, 250], [200, 100], [300, 100], [300, 250]], 4)
    pygame.draw.lines(screen, YELLOW_COLOR, False, [[350, 100], [450, 250]], 4)
    pygame.draw.lines(screen, YELLOW_COLOR, False, [[350, 250], [450, 100]], 4)
    
    #pygame.draw.line(screen, YELLOW_COLOR, [100, 30], [290, 30], 1)
    # pygame.draw.line(screen, WHITE_COLOR, [10, 30], [290, 15], 3)
    # pygame.draw.line(screen, WHITE_COLOR, [10, 80], [320, 55])
    
    # #aaline згладжена лінія, товщина в цьому
    # # випадку не задається
    #pygame.draw.aaline(screen, WHITE_COLOR, [10, 55], [290, 55], )
    # screen.fill(GREEN_COLOR)
    
    pygame.display.update()