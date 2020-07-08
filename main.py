import pygame
from Player import Player
from Level import Level_01
# Переменные для установки ширины и высоты окна
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750

bg = pygame.image.load('img/background.png')

# Основная функция прогарммы
def main():
	# Инициализация
	pygame.init()

	# Установка высоты и ширины
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)

	# Название игры
	pygame.display.set_caption("Платформер")

	# Создаем игрока
	player = Player()

	# Создаем все уровни
	level_list = []
	level_list.append(Level_01(player))

	# Устанавливаем текущий уровень
	current_level_no = 0
	current_level = level_list[current_level_no]

	active_sprite_list = pygame.sprite.Group()
	player.level = current_level

	player.rect.x = 340
	player.rect.y = SCREEN_HEIGHT - player.rect.height
	active_sprite_list.add(player)

	# Цикл будет до тех пор, пока пользователь не нажмет кнопку закрытия
	done = False

	# Используется для управления скоростью обновления экрана
	clock = pygame.time.Clock()

	# Основной цикл программы
	while not done:
		# Отслеживание действий
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Если закрыл программу, то останавливаем цикл
				done = True

			# Если нажали на стрелки клавиатуры, то двигаем объект
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.go_left()
					x = 0
				if event.key == pygame.K_RIGHT:
					player.go_right()
				if event.key == pygame.K_UP:
					player.go_up()
					break
				if event.key == pygame.K_DOWN:
					player.go_down()

			if event.type == pygame.KEYUP:
				player.stop()

		# Обновляем игрока
		active_sprite_list.update()

		# Обновляем объекты на сцене
		current_level.update()

		# Если игрок приблизится к правой стороне, то дальше его не двигаем
		if player.rect.right > SCREEN_WIDTH:
			player.rect.right = SCREEN_WIDTH

		# Если игрок приблизится к левой стороне, то дальше его не двигаем
		if player.rect.left < 0:
			player.rect.left = 0

		if player.rect.top < 0:
			player.rect.top = 0

		# Если игрок приблизится к левой стороне, то дальше его не двигаем
		if player.rect.bottom > SCREEN_HEIGHT:
			player.rect.bottom = SCREEN_HEIGHT

		# Рисуем объекты на окне
		current_level.draw(screen)
		active_sprite_list.draw(screen)

		# Устанавливаем количество фреймов
		clock.tick(80)

		# Обновляем экран после рисования объектов
		pygame.display.flip()

	# Корректное закртытие программы
	pygame.quit()

main()
