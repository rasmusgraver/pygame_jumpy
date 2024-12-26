import pygame
from constants import *

pygame.init()

# Create Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumpy")

# Må init pygame før vi kan gjøre tingene fra imageLoader...
from imageLoader import *
from player import Player
from wood import Wood, init_platforms


# set frame rate
clock = pygame.time.Clock()

# image loader
# imageLoader = ImageLoader()

# Our player character
jumpy = Player(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

# The platform group (Vi bruker sprite group, fordi den har innebygged draw funksjon bl.a.)
platforms = pygame.sprite.Group()
# Initierer 10 tilfeldige platformer
init_platforms(platforms)

def main():
    # Game loop
    run = True
    while run:

        clock.tick(FPS)

        # Check for move / keypresses:
        jumpy.check_collision(platforms)
        jumpy.move()

        # Draw background
        screen.blit(bg_image, (0,0))

        # Draw sprites
        platforms.draw(screen)
        jumpy.draw()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()


    pygame.quit()



main()

