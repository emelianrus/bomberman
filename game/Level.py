import pygame

from bomberman.Boxes import Box, Wall, Bomb, Floor
from bomberman.mapgenerator.MapGenerator import MapGenerator


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
					self.floor_group.add(Floor(i, j))
				if self.level[i][j] == 1:
					self.walls_group.add(Wall(i, j))
				if self.level[i][j] == 2:
					self.box_group.add(Box(i, j))

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

	def add_bomb_to_group(self, bomb_obj):
		self.bombs_group.add(bomb_obj)

# if collided:
# 	if destroyable
# 		kill
