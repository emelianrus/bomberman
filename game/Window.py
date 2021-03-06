import pygame

from game.BaseHero import Player
from game.Config import Config
from game.Level import Level


# draw and redraw everything on screen
class Window:
    def __init__(self):
        self.config = Config()
        self.WIN = pygame.display.set_mode((self.config.SCREEN_WIDTH, self.config.SCREEN_HEIGHT))
        pygame.display.set_caption(self.config.GAME_CAPTION)
        self.RUN = True
        self.clock = pygame.time.Clock()

        self.LEVEL = Level()

    def drawing(self):

        player = Player(1, 4)
        player.LEVEL = self.LEVEL

        collided_group = pygame.sprite.Group()

        while self.RUN:
            pygame_event = pygame.event.get()
            pygame_key_pressed = pygame.key.get_pressed()

            self.clock.tick(self.config.FPS)
            for event in pygame_event:
                if event.type == pygame.QUIT:
                    self.RUN = False

            self.LEVEL.get_floor_group().draw(self.WIN)
            self.LEVEL.get_walls_group().draw(self.WIN)
            self.LEVEL.get_box_group().draw(self.WIN)
            self.LEVEL.get_bombs_group().draw(self.WIN)
            self.LEVEL.get_explode_group().draw(self.WIN)

            # TODO: i don't like "add" here
            collided_group.add([self.LEVEL.get_box_group(), self.LEVEL.get_walls_group(), self.LEVEL.get_bombs_group()])

            player.update(self.WIN, collided_group)
            player.movement(pygame_event, pygame_key_pressed)

            self.LEVEL.bombs_group.update()
            self.LEVEL.explode_group.update()

            self.draw_hud(player)

            pygame.display.update()

    def draw_hud(self, player):
        # Update walls under the HUD
        for wall in self.LEVEL.get_walls_group():
            if wall.y == 0:
                wall.dirty = 1

        font = pygame.font.SysFont("monospace", 20)
        font.set_bold(True)
        millis = pygame.time.get_ticks()
        millis = int(millis)
        seconds = (millis / 1000) % 60
        seconds = int(seconds)
        minutes = (millis / (1000 * 60)) % 60
        minutes = int(minutes)
        hours = (millis / (1000 * 60 * 60)) % 24
        time_in_sec = ("%d:%d:%d" % (hours, minutes, seconds))

        hud = font.render(f"  Time: {time_in_sec} "
                          f"Level: {1} "
                          f"Lives: {player.lives} "
                          f"Power: {player.power} "
                          f"Bombs: {player.max_bomb - player.current_bombs}", 1, (255, 255, 255))

        self.WIN.blit(hud, (15, 15))
