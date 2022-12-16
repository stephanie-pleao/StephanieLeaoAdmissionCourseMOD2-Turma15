import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD

class cloud(Sprite):
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x <- self.rect.width:
            self.x = SCREEN_WIDTH + random.randint(600, 1100)
            self.y = random.randint(50, 100)
            


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))