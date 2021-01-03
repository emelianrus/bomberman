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
        self.hp: int


class Box(BaseWall):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 2
        self.hp = 1
        self.image = pygame.transform.scale(pygame.image.load(r'img\box.png'), (self.width, self.height))


class Wall(BaseWall):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 1
        self.hp = 999

# TODO: Not sure Bomb class should be here and it should implements BaseWall?
# class Bomb(BaseWall):
#     def __init__(self,x, y):
#         self.react.x = x
#         self.react.y = y
#         self.power = 3  # will explode near 3 cells

