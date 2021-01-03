import pygame


class BaseWall(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.id: int
		self.width = 50
		self.height = 50
		self.image = pygame.transform.scale(pygame.image.load('img\wall.png'), (self.width, self.height))
		self.rect = self.image.get_rect(center=(x * self.width /2, y* self.width/2))
		self.rect.width = self.width
		self.rect.height = self.height
		self.rect.x = x
		self.rect.y = y
		self.hp: int


	# def draw(self, window):
	# 	window.blit(self.image, (self.rect.x * self.width, self.rect.y * self.height, self.width, self.height))


class Box(BaseWall):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.id = 2
		self.hp = 1
		self.image = pygame.transform.scale(pygame.image.load('img\\box.png'), (self.width,self.height))


class Wall(BaseWall):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.id = 1
		self.hp = 999


class Level:
	level = [
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
		[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]
	box_group = pygame.sprite.Group()

	def __init__(self):
		for i in range(len(self.level)):
			for j in range(len(self.level)):
				if self.level[i][j] == 1:
					wall = Wall(i*50, j*50)
					self.box_group.add(wall)
				if self.level[i][j] == 2:
					box = Box(i*50, j*50)
					self.box_group.add(box)

	def getGroup(self):
		return self.box_group

	def draw(self, window):
		self.box_group.draw(window)

