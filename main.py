import pygame

from bomberman.BaseHero import Player, Enemy
from bomberman.Level import Level

# >>> Settings
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
DEBUG = True
FPS = 60
WHITE = (255, 255, 255)
# <<< Settings

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")


def main():
	pygame.init()
	clock = pygame.time.Clock()

	player = Player(50, 300)
	enemy = Enemy(50,400)

	blocks_group = pygame.sprite.Group()
	lvl = Level()
	blocks_group.add(lvl.get_group())

	surf_left = pygame.Surface(
		(SCREEN_WIDTH, SCREEN_WIDTH))
	surf_left.fill(WHITE)

	WIN.blit(surf_left, (0, 0))
	blocks_group.draw(WIN)

	def redraw_window():
		# WIN.fill(0)
		player.draw(WIN)
		enemy.draw(WIN)

	run = True
	while run:
		clock.tick(FPS)
		redraw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("Exit")
				run = False

		collide = pygame.sprite.spritecollide(player, blocks_group, False)
		if collide:
			if DEBUG:
				for s in collide:
					pygame.draw.rect(WIN, (255, 111, 4), (s.rect.x, s.rect.y, 50, 50), 8)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and player.rect.x - player.speed > 0:  # left
			player.move_left()
		if keys[pygame.K_d] and player.rect.x + player.speed + 50 < SCREEN_WIDTH:  # right
			player.move_right()
		if keys[pygame.K_w] and player.rect.y - player.speed > 0:  # up
			player.move_up()
		if keys[pygame.K_s] and player.rect.y + player.speed + 50 < SCREEN_HEIGHT:  # down
			player.move_down()
		pygame.display.update()

	pygame.quit()


main()
