import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class bird(Obstacle): ##classe bird
    def __init__(self, image):
        self.type = 0
        self.image = BIRD
        super().__init__(image, self.type)
        self.rect.y = 250 ##altura que o passaro aparece na tela
        self.index = 0 
    
    def draw(self, screen): ##asas do passaro mesmo esquema das perninhas do dino
        if self.index >= 9: ##reseta a função
            self.index = 0
        screen.blit (self.image[self.index//5], self.rect) ##de 0 ate 4 uma imagem, de 5 até 9 outra imagem
        self.index += 1