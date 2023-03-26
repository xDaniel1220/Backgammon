import pygame

class Piece:
    def __init__(self, x, y, imagePath):
        self.image = pygame.transform.scale(pygame.image.load(imagePath), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.clicked = False

    #Check whether the player clicked on a piece
    def checkClick(self, mousePos):
        if self.rect.collidepoint(mousePos):
            if self.clicked == True:
                self.clicked = False
            elif self.clicked == False:
                self.clicked = True