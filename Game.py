import pygame

from bomberman.BaseHero import Player
from bomberman.Window import Window


class Game:
    def __init__(self):
        self.DEBUG: bool = True
        self.FPS: int = 60

        self.RUN: bool = True
        self.clock = pygame.time.Clock()
        pygame.init()

        self.WIN = Window()

    def start(self):

        player = Player(50, 300)

        self.WIN.draw_static_objects()

        while self.RUN:
            self.clock.tick(self.FPS)
            self.WIN.draw_dynamic_objects()

            player.movement(pygame.key.get_pressed())
            self.WIN.draw_player(player)

            # self.WIN.collide()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end()

    def end(self):
        self.RUN = False
        print("Exit")
        pygame.quit()


game = Game()
game.start()
