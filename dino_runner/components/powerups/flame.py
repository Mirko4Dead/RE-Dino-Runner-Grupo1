import pygame
from dino_runner.components.powerups.power_up import PowerUp
from dino_runner.utils.constants import FLAME, FLAME_TYPE,SOUND_FLAME


class Flame(PowerUp):
    def __init__(self):
        self.sound = pygame.mixer.Sound(SOUND_FLAME)
        super().__init__(FLAME, FLAME_TYPE)