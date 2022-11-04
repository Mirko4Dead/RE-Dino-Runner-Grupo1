from random import randint

import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.powerups.flame import Flame
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.sword import Sword


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_powerups(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score.score:
            type = 2
            if type == 0:
                self.power_ups.append(Shield())
            elif type == 1:
                self.power_ups.append(Sword())
            else:
                self.power_ups.append(Flame())
            self.when_appears += randint(200, 300)


    def update(self, game_speed, player: Dinosaur, score):
        self.generate_powerups(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up.type == "flame":
                    power_up.sound.play()
                power_up.start_time = pygame.time.get_ticks()
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups =[]
        self.when_appears = randint(200, 300)

