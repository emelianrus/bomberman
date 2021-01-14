
import pygame

from bomberman.Boxes import Bomb, Floor
from bomberman.Config import Config

config = Config()
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("game")
WIN = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

millis = pygame.time.get_ticks()
millis = int(millis)
seconds = (millis / 1000) % 60
seconds = int(seconds)
minutes = (millis / (1000 * 60)) % 60
minutes = int(minutes)
hours = (millis / (1000 * 60 * 60)) % 24

# res = ("%d:%d:%d" % (hours, minutes, seconds))

RUN = True

b = Bomb(1,1)

f1 = Floor(1,1)
f2 = Floor(2,1)
f3 = Floor(0,1)
f4 = Floor(1,0)
f5 = Floor(1,2)
floor_group = pygame.sprite.Group()
bombs_group = pygame.sprite.Group()
floor_group.add([f1,f2,f3,f4,f5])
bombs_group.add(b)

while RUN:
    clock.tick(60)
    game_time = int(((int(pygame.time.get_ticks()) / 1000) % 60))
    floor_group.draw(WIN)
    bombs_group.draw(WIN)
    pygame.display.update()
    for i in bombs_group:
        if game_time-5 > i.create_time_seconds:
            i.activate()
            bombs_group.remove(i)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
            print("Exit")
            pygame.quit()




pygame.display.update()