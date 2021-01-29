import pygame
import os


class Base(pygame.sprite.DirtySprite):
    def __init__(self, x, y, group):
        super().__init__()
        self.dirty = 0
        self.id: int
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("img", "wall.png")), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.width = self.width
        self.rect.height = self.height
        self.rect.x = x * self.width
        self.rect.y = y * self.height
        self.hp: int  # unused
        group.add(self)


class Box(Base):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 2  # unused
        self.hp = 1  # unused
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'box.png')), (self.width, self.height))


class Wall(Base):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 1  # unused
        self.hp = 999  # unused

    # used for HUD update
    def update(self, win):
        win.blit(pygame.transform.scale(self.image, (self.width, self.height)),
                 (self.rect.x, self.rect.y))


# Change flor to dirty sprites
class Floor(Base):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 1  # unused
        self.hp = 999  # unused
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'ground_grass.png')), (self.width, self.height))


class Explode(Base):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 1  # unused
        self.hp = 999  # unused
        self.create_time_sec = int(((int(pygame.time.get_ticks()) / 1000) % 60))
        self.life_time_sec: int = 1
        self.phase = 1
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'explosion_a.png')), (self.width, self.height))
        self.image2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'explosion_c.png')), (50, 50))

    def update(self):
        # TODO: somewhere here bug with undeleted objects
        if int(((int(pygame.time.get_ticks()) / 1000) % 60)) - 1 >= self.create_time_sec:
            self.image = self.image2
            if int(((int(pygame.time.get_ticks()) / 1000) % 60)) - 2 >= self.create_time_sec:
                self.kill()


# TODO: Not sure Bomb class should be here and it should implements BaseWall?
class Bomb(Base):
    def __init__(self, x, y, group, power, level):
        super().__init__(x, y, group)
        self.id = 4  # unused
        self.hp = 1  # unused
        self.x = x
        self.y = y
        self.LEVEL = level
        self.power = power
        self.life_time_sec = 3  # unused
        self.create_time_sec = int(((int(pygame.time.get_ticks()) / 1000) % 60))
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'bomb.png')), (self.width, self.height))

    def update(self):
        # TODO: somewhere here bug with undeleted objects
        if int(((int(pygame.time.get_ticks()) / 1000) % 60)) - self.life_time_sec >= self.create_time_sec:
            self.activate()
            self.kill()

    # return explode group
    def activate(self):
        for i in range(1, self.power+1):
            self.LEVEL.add_explode_to_group(self.x + i, self.y)
            self.LEVEL.add_explode_to_group(self.x - i, self.y)
            self.LEVEL.add_explode_to_group(self.x, self.y - i)
            self.LEVEL.add_explode_to_group(self.x, self.y + i)
        self.LEVEL.add_explode_to_group(self.x, self.y)
