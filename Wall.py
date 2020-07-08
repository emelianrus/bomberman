import pygame

# Класс для описания платформы
class Wall(pygame.sprite.Sprite):
	def __init__(self, width, height):
		# Конструктор платформ
		super().__init__()
		# Также указываем фото платформы
		self.image = pygame.image.load('img\wall.png')

		# Установите ссылку на изображение прямоугольника
		self.rect = self.image.get_rect()
