import pygame

from bomberman.BaseHero import Player
from bomberman.Boxes import Bomb
from bomberman.Config import Config
from bomberman.Level import Level
from bomberman.Window import Window


class Game:
    def __init__(self):
        self.config = Config()
        self.RUN: bool = True
        pygame.init()

        self.WIN = Window()

    def start(self):
        level = Level()
        player = Player(50,450)
        player.LEVEL = level
        self.WIN.LEVEL = level

        clock = pygame.time.Clock()
        self.WIN.draw_static_objects()

        self.WIN.collided_group.add([level.get_persist_group(), level.get_dynamic_group()])
        RUN = True
        # print(float(3.44)))
        while RUN:
            clock.tick(self.config.FPS)
            self.WIN.draw_flor_objects()
            self.WIN.draw_dynamic_objects()

            player.draw(self.WIN.WIN)
            self.WIN.draw_bombs_objects()
            player.movement(pygame.key.get_pressed(), self.WIN.collided_group)

            # self.WIN.collide()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        self.end()

    def end(self):
        self.RUN = False
        print("Exit")
        pygame.quit()


Game().start()

