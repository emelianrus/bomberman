import pygame
from Wall import Wall
# Класс для расстановки платформ на сцене
bg = pygame.image.load('img/background.png')
class Level(object):
	def __init__(self, player):
		# Создаем группу спрайтов (поместим платформы различные сюда)
		self.platform_list = pygame.sprite.Group()
		# Ссылка на основного игрока
		self.player = player

	# Чтобы все рисовалось, то нужно обновлять экран
	# При вызове этого метода обновление будет происходить
	def update(self):
		self.platform_list.update()

	# Метод для рисования объектов на сцене
	def draw(self, screen):
		# Рисуем задний фон
		screen.blit(bg, (0, 0))

		# Рисуем все платформы из группы спрайтов
		self.platform_list.draw(screen)


# Класс, что описывает где будут находится все платформы
# на определенном уровне игры
class Level_01(Level):
	def __init__(self, player):
		# Вызываем родительский конструктор
		Level.__init__(self, player)

		# Массив с данными про платформы. Данные в таком формате:
		# ширина, высота, x и y позиция
		width = 20
		height = 20
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
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
		]

		for y in range(15):
			for x in range(15):
				if level[y][x]:
					block = Wall(width, height)
					block.rect.x = x*50
					block.rect.y = y*50
					block.player = self.player
					self.platform_list.add(block)
