import pygame

class Player:

    #Initating Player
    def __init__(self, name, startingSide):
        self.name = name

        #Variable to determine which side the player is on (0 or 1)
        self.startingSide = startingSide

        #Number of max pieces a player can have
        self.pieces = 15
        self.currentPiece = 0

        #TODO: Fix player turns
        self.canPlay = False

        #List of the players Pieces
        self.instances = []

        for i in range(self.pieces):
            instance = self.Piece(977, 115 + (i * 35), "Assets/images/blackPiece.png")
            self.instances.append(instance)

    #Render the piece on the screen
    def drawPiece(self, surface):
        for instance in self.instances:
            surface.blit(instance.image, instance.rect)
    
    def getPieces(self):
        return self.pieces
    
    def getCurrentPiece(self):
        return self.currentPiece
    
    def canPlay(self):
        return self.canPlay
    
    def setCanPlay(self, bool):
        self.canPlay = bool

    #Event handler implementation
    def handleInput(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = event.pos
            for instance in self.instances:
                instance.checkClick(mousePos)
        if event.type == pygame.MOUSEMOTION:
            for instance in self.instances:
                if instance.clicked:
                    instance.rect.move_ip(event.rel)
    
    class Piece:
        def __init__(self, x, y, imagePath):
            self.image = pygame.image.load(imagePath)
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