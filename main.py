import pygame
from random import randrange

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Backgammon")
    board = pygame.image.load("Assets/Board.jpg")

    board = pygame.transform.scale(board, (1280, 720))
    print(randrange(0, 6))

    font = pygame.font.SysFont('monaco', 24)
    img = font.render(generateNumber(), True, (0, 0, 0))
    img2 = font.render(generateNumber(), True, (0, 0, 0))


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                img = font.render(generateNumber(), True, (0, 0, 0))
                img2 = font.render(generateNumber(), True, (0, 0, 0))
                pygame.display.update()

        pygame.display.flip()
        screen.blit(board, (0, 0))
        screen.blit(img, (0, 0))
        screen.blit(img2, (0, 20))

    pygame.quit()


def generateNumber():
    return str(randrange(1, 7))

main()
