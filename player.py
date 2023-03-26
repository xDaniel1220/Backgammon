import pygame
from piece import Piece

class Player:

    #Initating Player
    def __init__(self, name, color):
        self.name = name

        #Variable to determine which side the player is on (B or W)
        self.color = color

        #Number of max pieces a player can have
        self.pieces = 0
        self.currentPiece = 0

        #TODO: Fix player turns
        self.canPlay = False

        #List of the players Pieces
        self.instances = []

        while True:
            if self.pieces < 2 and self.color == "B":
                for i in range(2):
                    instance = Piece(960, 600 + (i * -55), self.getImagePath())
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces >= 2 and self.pieces < 7 and self.color == "B":
                for i in range(5):
                    instance = Piece(156, 600 + (i * -55), self.getImagePath())
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces >= 7 and self.pieces < 10 and self.color == "B":
                for i in range(3):
                    instance = Piece(503, 100 + (i * 55), self.getImagePath())
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces >= 10 and self.pieces < 15 and self.color == "B":
                for i in range(5):
                    instance = Piece(612, 100 + (i * 55), self.getImagePath())
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces < 2 and self.color == "W":
                for i in range(2):
                    instance = Piece(960, 100 + (i * 55), self.getImagePath())
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces >= 2 and self.pieces < 7 and self.color == "W":
                for i in range(5):
                    instance = Piece(156, 100 + (i * 55), self.getImagePath())
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces >= 7 and self.pieces < 10 and self.color == "W":
                for i in range(3):
                    instance = Piece(503, 600 + (i * -55), self.getImagePath())
                    self.instances.append(instance)
                    self.pieces += 1
            elif self.pieces >= 10 and self.pieces < 15 and self.color == "W":
                for i in range(5):
                    instance = Piece(612, 600 + (i * -55), self.getImagePath())
                    self.instances.append(instance)
                    self.pieces += 1 
            else:
                break
                
    def getImagePath(self):
        if self.color == "B":
            return "assets/images/blackPiece.png"
        else:
            return "assets/images/whitePiece.png"
        
    #Tohle pico nejde protože nemůžu return formatted "i" mimo for loop :)))))
    """
    def getPiecePos(self):
        if self.color == "B" and self.pieces < 2:
            return f"{960, 600 + (i * -55)}"
        elif self.color == "B" and self.pieces >= 2 and self.pieces < 7:
            return f"{156, 600 + (i * -55)}"
        elif self.color == "B" and self.pieces >= 7 and self.pieces < 10:
            return f"{503, 100 + (i * 55)}"
        elif self.color == "B" and self.pieces >= 10 and self.pieces < 15:
            return f"{612, 100 + (i * 55)}"
        elif self.color == "W" and self.pieces < 2:
            return f"{960, 100 + (i * 55)}"
        elif self.color == "W" and self.pieces >= 2 and self.pieces < 7:
            return f"{156, 100 + (i * 55)}"
        elif self.color == "W" and self.pieces >= 7 and self.pieces < 10:
            return f"{503, 600 + (i * -55)}"
        elif self.color == "W" and self.pieces >= 10 and self.pieces < 15:
            return f"{612, 600 + (i * -55)}"
    """

    #Render the piece on the screen
    def drawPieces(self, surface):
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