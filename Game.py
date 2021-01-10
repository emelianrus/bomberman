import pygame

from bomberman.Window import Window


class Game:
    def __init__(self):
        self.FPS: int = 60
        self.RUN: bool = True
        pygame.init()

        self.WIN = Window()

    def start(self):
        self.WIN.game_loop(self.FPS)
        self.end()

    def end(self):
        self.RUN = False
        print("Exit")
        pygame.quit()


game = Game()
game.start()
