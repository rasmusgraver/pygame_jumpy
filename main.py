import pygame
from constants import *

pygame.init()

# Create Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumpy")

# Må init pygame før vi kan gjøre tingene fra imageLoader...
from imageLoader import *
from player import Player
from wood import init_platforms

# set frame rate
clock = pygame.time.Clock()

# image loader
# imageLoader = ImageLoader()

# Our player character
jumpy = Player(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

# The platform group (Vi bruker sprite group, fordi den har innebygged draw funksjon bl.a.)
platform_group = pygame.sprite.Group()
# Initierer 10 tilfeldige platformer
init_platforms(platform_group)

def draw_bg(bg_scroll):
	screen.blit(bg_image, (0, 0 + bg_scroll))
	screen.blit(bg_image, (0, -SCREEN_HEIGHT + bg_scroll))

def main():

    bg_scroll = 0

    run = True
    while run:

        clock.tick(FPS)

        # Check for move / keypresses:
        jumpy.check_collision(platform_group)
        scroll = jumpy.move()

        # Draw background
        # Bedre bare å ha bakgrunnen fast?
        # screen.blit(bg_image, (0,0))
        bg_scroll += scroll
        draw_bg(bg_scroll)

        # Update platforms
        platform_group.update(scroll)

        # Draw sprites
        platform_group.draw(screen)
        jumpy.draw()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()


    pygame.quit()



main()

