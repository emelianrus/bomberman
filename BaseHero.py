import pygame

from bomberman.Boxes import Bomb


class BaseHero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 30
        self.height = 30
        self.image = pygame.image.load(r'img\player.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = self.width
        self.rect.height = self.height
        self.speed = 4

    def draw(self, window):
        self.remove()
        self.kill()
        window.blit(pygame.transform.scale(self.image, (self.width, self.height)),
                    (self.rect.x, self.rect.y))

    # debug player rect
    # pygame.draw.rect(window, (222, 1, 141), (self.rect.x , self.rect.y, self.width, self.height), 4)

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
        self.max_bomb = 1
        self.current_bombs = 0
        self.LEVEL = None
        self.image = pygame.image.load(r'img\player.png')

    def movement(self, keys, collided_group):
        # TODO: change collided logic for player, it should smoothly avoid walls and blocks
        # https://www.pygame.org/docs/ref/event.html
        if keys[pygame.K_a]:
            collide = pygame.sprite.spritecollide(self, collided_group, False)
            if collide:
                self.rect.x += 12
            else:
                self.move_left()
        if keys[pygame.K_d]:
            collide = pygame.sprite.spritecollide(self, collided_group, False)
            if collide:
                self.rect.x -= 12
            else:
                self.move_right(750)  # SCREEN_WIDTH
        if keys[pygame.K_w]:
            collide = pygame.sprite.spritecollide(self, collided_group, False)
            if collide:
                self.rect.y += 12
            else:
                self.move_up()
        if keys[pygame.K_s]:
            collide = pygame.sprite.spritecollide(self, collided_group, False)
            if collide:
                self.rect.y -= 12
            else:
                self.move_down(750)  # SCREEN_HEIGHT
        if keys[pygame.K_SPACE]:
            # TODO: add more than 1 copies while pressing button
            self.LEVEL.add_bomb_to_group(Bomb(int(self.rect.x/50), int(self.rect.y/50)))

class Enemy(BaseHero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(r'img\enemy.png')
