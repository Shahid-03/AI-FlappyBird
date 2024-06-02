import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800 


BIRD_FILENAMES = ["bird1.png", "bird2.png", "bird3.png"]

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", filename))) for filename in bird_filenames]

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", pipe.png)))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", base.png)))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", bg.png)))


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25 # max tilt angle when bird moves up and down
    ROT_VEL = 20 # how much bird rotates in each frame
    ANIMATION_TIME = 5 # duration each bird's animation in the frame

    def __init__self(self,x,y): #start postition of bird
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.velocity = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.velocity * self.tick_count + 1.5*self.tick_count**2

        if d >= 16:
            d = 16
        
        if d < 0:
            d -= 2

        self.y += d


    




    