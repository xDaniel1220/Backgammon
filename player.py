import pygame
from piece import Piece

class Player:

    #Initating Player
    def __init__(self, name, startingSide):
        self.name = name

        #Variable to determine which side the player is on (0 or 1)
        self.startingSide = startingSide

        #Number of max pieces a player can have
        self.pieces = 0
        self.currentPiece = 0

        #TODO: Fix player turns
        self.canPlay = False

        #List of the players Pieces
        self.instances = []

        while True:
            if self.pieces < 2:
                for i in range(2):
                    instance = Piece(960, (100 if self.startingSide == 0 else 600) + 
                                     (i * (55 if self.startingSide == 0 else -55)), self.getPieceImage(), name)
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces >= 2 and self.pieces < 7:
                for i in range(5):
                    instance = Piece(156, (100 if self.startingSide == 0 else 600) + 
                                     (i * (55 if self.startingSide == 0 else -55)), self.getPieceImage(), name)
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces >= 7 and self.pieces < 10:
                for i in range(3):
                    instance = Piece(503, (600 if self.startingSide == 0 else 100) + 
                                     (i * (-55 if self.startingSide == 0 else 55)), self.getPieceImage(), name)
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces >= 10 and self.pieces < 15:
                for i in range(5):
                    instance = Piece(612, (600 if self.startingSide == 0 else 100) + 
                                     (i * (-55 if self.startingSide == 0 else 55)), self.getPieceImage(), name)
                    self.instances.append(instance)
                    self.pieces += 1 
            else:
                break
            
                
    #Render the piece on the screen
    def drawPieces(self, surface, font):
        for instance in self.instances:
            instance.renderDebug(surface, font)
            surface.blit(instance.image, instance.rect)

    def getPieceImage(self):
        if self.startingSide == 0:
            return "Assets/images/whitePiece.png"
        else:
            return "Assets/images/blackPiece.png"
    
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