import pygame
import os

from game.Config import Config


def get_time_sec():
    # float
    return pygame.time.get_ticks() / 1000


class BaseTile(pygame.sprite.DirtySprite):
    def __init__(self, x, y, group):
        super().__init__()
        # 0 means that it is not dirty and therefore not repainted again
        # 1, it is repainted and then set to 0 again
        # 2 then it is always dirty ( repainted each frame, flag is not reset)
        self.config = Config()
        group.add(self)
        self.dirty = 2
        self.id: int
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.create_time_sec: int = get_time_sec()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("img", "wall.png")), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.width = self.width
        self.rect.height = self.height
        self.rect.x = x * self.width
        self.rect.y = y * self.height
        self.hp: int  # unused


class Box(BaseTile):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 2  # unused
        self.hp = 1  # unused
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'box.png')), (self.width, self.height))


class Wall(BaseTile):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 1  # unused
        self.hp = 999  # unused

    # used for HUD update
    def update(self, win):
        win.blit(pygame.transform.scale(self.image, (self.width, self.height)),
                 (self.rect.x, self.rect.y))


# Change flor to dirty sprites
class Floor(BaseTile):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 1  # unused
        self.hp = 999  # unused
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'ground_grass.png')), (self.width, self.height))


class Explode(BaseTile):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 1  # unused
        self.hp = 999  # unused
        self.life_time_sec: int = 1
        self.phase = 1
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'explosion_a.png')), (self.width, self.height))
        self.image2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'explosion_c.png')), (50, 50))

    def update(self):
        if self.config.DEBUG_SHOW_BOMB_TIMERS:
            print(f"{self}::{id(self)}:{self.create_time_sec + 1} >= {get_time_sec()}")
        if self.create_time_sec + 1 <= get_time_sec():
            self.image = self.image2
            if self.config.DEBUG_SHOW_BOMB_TIMERS:
                print(f"{self}:: CHANGE IMAGE")
            if self.create_time_sec + 2 <= get_time_sec():
                if self.config.DEBUG_SHOW_BOMB_TIMERS:
                    print(f"{self}:: KILL")
                self.kill()


class Bomb(BaseTile):
    def __init__(self, x, y, group, player, level):
        super().__init__(x, y, group)
        self.LEVEL = level
        self.PLAYER = player
        self.id = 4  # unused
        self.hp = 1  # unused
        self.life_time_sec = 3  # unused
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'bomb.png')), (self.width, self.height))

    def update(self):
        if self.config.DEBUG_SHOW_BOMB_TIMERS:
            print(f"{self}::{id(self)}:{self.create_time_sec + 3} >= {get_time_sec()}")
        if self.create_time_sec + 3 <= get_time_sec():
            if self.config.DEBUG_SHOW_BOMB_TIMERS:
                print(f"{self}::{id(self)}: ACTIVATED")
            self.activate()
            self.kill()

    def activate(self):
        self.PLAYER.current_bombs -= 1
        self.LEVEL.add_explode_to_group(self.x, self.y, self.PLAYER.power)  # center
