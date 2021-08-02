# -*- coding: utf-8 -*-
"""
@FileName: main
@Time: 2021/8/2 17:44
@Author: zhaojm

Module Description

"""



import pygame, sys
from pygame.locals import *




pygame.init()


DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('sound')




# DISPLAYSURF.fill(WHITE)

# loading and playing a sound effect
soundObj = pygame.mixer.Sound('beepingsound.wav')
soundObj.play()

# loading and playing background music
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1, 0, 0)
pygame.mixer.music.stop()



while True: # main game loop

    # DISPLAYSURF.fill(WHITE)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
