import random

from dino_runner.components.obstacles.obstacle import Obstacle

class small_cactus(Obstacle): ##classe para os cactos pequenos
    def __init__(self, image):
        self.type = random.randint(0, 2) ##deixa as imagens aleatorias
        super().__init__(image, self.type) ## sobrepoe um metodo
        self.rect.y = 325 ##tamanho do cacto menor


class large_cactus(Obstacle): ##classe cactos grandes
    def __init__(self, image):
        self.type = random.randint(0, 2) ##randomiza as imagens
        super().__init__(image, self.type) ## sobrepoe um metodo
        self.rect.y = 300 ##mostra o tamanho maior do cacto

