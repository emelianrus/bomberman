import pygame

from game.Boxes import Box, Wall, Bomb, Floor, Explode
from game.mapgenerator.MapGenerator import MapGenerator


class Level:

    def __init__(self):
        self.walls_group = pygame.sprite.LayeredDirty()
        self.floor_group = pygame.sprite.LayeredDirty()
        self.bombs_group = pygame.sprite.LayeredDirty()
        self.box_group = pygame.sprite.LayeredDirty()
        self.explode_group = pygame.sprite.LayeredDirty()

        self.level = MapGenerator().get_map()
        self.generate_lvl()

    def generate_lvl(self):
        for i in range(len(self.level)):
            for j in range(len(self.level)):
                # TODO: https://www.pygame.org/docs/ref/rect.html#pygame.Rect.copy
                if self.level[i][j] == 0:
                    Floor(i, j, self.floor_group)
                if self.level[i][j] == 1:
                    Wall(i, j, self.walls_group)
                if self.level[i][j] == 2:
                    Floor(i, j, self.floor_group).dirty = 0
                    Box(i, j, self.box_group)

    def get_bombs_group(self):
        return self.bombs_group

    def get_walls_group(self):
        return self.walls_group

    def get_box_group(self):
        return self.box_group

    def get_floor_group(self):
        return self.floor_group

    def get_explode_group(self):
        return self.explode_group

    def add_bomb_to_group(self, x, y, player):
        bomb = Bomb(x, y, self.bombs_group, player, self)
        collided_group = pygame.sprite.LayeredDirty()
        collided_group.add([self.box_group, self.walls_group])

        collide = pygame.sprite.spritecollide(bomb, collided_group, False)
        if collide:
            bomb.kill()
        if not collide:
            self.bombs_group.add(bomb)

    def add_explode_to_group(self, x, y, power):
        Explode(x, y, self.explode_group)  # center

        def check_collide(explode):
            collide_walls = pygame.sprite.spritecollide(explode, self.walls_group, False)
            collide_box = pygame.sprite.spritecollide(explode, self.box_group, True)
            # TODO: start updating floor tiles after explosion
            collide_floor = pygame.sprite.spritecollide(explode, self.floor_group, False)
            for floor in collide_floor:
                floor.dirty = 2  # 2 it is always dirty

            if collide_walls:
                explode.kill()
                return True

            if collide_box:
                for box in collide_box:
                    box.kill()
                return True

            if not collide_walls:
                self.explode_group.add(explode)

        for i in range(1, power + 1):
            if check_collide(Explode(x + i, y, self.explode_group)):  # right line
                break
        for i in range(1, power + 1):
            if check_collide(Explode(x - i, y, self.explode_group)):  # left line
                break
        for i in range(1, power + 1):
            if check_collide(Explode(x, y - i, self.explode_group)):  # top line
                break
        for i in range(1, power + 1):
            if check_collide(Explode(x, y + i, self.explode_group)):  # down line
                break
