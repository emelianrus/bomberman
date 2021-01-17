import pygame

from game.Boxes import Bomb
from game.Config import Config


class BaseHero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.config = Config()
        self.width = 30
        self.height = 30
        self.image = pygame.image.load(r'img\player.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = self.width
        self.rect.height = self.height
        self.speed = 4

    def move_left(self):
        if self.rect.x - self.speed > 0:
            self.rect.x -= self.speed

    def move_right(self, screen_width):
        if self.rect.x + self.speed + 50 < screen_width:
            self.rect.x += self.speed

    def move_up(self):
        if self.rect.y - self.speed > 0:
            self.rect.y -= self.speed

    def move_down(self, screen_height):
        if self.rect.y + self.speed + 50 < screen_height:
            self.rect.y += self.speed


class Player(BaseHero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.config = Config()
        self.max_bomb = 1
        self.current_bombs = 0
        self.LEVEL = None
        self.image = pygame.image.load(r'img\player.png')

    def movement(self):
        # TODO: change collided logic for player, it should smoothly avoid walls and blocks
        # https://www.pygame.org/docs/ref/event.html
        if pygame.key.get_pressed()[pygame.K_a]:
            self.move_left()
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.move_right(self.config.SCREEN_WIDTH)
        elif pygame.key.get_pressed()[pygame.K_w]:
            self.move_up()
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.move_down(self.config.SCREEN_HEIGHT)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            # TODO: add more than 1 copies while pressing button
            self.LEVEL.add_bomb_to_group(Bomb(int(self.rect.x / 50), int(self.rect.y / 50)))

    def draw(self, win, collided_group):
        self.movement()
        win.blit(pygame.transform.scale(self.image, (self.width, self.height)),
                 (self.rect.x, self.rect.y))

        # draw rect to collided objects
        if self.config.DEBUG:
            pygame.draw.rect(win, (222, 1, 141), (self.rect.x, self.rect.y, self.width, self.height), 4)

        # collide detect
        collide = pygame.sprite.spritecollide(self, collided_group, False)
        if collide:
            collision_tollerance = 10
            for i in collide:
                pygame.draw.rect(win, (255, 111, 4), (i.rect.x, i.rect.y, 50, 50), 8)
                if abs(i.rect.top - self.rect.bottom) < collision_tollerance:
                    self.rect.y -= self.speed  # down
                if abs(i.rect.bottom - self.rect.top) < collision_tollerance:
                    self.rect.y += self.speed  # up
                if abs(i.rect.right - self.rect.left) < collision_tollerance:
                    self.rect.x += self.speed  # left
                if abs(i.rect.left - self.rect.right) < collision_tollerance:
                    self.rect.x -= self.speed  # right


class Enemy(BaseHero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(r'img\enemy.png')
