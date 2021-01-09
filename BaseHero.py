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

	def put_bomb(self):
		pass


class Player(BaseHero):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.image = pygame.image.load(r'img\player.png')

	def movement(self, keys):
		if keys[pygame.K_a]:
			self.move_left()
		if keys[pygame.K_d]:
			self.move_right(750)  # SCREEN_WIDTH
		if keys[pygame.K_w]:
			self.move_up()
		if keys[pygame.K_s]:
			self.move_down(750)  # SCREEN_HEIGHT

	def put_bomb(self):
		pass


class Enemy(BaseHero):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.image = pygame.image.load(r'img\enemy.png')
