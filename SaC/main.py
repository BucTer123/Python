import pygame 

def game(self):
    screen2 = pygame.display.set_mode((800, 600))
    width = screen2.get_width()
    height = screen2.get_height()

    running = True 
    dt = 0
    player_pos = pygame.Vector2(width / 2, height - 590)

    smallfont = pygame.get.SysFont("sans-serif", 35)

    color = (255, 255, 0)
    game_over_color = (0, 255, 255)

    img = pygame.image.load("sprites/main.png").pygame.Surface.convert_alpha()

    player = pygame.transform.scale(img, (67, 69))

    while running:

        if (keys[pygame.K_w]):
            player_pos.y += 300 * dt
        elif (keys[pygame.K_s]):
            player_pos.y -= 300 * dt 
        elif (keys[pygame.K_a]):
            player_pos.x += 300 * dt 
        elif (keys[pygame.K_d]):
            player_pos.x -= 300 * dt
        elif (keys[pygame.K_SPACE]):
            player_pos.y + 30 * dt 
        elif (keys[pygame.K_LCTRL]):
            player_pos.y - 30 * dt
        elif (keys[pygame.K_RCTRL]):
            player_pos.y - 30 * dt 

        elif (player_pos.x == 0 or player_pos.y == 0):
            text = smallfont.render("GAME OVER!", True, game_over_color, 50)

    pygame.quit()


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    width = screen.get_width()
    height = screen.get_height()

    smallfont = pygame.font.SysFont("sans-serif", 35)

    color = (255, 255, 255)

    text = smallfont.render("Press R to start or E to leave ....", True, color)

    dt = 0
    running = True 

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            

        if (keys[pygame.K_r]):
            game()
        elif (keys[pygame.K_e]):
            running = False 

    pygame.quit()


if __name__ == "__main__":
    main()