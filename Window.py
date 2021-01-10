import pygame

# draw and redraw everything on screen
from bomberman.Config import Config


class Window:
    def __init__(self):
        self.config = Config()
        self.WIN = pygame.display.set_mode((self.config.SCREEN_WIDTH, self.config.SCREEN_HEIGHT))
        pygame.display.set_caption(self.config.GAME_CAPTION)

        self.persist_group = pygame.sprite.Group()
        self.dynamic_blocks_group = pygame.sprite.Group()
        self.collided_group = pygame.sprite.Group()
        self.LEVEL = None
        # self.bombs_objects = pygame.sprite.Group()

    def get_window(self):
        return self.WIN

    def draw_static_objects(self):
        self.LEVEL.get_persist_group().draw(self.WIN)

    def draw_dynamic_objects(self):
        self.LEVEL.get_dynamic_group().draw(self.WIN)

    def draw_bombs_objects(self):
        self.LEVEL.get_bomb_group().draw(self.WIN)

    def draw_flor_objects(self):
        self.LEVEL.get_floor_blocks_group().draw(self.WIN)

    # def collide(self):
    #     collide = pygame.sprite.spritecollide(self.PLAYER, self.collided_group, False)
    #     if collide:
    #         for s in collide:
    #             pygame.draw.rect(self.WIN, (255, 111, 4), (s.rect.x, s.rect.y, 50, 50), 8)


