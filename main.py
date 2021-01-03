import pygame

from bomberman.BaseHero import Player, Enemy
from bomberman.Level import Level

DEBUG = True
# >>> Settings
FPS = 60
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750

WHITE = (255, 255, 255)
# <<< Settings

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

surf_left = pygame.Surface(
    (SCREEN_WIDTH, SCREEN_WIDTH))
surf_left.fill(WHITE)


def main():
    pygame.init()
    clock = pygame.time.Clock()

    player = Player(50, 300)
    enemy = Enemy(50, 400)

    # TODO: decide what way to choose
    # flor dynamic
    # person dynamic
    # wall persist collided
    # bomb dynamic collided
    # boxes dynamic collided

    # dynamic - update per frame
    # persist - update once
    # collided

    persist_group = pygame.sprite.Group()
    dynamic_blocks_group = pygame.sprite.Group()
    collided_group = pygame.sprite.Group()



    lvl = Level()

    persist_group.add(lvl.get_persist_group())
    dynamic_blocks_group.add(lvl.get_dynamic_group())

    collided_group.add([persist_group, dynamic_blocks_group])

    # one time draw
    persist_group.draw(WIN)

    def redraw_window():
        dynamic_blocks_group.draw(WIN)
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

        collide = pygame.sprite.spritecollide(player, collided_group, False)
        if collide:
            if DEBUG:
                for s in collide:
                    pygame.draw.rect(WIN, (255, 111, 4), (s.rect.x, s.rect.y, 50, 50), 8)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.move_left()
        if keys[pygame.K_d]:
            player.move_right(SCREEN_WIDTH)
        if keys[pygame.K_w]:
            player.move_up()
        if keys[pygame.K_s]:
            player.move_down(SCREEN_HEIGHT)
        pygame.display.update()

    pygame.quit()


main()
