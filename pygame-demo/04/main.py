# -*- coding: utf-8 -*-
"""
@FileName: main
@Time: 2021/8/2 17:38
@Author: zhaojm

Module Description

"""


import pygame, sys
from pygame.locals import *




pygame.init()


DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('hello world')





BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


DISPLAYSURF.fill(WHITE)

fontObj = pygame.font.Font('BrushScriptStd.otf', 32)
textSurfaceObj = fontObj.render('Hello World!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)



while True: # main game loop

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
