import pygame
from dice import Dice
from player import Player

class Game:

    def __init__(self):
        #Initialize pygame library
        pygame.init()

        self.players = []

        # Playing field creation
        self.board = pygame.transform.scale(pygame.image.load('Assets/images/board.png'), (1000, 600))

        #Initialize Two Dices
        self.dice1 = Dice()
        self.dice2 = Dice()

        # Window setup
        self.windowWidth = 1200
        self.windowHeight = 770

        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption('Backgammon')
        self.backgroundColor = (71, 71, 71)

        # Window center calculation
        self.centerX = self.windowWidth // 2
        self.centerY = self.windowHeight // 2

        self.boardX = self.centerX - self.board.get_width() // 2
        self.boardY = self.centerY - self.board.get_height() // 2

        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)

        #Generate a new player
        self.playerOne = Player("Johny", 0)
        self.playerTwo = Player("Daniel", 1)

        #Add players into a list
        self.players.append(self.playerOne)
        self.players.append(self.playerTwo)

    #Render method
    def onRender(self):
        self.window.fill(self.backgroundColor)
        self.window.blit(self.board, (self.boardX, self.boardY))
        self.dice1.renderDice(self.window, self.centerX, -60, 25)
        self.dice2.renderDice(self.window, self.centerX, 10, 25)

        for player in self.players:
            player.drawPieces(self.window, self.font)
        
        pygame.display.update()

    def onExecute(self):
        while True:
            for event in pygame.event.get():
                #Event Handler implementation
                for player in self.players:
                    player.handleInput(event)
                
                self.dice1.handleInpput(event)
                self.dice2.handleInpput(event)

                if event.type == pygame.QUIT:
                    pygame.quit()

            #Run the render method
            self.onRender()

#Run the game
if __name__ == "__main__":
    game = Game()
    game.onExecute()
