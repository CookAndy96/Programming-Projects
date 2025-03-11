import pygame, sys
import numpy as np
from pygame.locals import *

pygame.init()   # Initialise gamestate?

DISPLAYSURF = pygame.display.set_mode((400,300))    # Initialise GUI - Width x Height

pygame.display.set_caption('Hello World')   # Window caption

pygame.Color(255,0,0)   # -> (255,0,0,255) R, G, B, Alpha

spamRect = pygame.Rect(10,20,200,300)   # Creates a rectangular object that starts in the top left x,y coords at 10,20 with width 200 pixels and height 300 pixels

spamRect.right  # find the xcoord of the right edge

spamRect.right = 350
spamRect.left

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

# set up the colors

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE) #Fill background of the window
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))    #Pentagon as there are 5 tuples. DISPLAYSURF is the window itself that it needs to be included in and GREEN is the colour
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4) #Lines that produce a Z shape
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))   #Lines that produce a Z shape
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)   #Lines that produce a Z shape
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    