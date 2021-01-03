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

	persist_group = pygame.sprite.Group()  # shouldn't be updated
	dynamic_blocks_group = pygame.sprite.Group()  # should be updated
	floor_blocks_group = pygame.sprite.Group()  # should be updated

	def __init__(self):
		for i in range(len(self.level)):
			for j in range(len(self.level)):
				if self.level[i][j] == 0:
					floor = Floor(i, j)
					self.level[i][j] = Floor(i, j)
					self.floor_blocks_group.add(floor)
				if self.level[i][j] == 1:
					wall = Wall(i, j)
					self.level[i][j] = Wall(i, j)
					self.persist_group.add(wall)
				if self.level[i][j] == 2:
					box = Box(i, j)
					self.level[i][j] = Box(i, j)
					self.dynamic_blocks_group.add(box)
				if self.level[i][j] == 4:
					bomb = Bomb(i, j)
					self.level[i][j] = Bomb(i, j)
					self.dynamic_blocks_group.add(bomb)

	def get_persist_group(self):
		print(self.persist_group)
		return self.persist_group

	def get_dynamic_group(self):
		return self.dynamic_blocks_group

	def get_floor_blocks_group(self):
		return self.floor_blocks_group

	def redraw_window(self):
		pass