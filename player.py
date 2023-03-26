import pygame
from piece import Piece

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
            instance = Piece(977, 115 + (i * 35), "Assets/images/blackPiece.png")
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