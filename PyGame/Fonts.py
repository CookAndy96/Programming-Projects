import pygame, sys
import numpy as np
from pygame.locals import *

pygame.init()   # Initialise gamestate?

DISPLAYSURF = pygame.display.set_mode((400,300))    # Initialise GUI - Width x Height

pygame.display.set_caption('Hello World')   # Window captiom

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)

fontObj = pygame.font.Font('impact.ttf', 32)

textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()