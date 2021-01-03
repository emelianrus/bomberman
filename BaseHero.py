import pygame


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
		window.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.rect.x , self.rect.y))
		# debug player rect
		# pygame.draw.rect(window, (222, 1, 141), (self.rect.x , self.rect.y, self.width, self.height), 4)

	def move_left(self):
		self.rect.x -= self.speed

	def move_right(self):
		self.rect.x += self.speed

	def move_up(self):
		self.rect.y -= self.speed

	def move_down(self):
		self.rect.y += self.speed

class Player(BaseHero):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.image = pygame.image.load(r'img\player.png')

class Enemy(BaseHero):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.image = pygame.image.load(r'img\enemy.png')
