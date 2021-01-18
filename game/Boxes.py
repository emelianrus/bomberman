import pygame


class Base(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__()
        self.id: int
        self.width = 50
        self.height = 50
        self.image = pygame.transform.scale(pygame.image.load(r'img\wall.png'), (self.width, self.height))
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
        self.image = pygame.transform.scale(pygame.image.load(r'img\box.png'), (self.width, self.height))


class Wall(Base):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 1  # unused
        self.hp = 999  # unused


class Floor(Base):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 1  # unused
        self.hp = 999  # unused
        self.image = pygame.transform.scale(pygame.image.load(r'img\ground_grass.png'), (self.width, self.height))


class Explode(Base):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 1  # unused
        self.hp = 999  # unused
        self.create_time_sec = int(((int(pygame.time.get_ticks()) / 1000) % 60))
        self.life_time_sec: int = 1
        self.image = pygame.transform.scale(pygame.image.load(r'img\explosion_a.png'), (self.width, self.height))

    def update(self):
        # TODO: somewhere here bug with undeleted objects
        if int(((int(pygame.time.get_ticks()) / 1000) % 60)) - 1 >= self.create_time_sec:
            self.image = pygame.transform.scale(pygame.image.load(r'img\explosion_c.png'), (50, 50))
            if int(((int(pygame.time.get_ticks()) / 1000) % 60)) - 2 >= self.create_time_sec:
                self.kill()


# TODO: Not sure Bomb class should be here and it should implements BaseWall?
class Bomb(Base):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.id = 4  # unused
        self.hp = 1  # unused
        self.x = x
        self.y = y
        self.life_time_sec = 3  # unused
        self.create_time_sec = int(((int(pygame.time.get_ticks()) / 1000) % 60))
        self.image = pygame.transform.scale(pygame.image.load(r'img\bomb.png'), (self.width, self.height))

    def update(self, explode_group):
        # TODO: somewhere here bug with undeleted objects
        if int(((int(pygame.time.get_ticks()) / 1000) % 60)) - self.life_time_sec >= self.create_time_sec:
            self.activate(explode_group)
            self.kill()

    # return explode group
    def activate(self, explode_group):
        power = 3
        for i in range(1, power+1):
            Explode(self.x + i, self.y, explode_group)
            Explode(self.x - i, self.y, explode_group)
            Explode(self.x, self.y - i, explode_group)
            Explode(self.x, self.y + i, explode_group)
        Explode(self.x, self.y, explode_group)
