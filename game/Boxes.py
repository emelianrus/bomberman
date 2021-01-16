import pygame


class BaseWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
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


class Box(BaseWall):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 2  # unused
        self.hp = 1  # unused
        self.image = pygame.transform.scale(pygame.image.load(r'img\box.png'), (self.width, self.height))


class Wall(BaseWall):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 1  # unused
        self.hp = 999  # unused


class Floor(BaseWall):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 1  # unused
        self.hp = 999  # unused
        self.image = pygame.transform.scale(pygame.image.load(r'img\ground_grass.png'), (self.width, self.height))


class Explode(BaseWall):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 1  # unused
        self.hp = 999  # unused
        self.create_time_sec = int(((int(pygame.time.get_ticks()) / 1000) % 60))
        self.life_time_sec: int = 1
        self.image = pygame.transform.scale(pygame.image.load(r'img\explosion_a.png'), (self.width, self.height))

    def update(self):
        if int(((int(pygame.time.get_ticks()) / 1000) % 60)) - 1 >= self.create_time_sec:
            self.image = pygame.transform.scale(pygame.image.load(r'img\explosion_c.png'), (50, 50))
            if int(((int(pygame.time.get_ticks()) / 1000) % 60)) - 2 >= self.create_time_sec:
                self.kill()

# TODO: Not sure Bomb class should be here and it should implements BaseWall?
class Bomb(BaseWall):
    def __init__(self, x, y):
        BaseWall.__init__(self, x, y)
        self.id = 4  # unused
        self.hp = 1  # unused
        self.x = x
        self.y = y
        self.life_time_sec = 3  # unused
        self.create_time_sec = int(((int(pygame.time.get_ticks()) / 1000) % 60))
        self.image = pygame.transform.scale(pygame.image.load(r'img\bomb.png'), (self.width, self.height))

    # TODO: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.remove
    def tick(self):
        pass

    def update(self, explode_group):
        if int(((int(pygame.time.get_ticks()) / 1000) % 60)) - self.life_time_sec >= self.create_time_sec:
            self.activate(explode_group)
            self.kill()

    # return explode group
    def activate(self, explode_group):
        e1 = Explode(self.x + 1, self.y)
        e2 = Explode(self.x-1, self.y)
        e3 = Explode(self.x, self.y-1)
        e4 = Explode(self.x, self.y+1)
        e5 = Explode(self.x, self.y)
        explode_group.add([e1,e2,e3,e4,e5])
