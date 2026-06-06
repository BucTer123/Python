import pygame
from second_file import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")

    pygame.draw.circle(screen, "red", player_pos, 10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    elif keys[pygame.K_s]:
        player_pos.y += 300 * dt
    elif keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    elif keys[pygame.K_d]:
        player_pos.x += 300 * dt
    elif keys[pygame.K_e]:
        exit(0)
    elif keys[pygame.K_0]:
        inventary_function()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()