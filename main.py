import pygame
import random
from dice import Dice
from player import Player

class Game:

    def __init__(self):
        #Initialize pygame library
        pygame.init()

        # Playing field creation
        self.board = pygame.image.load('Assets/images/board.png')
        self.boardScaled = pygame.transform.scale(self.board, (1000, 600))

        #Initialize Two Dices
        self.dice1 = Dice()
        self.dice2 = Dice()

        # Window setup
        self.windowWidth = self.board.get_width() - (self.board.get_width() / 2.5)
        self.windowHeight = self.board.get_height() - (self.board.get_width() / 5.5)

        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption('Backgammon')
        self.background_color = (71, 71, 71)

        # Window center calculation
        self.centerX = self.windowWidth // 2
        self.centerY = self.windowHeight // 2

        self.board_x = self.centerX - self.boardScaled.get_width() // 2
        self.board_y = self.centerY - self.boardScaled.get_height() // 2

        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)

        #Generate a new player
        self.playerOne = Player("Johny", 1)

    #Render method
    def onRender(self):
        self.window.fill(self.background_color)
        self.window.blit(self.boardScaled, (self.board_x, self.board_y))
        self.dice1.renderDice(self.window, self.centerX, -60, 35)
        self.dice2.renderDice(self.window, self.centerX, 10, 35)
        self.playerOne.drawPiece(self.window)
        pygame.display.update()



    def onExecute(self):
        while True:
            for event in pygame.event.get():
                #Event Handler implementation
                self.playerOne.handleInput(event)
                self.dice1.handleInpput(event)
                self.dice2.handleInpput(event)

                if event.type == pygame.QUIT:
                    pygame.quit()

            #Run the render method
            self.onRender()

if __name__ == "__main__":
    game = Game()
    game.onExecute()
