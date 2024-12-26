import pygame
from constants import *
from imageLoader import *

class Player():


    def __init__(self, screen, x, y):
        self.screen = screen
        # self.imageLoader = imageLoader
        self.image = pygame.transform.scale(cat_image, (60, 63))
        # Den enkle måten å kjøre rect på: 
        self.width = 50
        self.height = 60
        # self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x,y)
        self.dy = 0
        self.flipped = False

    def draw(self):
        x_adjust = 10 if self.flipped else 0
        xy = (self.rect.x - x_adjust, self.rect.y - 2)
        self.screen.blit(pygame.transform.flip(self.image, self.flipped, False), xy)
        # For å vise firkanten rundt: 
        # pygame.draw.rect(self.screen, WHITE, self.rect, 2)

    def move(self):
        # Process keypresses
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= X_SPEED
            self.flipped = False
        if keys_pressed[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += X_SPEED
            self.flipped = True

        # Gravitasjon og hopping
        if self.rect.y > SCREEN_HEIGHT:
            self.dy = -JUMP_SPEED
            self.rect.y = SCREEN_HEIGHT - 40
        self.dy += GRAVITY
        self.rect.y += self.dy

    #check collision with platforms
    def check_collision(self, platforms):
        for platform in platforms:
            # Sjekk også med adjusted y posisjon halveis gjennom
            check1 = platform.rect.colliderect(self.rect.x, self.rect.y + self.dy//2, self.width, self.height) 
            check2 = platform.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height)

            if check1 or check2:
                # print("check1 og check2", check1, check2)
                # Funka ikke bra nok? if platform.rect.colliderect(self.rect):
                # Må sjekke at vi er over platformen, og på vei ned:
                if self.rect.bottom < platform.rect.bottom and self.dy > 0:
                    self.rect.bottom = platform.rect.top
                    self.dy = -JUMP_SPEED


