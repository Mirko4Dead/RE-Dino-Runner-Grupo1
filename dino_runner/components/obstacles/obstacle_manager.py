import random
import pygame

from dino_runner.components.obstacles.bird import Bird
from .cactus import Cactus
from dino_runner.utils.constants import BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            type = random.randint(0, 2)
            if type == 0:
                type_obstacle = "SMALL"
                self.obstacles.append(Cactus(type_obstacle))
            elif type == 1:
                type_obstacle = "LARGE"
                self.obstacles.append(Cactus(type_obstacle))
            else:
                self.obstacles.append(Bird(BIRD))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                game.death_count += 1

    def draw(self, game):
        for obstacle in self.obstacles:
            obstacle.draw(game.screen)

    def reset_obstacles(self):
        self.obstacles = []