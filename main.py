import pygame

from bomberman.BaseHero import Player, Enemy, BaseHero
from bomberman.Level import Level

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Background
# BG = pygame.transform.scale(pygame.image.load('img/background.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()


def main():
	pygame.init()

	FPS = 60
	run = True

	player_vel = 4


	player = Player(50, 300)
	enemy = Enemy(50,400)


	blocks_group = pygame.sprite.Group()
	lvl = Level()
	blocks_group.add(lvl.getGroup())
	# print(lvl.getGroup())
	WHITE = (255, 255, 255)
	surf_left = pygame.Surface(
		(SCREEN_WIDTH, SCREEN_WIDTH))
	surf_left.fill(WHITE)
	# WIN.blit(surf_left, (0, 0))


	# lvl.getGroup().draw(WIN)
	WIN.blit(surf_left, (0, 0))
	blocks_group.draw(WIN)

	def redraw_window():
		# WIN.fill(0)


		player.draw(WIN)
		enemy.draw(WIN)



	while run:
		clock.tick(FPS)
		redraw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("Exit")
				run = False

		collide = pygame.sprite.spritecollide(player, lvl.getGroup(), False)
		if collide:
			for s in collide:
				pygame.draw.rect(WIN, (255, 111, 4), (s.rect.x, s.rect.y, 50, 50), 8)




		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and player.rect.x - player_vel > 0: # left
			player.move_left()
		if keys[pygame.K_d] and player.rect.x + player_vel + 50 < SCREEN_WIDTH: # right
			player.move_right()
		if keys[pygame.K_w] and player.rect.y - player_vel > 0: # up
			player.move_up()
		if keys[pygame.K_s] and player.rect.y + player_vel + 50 < SCREEN_HEIGHT: # down
			player.move_down()
		pygame.display.update()

	pygame.quit()


main()
