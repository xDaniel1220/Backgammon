import pygame

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Backgammon")
    test = pygame.image.load("Assets/Board1.jpg")

    test = pygame.transform.scale(test, (1280, 720))


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        screen.blit(test, (0, 0))

    pygame.quit()

main()
