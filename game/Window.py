import pygame

from bomberman.BaseHero import Player
from bomberman.Config import Config
from bomberman.Level import Level


# draw and redraw everything on screen
class Window:
    def __init__(self):
        self.config = Config()
        self.WIN = pygame.display.set_mode((self.config.SCREEN_WIDTH, self.config.SCREEN_HEIGHT))
        pygame.display.set_caption(self.config.GAME_CAPTION)

        self.LEVEL = Level()

    def drawing(self):

        player = Player(50, 450)
        player.LEVEL = self.LEVEL
        self.LEVEL = self.LEVEL

        clock = pygame.time.Clock()

        collided_group = pygame.sprite.Group()

        RUN = True
        while RUN:
            clock.tick(self.config.FPS)
            self.LEVEL.get_floor_group().draw(self.WIN)
            self.LEVEL.get_walls_group().draw(self.WIN)
            self.LEVEL.get_box_group().draw(self.WIN)
            self.LEVEL.get_bombs_group().draw(self.WIN)
            self.LEVEL.get_explode_group().draw(self.WIN)

            # i don't like "add" here
            collided_group.add([self.LEVEL.get_box_group(), self.LEVEL.get_walls_group()])

            player.draw(self.WIN, collided_group)

            self.LEVEL.bombs_group.update(self.LEVEL.get_explode_group())
            self.LEVEL.explode_group.update()



            self.draw_hud()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

    def draw_hud(self):
        font = pygame.font.SysFont("monospace", 25)
        font.set_bold(True)
        millis = pygame.time.get_ticks()
        millis = int(millis)
        seconds = (millis / 1000) % 60
        seconds = int(seconds)
        minutes = (millis / (1000 * 60)) % 60
        minutes = int(minutes)
        hours = (millis / (1000 * 60 * 60)) % 24
        time_in_sec = ("%d:%d:%d" % (hours, minutes, seconds))

        hud = font.render("Time: {}     Level: {}     Lives: {}".format(time_in_sec, 1, 1), 1, (255, 255, 255))

        self.WIN.blit(hud, (15, 15))

    # def collide(self):
    #     collide = pygame.sprite.spritecollide(self.PLAYER, self.collided_group, False)
    #     if collide:
    #         for s in collide:
    #             pygame.draw.rect(self.WIN, (255, 111, 4), (s.rect.x, s.rect.y, 50, 50), 8)
