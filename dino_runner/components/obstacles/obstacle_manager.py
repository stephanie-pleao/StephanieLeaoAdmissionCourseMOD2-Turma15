import pygame
import random

from dino_runner.components.obstacles.cactus import small_cactus, large_cactus ##importa a função do cacto pequeno
from dino_runner.components.obstacles.cactus import large_cactus ##importa a função do cacto grande
from dino_runner.components.obstacles.bird import bird ##importa a função do passaro
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD ##importa a imagem do cacto pequeno, grande, passaro


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0: ##deixa os 3 obstaculos serem escolhidos aleatoriamente
            if random.randint(0, 2) == 0:
                self.obstacles.append(small_cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(large_cactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    game.score -= 1 ## diminuir o score
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                elif game.player.type == 'hammer':
                    self.obstacles.remove(obstacle)
                    game.score += 100

                elif game.player.type == 'shield':
                    self.obstacles.remove(obstacle)
                else:
                    pass

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []           