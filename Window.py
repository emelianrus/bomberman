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
        self.PLAYER = Player(50, 300)
        self.LEVEL = Level()

    def game_loop(self, FPS):
        clock = pygame.time.Clock()
        self.draw_static_objects()

        self.collided_group.add([self.LEVEL.get_persist_group(), self.LEVEL.get_dynamic_group()])
        RUN = True
        while RUN:
            clock.tick(FPS)
            self.draw_flor_objects()
            self.draw_dynamic_objects()

            self.PLAYER.movement(pygame.key.get_pressed(), self.collided_group)
            self.draw_player()

            self.collide()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

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

    def draw_bombs_objects(self):
        self.LEVEL.get_bombs_group().draw(self.WIN)

    def draw_flor_objects(self):
        self.LEVEL.get_floor_blocks_group().draw(self.WIN)

    def collide(self):
        collide = pygame.sprite.spritecollide(self.PLAYER, self.collided_group, False)
        if collide:
            for s in collide:
                pygame.draw.rect(self.WIN, (255, 111, 4), (s.rect.x, s.rect.y, 50, 50), 8)

    def draw_player(self):
        self.WIN.blit(pygame.transform.scale(self.PLAYER.image, (self.PLAYER.width, self.PLAYER.height)),
                      (self.PLAYER.rect.x, self.PLAYER.rect.y))
