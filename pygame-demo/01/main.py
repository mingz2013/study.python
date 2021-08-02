# -*- coding: utf-8 -*-
"""
@FileName: main
@Time: 2021/8/2 16:46
@Author: zhaojm

Module Description

"""


import pygame, sys
from pygame.locals import *




pygame.init()


DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('hello world')

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
