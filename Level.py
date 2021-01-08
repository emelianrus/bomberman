import pygame

from bomberman.Boxes import Box, Wall, Bomb, Floor


class Level:
	level = [
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
		[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]


	def __init__(self):
		self.generate_lvl()
		self.persist_group = pygame.sprite.Group()  # shouldn't be updated
		self.dynamic_blocks_group = pygame.sprite.Group()  # should be updated
		self.floor_blocks_group = pygame.sprite.Group()  # should be updated
		self.level = Level.level


	def generate_lvl(self):
		for i in range(len(self.level)):
			for j in range(len(self.level)):
				if self.level[i][j] == 0:
					self.floor_blocks_group.add(Floor(i, j))
				if self.level[i][j] == 1:
					self.persist_group.add(Wall(i, j))
				if self.level[i][j] == 2:
					self.dynamic_blocks_group.add(Box(i, j))
				if self.level[i][j] == 4:
					self.dynamic_blocks_group.add(Bomb(i, j))

	def get_persist_group(self):
		print(self.persist_group)
		return self.persist_group

	def get_dynamic_group(self):
		return self.dynamic_blocks_group

	def get_floor_blocks_group(self):
		return self.floor_blocks_group
