import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: JUMPING_SHIELD}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5
Y_POS_DUCK = 340

class Dinossaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = JUMP_VEL
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.showe_text = False
        self.shield_time_up = 0



    def update(self, user_input):
        if self.dino_run:
            self.run()

        if self.dino_jump: #pode mudar p elif
            self.jump()
        if self.dino_duck: #pode mudar p elif
            self.duck() #adcionou o metodo duck

        if user_input[pygame.K_UP] and not self.dino_jump: #verifica p pular
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump: #verifica abaixando
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not (self.dino_jump or user_input[pygame.K_DOWN]): #verifica correndo
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False
        
        

        if self.step_index >= 9:
            self.step_index = 0




    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
            
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1
    def duck(self): #metodo duck p abaixar
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

#parecido com o pular