import pygame

def main():
    pygame.init()

    pygame.display.set_mode((800, 600))

    width = 800
    height = 600
        
    width_rect = Vector2(width/2)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    smallfont = Font.SysFont("sans-serif", 40)

    clicked = 0

    text = smallfont.render(clicked, True, GREEN)

    running = True

    while running:
        for event in pygame_event.get():
            if event.type == pygame.QUIT:
                running = False
                
    screen.fill(WHITE)

        if (keys(pygame.C):
            clicked += 1
        elif (keys(pygame.R):
            clicked = 0

    screen.bill(text, width()/2, height()/2)

    pygame.display.update()
        
if __name__ == "__main__":
    main()
