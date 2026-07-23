import pygame
import tkinter as tkinter
import tkinter as ttk

def inventory_window():
    ttk.style("radiance")

    root2 = tk.Tk()
    root2.title("INVENTORY!")
    root2.geometry(300, 300)

    tk.Button(root2, text="Close Inventory", command=starting_game)
    tk.Button(root2, text="Go to Menu", command=main)

    root2.destroy()
    root2.mainloop()

def starting_game():
    pygame.init()
    screen2 = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen2.get_width() / 2, screen2.get_height() / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                inventory_window()

        screen.fill("white")

        pygame.draw.rectangle(screen2, "red", player_pos, 67)

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_w]):
            player_pos.y -= 300 * dt
        elif (keys[pygame.K_s]):
            player_pos.y += 300 * dt
        elif (keys[pygame.K_a]):
            player_pos.x -= 300 * dt
        elif (keys[pygame.K_d]):
            player_pos.x += 300 * dt
        elif (keys[pygame.k_e]):
            create_inventory_window()

        pygame.display.flip()

        clock.tick(60) / 1000

        pygame.quit()

def start_game():
    ttk.style("plastik")

    root = tk.Tk()
    root.title("Starting?")
    root.geometry(300, 200)

    tk.Label(root,text="Do you want to start?")
    
    tk.Button(root, text="Yes", command=starting_game)
    tk.Button(root, text="No", command=exit(0))

    root.destroy()
    root.mainloop()

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    width = screen_get_width()

    height = screen_get_height()

    color = (255, 255, 255)

    color_light = (170, 170, 170)

    color_dark = (100, 100, 100)

    smallfont = pygame.font.SysFont('sans-serif', 35)

    text = smallfont.render('Start', True, color)

    running = True 

    dt = 0

    while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                start_game()
        
        
    screen.fill("white")

    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen, color_light, [width/2,height/2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width/2, height/2, 140, 40])


    screen.blit(text, (width/2+50, height/2))


    pygame.display.update()

if __name__ == "__main__":
    main()
