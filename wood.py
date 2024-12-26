import pygame
import random
from constants import *
from imageLoader import *

class Wood(pygame.sprite.Sprite):

    def __init__(self, x, y, width):
        super().__init__()
        self.image = pygame.transform.scale(wood_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        self.rect.y += scroll
        


def init_platforms(spriteGroup):
    for i in range(10):
        width = random.randint(20, 50)
        x = random.randint(0, SCREEN_WIDTH - width)
        y = random.randint(40, 60) + 40*(i+1)
        w = Wood(x, y, width)
        spriteGroup.add(w)
