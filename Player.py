import pygame
class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()

		self.image = pygame.image.load('img\player.png')

		self.rect = self.image.get_rect()

		self.change_x = 0
		self.change_y = 0

	def update(self):
		self.rect.x += self.change_x
		self.rect.y += self.change_y

	def go_left(self):
		self.change_x = -9

	def go_right(self):
		self.change_x = 9

	def go_up(self):
		self.change_y = -9

	def go_down(self):
		self.change_y = 9

	def stop(self):
		self.change_x = 0
		self.change_y = 0
