import pygame
import random

# Inicializace Pygame
pygame.init()

def roll_dice():
  return random.randint(1, 6)

# Vytvoření hrací plochy
board = pygame.image.load('assets/images/board.png')
board_scaled = pygame.transform.scale(board, (1000, 600))

# Velikost herního okna
window_width = board.get_width() - (board.get_width() / 2.5)
window_height = board.get_height() - (board.get_width() / 5.5)

# Vytvoření herního okna
window = pygame.display.set_mode((window_width, window_height))

# Nastavení titulku okna
pygame.display.set_caption('Backgammon')

# Barva pozadí herního okna
background_color = (71, 71, 71)

# Kalkulace centru okna
center_x = window_width // 2
center_y = window_height // 2

# Kalkulace centru hrací plochy
board_x = center_x - board_scaled.get_width() // 2
board_y = center_y - board_scaled.get_height() // 2

# Vytvoření dvou vrácených hodnot z hodu kostkou
font = pygame.font.Font(None, 36)
dice1_output = font.render(str(roll_dice()), True, (255, 255, 255))
dice2_output = font.render(str(roll_dice()), True, (255, 255, 255))

roll_button = pygame.image.load('assets/images/dice5.png')
roll_button_scaled = pygame.transform.scale(roll_button, (30, 30))
roll_button_width = roll_button_scaled.get_width()
roll_button_height = roll_button_scaled.get_height()
roll_button_area = pygame.Rect(center_x - 15, 35, roll_button_width, roll_button_height)

# Hlavní smyčka hry
while True:
    # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if roll_button_area.collidepoint(event.pos):
                    dice1_output = font.render(str(roll_dice()), True, (255, 255, 255))
                    dice2_output = font.render(str(roll_dice()), True, (255, 255, 255))

    # Vykreslení objektů do okna
    window.fill(background_color)
    window.blit(board_scaled, (board_x, board_y))
    window.blit(dice1_output, (center_x - 60, 40))
    window.blit(dice2_output, (center_x + 50, 40))
    window.blit(roll_button_scaled, roll_button_area)

    # Obnova okna
    pygame.display.update()
