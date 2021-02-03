import pygame
import os

from game.Config import Config


class BaseHero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.config = Config()
        self.x = x
        self.y = y
        self.lives = 1
        self.width = 30
        self.height = 30
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player.png')), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x * 50
        self.rect.y = y * 50
        self.rect.width = self.width
        self.rect.height = self.height
        self.LEVEL = None
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


class Enemy(BaseHero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join('img', 'enemy.png'))


class Player(BaseHero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.config = Config()
        self.max_bomb = 2
        self.current_bombs = 0
        self.power = 2
        self.lives = 3
        self.image = pygame.image.load(os.path.join('img', 'player.png'))
        self.put_bomb_key_pressed = False
        self.bombs_amount = 2

    def put_bomb(self):
        self.put_bomb_key_pressed = True
        # Bomb limit reached
        if self.current_bombs >= self.max_bomb:
            return
        bx = int((self.rect.x+25) / 50)
        by = int((self.rect.y+25) / 50)
        self.LEVEL.add_bomb_to_group(bx, by, self)
        self.current_bombs += 1

    def movement(self, py_event, py_keys):
        for event in py_event:
            if event.type == pygame.KEYUP:
                if event.key == 32:
                    self.put_bomb_key_pressed = False

        if py_keys[pygame.K_a]:
            self.move_left()
        elif py_keys[pygame.K_d]:
            self.move_right(self.config.SCREEN_WIDTH)
        elif py_keys[pygame.K_w]:
            self.move_up()
        elif py_keys[pygame.K_s]:
            self.move_down(self.config.SCREEN_HEIGHT)

        if py_keys[pygame.K_SPACE]:
            if not self.put_bomb_key_pressed:
                self.put_bomb()

    def update(self, win, collided_group):
        if self.lives == 0:
            print("GAME OVER")
            self.config.FPS = 0
        win.blit(pygame.transform.scale(self.image, (self.width, self.height)),
                 (self.rect.x, self.rect.y))

        # draw rect to collided objects
        if self.config.DEBUG:
            pygame.draw.rect(win, (222, 1, 141), (self.rect.x, self.rect.y, self.width, self.height), 4)

        # TODO: should be in draw method?
        # collide detect
        collide = pygame.sprite.spritecollide(self, collided_group, False)
        if collide:
            collision_tollerance = self.config.COLLISION_TOLLERANCE
            for i in collide:
                if self.config.DEBUG:
                    pygame.draw.rect(win, (255, 111, 4), (i.rect.x, i.rect.y, 50, 50), 8)

                if not self.config.NO_CLIP:
                    if abs(i.rect.top - self.rect.bottom) < collision_tollerance:
                        self.rect.y -= self.speed  # down
                    if abs(i.rect.bottom - self.rect.top) < collision_tollerance:
                        self.rect.y += self.speed  # up
                    if abs(i.rect.right - self.rect.left) < collision_tollerance:
                        self.rect.x += self.speed  # left
                    if abs(i.rect.left - self.rect.right) < collision_tollerance:
                        self.rect.x -= self.speed  # right


