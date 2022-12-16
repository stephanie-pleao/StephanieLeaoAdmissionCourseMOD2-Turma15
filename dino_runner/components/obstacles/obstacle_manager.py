import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    game.score -=1 #diminui o score para nao vantagem
                    game.game_speed = 20
                    pygame.time.delay(1000)

                    game.playing = False
                    game.death_count += 1
                    break
            else:
                self.obstacles.remove(obstacle)



    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles = []

