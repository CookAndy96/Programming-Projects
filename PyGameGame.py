import pygame, sys
import numpy as np
from pygame.locals import *

pygame.init()   # Initialise gamestate?

DISPLAYSURF = pygame.display.set_mode((400,300))    # Initialise GUI - Width x Height

pygame.display.set_caption('Hello World')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

pygame.Color(255,0,0)   # -> (255,0,0,255) R, G, B, Alpha

spamRect = pygame.Rect(10,20,200,300)   # Creates a rectangular object that starts in the top left x,y coords at 10,20 with width 200 pixels and height 300 pixels

spamRect.right  # find the xcoord of the right edge