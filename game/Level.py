import pygame

from game.Boxes import Box, Wall, Bomb, Floor
from game.mapgenerator.MapGenerator import MapGenerator


# TODO: REFACTOR NEEDED
class Level:

    def __init__(self):
        self.walls_group = pygame.sprite.Group()
        self.floor_group = pygame.sprite.Group()
        self.bombs_group = pygame.sprite.Group()
        self.box_group = pygame.sprite.Group()
        self.explode_group = pygame.sprite.Group()

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

    def add_bomb_to_group(self, x, y):
        collide = pygame.sprite.spritecollide(Bomb(x, y, self.bombs_group), self.walls_group, False)
        if not collide:
            bomb = Bomb(x, y, self.bombs_group)
            # TODO: create explode here?
            # self.bombs_group.add(bomb)
            # self.explode_group.add(Explode)



    def add_explode_to_group(self, explode_obj):
        collide = pygame.sprite.spritecollide(explode_obj, self.walls_group, False)
        if not collide:
            self.explode_group.add(explode_obj)
