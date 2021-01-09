import player
import pygame

from bomberman.BaseHero import Player
from bomberman.Level import Level


# draw and redraw everything on screen
class Window:
    def __init__(self):
        self.SCREEN_WIDTH: int = 750
        self.SCREEN_HEIGHT: int = 750
        self.WIN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Game")

        self.persist_group = pygame.sprite.Group()
        self.dynamic_blocks_group = pygame.sprite.Group()
        self.collided_group = pygame.sprite.Group()

        self.LEVEL = Level()
        # self.PLAYER = Player()

    def get_window(self):
        return self.WIN

    def get_window_height(self):
        return self.SCREEN_HEIGHT

    def get_window_width(self):
        return self.SCREEN_WIDTH

    def draw_static_objects(self):
        self.LEVEL.get_persist_group().draw(self.WIN)

    def draw_dynamic_objects(self):
        self.LEVEL.get_dynamic_group().draw(self.WIN)

    def collide(self ):
        collide = pygame.sprite.spritecollide(player, self.collided_group, False)
        if collide:
            for s in collide:
                pygame.draw.rect(self.WIN, (255, 111, 4), (s.rect.x, s.rect.y, 50, 50), 8)

    # def redraw_dynamic(self):
    #     self.LEVEL.get_dynamic_group()
    #     self.dynamic_blocks_group.draw(self.WIN)
    #     self.player.draw(self.WIN)
    #     self.enemy.draw(self.WIN)
    #     pygame.display.update()
    def draw_player(self, player_instance):
        self.WIN.blit(pygame.transform.scale(player_instance.image, (player_instance.width, player_instance.height)),
                      (player_instance.rect.x, player_instance.rect.y))
