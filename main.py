import pygame

# Inicializace Pygame
pygame.init()

# Velikost okna
window_width = 1360
window_height = 781

# Vytvoření herního okna
game_display = pygame.display.set_mode((window_width, window_height))

# Nastavení titulku okna
pygame.display.set_caption('Herní okno')

# Pozadí hry
#background_color = (255, 255, 255)
background = pygame.image.load("assets/images/board.png")

# Hlavní smyčka hry
while True:
    # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Vykreslení pozadí
    #game_display.fill(background_color)
    game_display.blit(background, (0,0))

    # Obnova okna
    pygame.display.update()
