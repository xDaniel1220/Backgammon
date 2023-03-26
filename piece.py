import pygame

class Piece:
    def __init__(self, x, y, imagePath, pieceOwner):
        self.image = pygame.transform.scale(pygame.image.load(imagePath), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.clicked = False
        self.showOwnerDebug = False
        self.pieceOwner = pieceOwner

    def setPieceOwner(self, player):
        self.pieceOwner = player

    #Check whether the player clicked on a piece
    def checkClick(self, mousePos):
        if self.rect.collidepoint(mousePos):
            if self.clicked == True:
                self.clicked = False
                self.showOwnerDebug = False
            elif self.clicked == False:
                self.clicked = True
                self.showOwnerDebug = True

    def renderDebug(self, window, font):
        if self.showOwnerDebug:
            text = font.render(self.pieceOwner, True, (0, 0, 0))
            window.blit(text, (0, 0))