import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SWORD_RUNNING, SWORD_TYPE, DUCKING, JUMPING, RUNNING ,DEFAULT_TYPE, SHIELD_TYPE,DUCKING_SHIELD,RUNNING_SHIELD,JUMPING_SHIELD,SWORD_JUMPING,SWORD_DUCKING,FLAME_TYPE,FLAME_RUNNING,FLAME_DUCKING,FLAME_JUMPING,FLAME2_JUMPING,FLAME_DUCKING_FLAME,FLAME_RUNNING_FLAME,FIRE_TYPE

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD ,SWORD_TYPE:SWORD_DUCKING, FLAME_TYPE:FLAME_DUCKING, FIRE_TYPE:FLAME_DUCKING}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD,SWORD_TYPE:SWORD_RUNNING, FLAME_TYPE:FLAME_RUNNING, FIRE_TYPE:FLAME_RUNNING_FLAME}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD,SWORD_TYPE:SWORD_JUMPING, FLAME_TYPE:FLAME_JUMPING, FIRE_TYPE:FLAME2_JUMPING}

class Dinosaur(Sprite):
    X_POS = 150
    Y_POS = 310
    JUMP_VELOCITY = 8.5
    Y_POS_DUCKING = 350
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_velocity = self.JUMP_VELOCITY
        self.has_power_up = False
        self.power_up_time_up = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        ##si hay un error al correr aqui podria haber un error
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][0] if self.step_index < 5 else RUN_IMG[self.type] [1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8

        if self.jump_velocity < - self.JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCK_IMG[self.type][0] if self.step_index < 5 else DUCK_IMG[self.type] [1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCKING
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

