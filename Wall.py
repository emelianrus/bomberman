import pygame

class Wall(pygame.sprite.Sprite):
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.image.load('img\wall.png')
		self.rect = self.image.get_rect()
