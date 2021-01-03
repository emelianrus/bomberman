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

	# walls - one time draw
	# blocks - redraw
	# bombs - redraw

	persist_group = pygame.sprite.Group()  # shouldn't be updated
	dynamic_blocks_group = pygame.sprite.Group()  # should be updated

	def __init__(self):
		for i in range(len(self.level)):
			for j in range(len(self.level)):
				if self.level[i][j] == 0:
					floor = Floor(i, j)
					self.level[i][j] = Floor(i, j)
					self.dynamic_blocks_group.add(floor)
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
		return self.persist_group

	def get_dynamic_group(self):
		return self.dynamic_blocks_group

	# def draw(self, window):
	# 	self.box_group.draw(window)

