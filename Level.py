import pygame

from bomberman.Boxes import Box, Wall, Bomb, Floor
from bomberman.mapgenerator.MapGenerator import MapGenerator


class Level:

	def __init__(self):
		self.persist_group = pygame.sprite.Group()  # shouldn't be updated
		self.dynamic_blocks_group = pygame.sprite.Group()  # should be updated
		self.floor_blocks_group = pygame.sprite.Group()  # should be updated
		self.bombs_group = pygame.sprite.Group()  # should be updated

		self.level = MapGenerator().get_map()
		self.generate_lvl()

	def generate_lvl(self):
		for i in range(len(self.level)):
			for j in range(len(self.level)):
				# TODO: https://www.pygame.org/docs/ref/rect.html#pygame.Rect.copy
				if self.level[i][j] == 0:
					self.floor_blocks_group.add(Floor(i, j))
				if self.level[i][j] == 1:
					self.persist_group.add(Wall(i, j))
				if self.level[i][j] == 2:
					self.dynamic_blocks_group.add(Box(i, j))
				# if self.level[i][j] == 4:
				# 	self.dynamic_blocks_group.add(Bomb(44, 55))

	def get_persist_group(self):
		return self.persist_group

	def get_bomb_group(self):
		return self.bombs_group

	def add_bomb_to_group(self, bomb_obj):
		self.bombs_group.add(bomb_obj)

	def get_dynamic_group(self):
		return self.dynamic_blocks_group

	def get_floor_blocks_group(self):
		return self.floor_blocks_group
