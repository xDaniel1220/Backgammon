import pygame
import random

class Dice:
    def __init__(self):
        self.dices = [pygame.image.load("Assets/images/Dices/dice1.png"),
                      pygame.image.load("Assets/images/Dices/dice2.png"),
                      pygame.image.load("Assets/images/Dices/dice3.png"),
                      pygame.image.load("Assets/images/Dices/dice4.png"),
                      pygame.image.load("Assets/images/Dices/dice5-2.png"),
                      pygame.image.load("Assets/images/Dices/dice6.png")]
        self.currentDice = 0

    def setCurrentDice(self, value):
        self.currentDice = value

    def getCurrentDice(self):
        return self.currentDice

    def getCurrentDiceImage(self):
        return self.dices[self.currentDice - 1]

    def printDices(self):
        print(len(self.dices))

class Game:

    def init(self):
        #Initialize pygame library
        pygame.init()

        # Playing field creation
        board = pygame.image.load('Assets/images/board.png')
        board_scaled = pygame.transform.scale(board, (1000, 600))

        #Initialize Two Dices
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.initialiteDiceImages()

        # Window setup
        window_width = board.get_width() - (board.get_width() / 2.5)
        window_height = board.get_height() - (board.get_width() / 5.5)

        window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('Backgammon')
        background_color = (71, 71, 71)

        # Window center calculation
        center_x = window_width // 2
        center_y = window_height // 2

        board_x = center_x - board_scaled.get_width() // 2
        board_y = center_y - board_scaled.get_height() // 2

        font = pygame.font.Font(None, 36)
        dice1_output = font.render(str(roll_dice()), True, (255, 255, 255))
        dice2_output = font.render(str(roll_dice()), True, (255, 255, 255))

        roll_button = pygame.image.load('Assets/images/Dices/dice5.png')
        roll_button_scaled = pygame.transform.scale(roll_button, (30, 30))
        roll_button_width = roll_button_scaled.get_width()
        roll_button_height = roll_button_scaled.get_height()
        roll_button_area = pygame.Rect(center_x - 15, 35, roll_button_width, roll_button_height)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    self.dice1.setCurrentDice(roll_dice())
                    self.dice2.setCurrentDice(roll_dice())
                    self.diceImage1 = self.dice1.getCurrentDiceImage()
                    self.diceImage2 = self.dice2.getCurrentDiceImage()

                    self.diceImage1 = pygame.transform.scale(self.diceImage1, (50, 50))
                    self.diceImage2 = pygame.transform.scale(self.diceImage2, (50, 50))

            pygame.display.flip()
            window.fill(background_color)
            window.blit(board_scaled, (board_x, board_y))
            window.blit(self.diceImage1, (center_x - 60, 35))
            window.blit(self.diceImage2, (center_x + 10, 35))

            pygame.display.update()

    def initialiteDiceImages(self):
        self.diceImage1 = self.dice1.getCurrentDiceImage()
        self.diceImage2 = self.dice2.getCurrentDiceImage()

        self.diceImage1 = pygame.transform.scale(self.diceImage1, (50, 50))
        self.diceImage2 = pygame.transform.scale(self.diceImage2, (50, 50))

def roll_dice():
    return random.randint(1, 6)


game = Game()
game.init()
