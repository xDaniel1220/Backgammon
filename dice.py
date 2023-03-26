import pygame
import random

class Dice:
    def __init__(self):
        #Loading all the dice assets and storing them into a List
        self.dices = [pygame.image.load("Assets/images/dice1.png"),
                      pygame.image.load("Assets/images/dice2.png"),
                      pygame.image.load("Assets/images/dice3.png"),
                      pygame.image.load("Assets/images/dice4.png"),
                      pygame.image.load("Assets/images/dice5.png"),
                      pygame.image.load("Assets/images/dice6.png")]
        
        #Variable to store the dices number
        self.currentDice = 0
        self.diceImage = pygame.transform.scale(self.getCurrentDiceImage(), (50, 50))

    #Event Implementation
    def handleInput(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
                    self.setCurrentDice(self.rollDice())
                    self.diceImage = pygame.transform.scale(self.getCurrentDiceImage(), (50, 50))

    #Random generated number in range 1-6
    def rollDice(self):
        return random.randint(1, 6)

    #Render method to render the dice
    def renderDice(self, window, center_x, posX, posY):
        window.blit(self.diceImage, (center_x + posX, posY))

    def setCurrentDice(self, value):
        self.currentDice = value

    def getCurrentDice(self):
        return self.currentDice

    #Method to return the right dice image according to the dice number
    def getCurrentDiceImage(self):
        return self.dices[self.currentDice - 1]

    def printDices(self):
        print(len(self.dices))
