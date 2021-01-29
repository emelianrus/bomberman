import pygame

from game.Window import Window
from game.Config import Config


class Game:
    def __init__(self):
        self.config = Config()
        pygame.init()

        self.WIN = Window()

    def start(self):

        self.WIN.drawing()

        self.end()

    def end(self):
        print("Exit")
        pygame.quit()


Game().start()
