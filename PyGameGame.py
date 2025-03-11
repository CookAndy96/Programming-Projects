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