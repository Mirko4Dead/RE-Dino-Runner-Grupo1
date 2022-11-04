import random
import pygame

from dino_runner.components.obstacles.bird import Bird
from .cactus import Cactus
from dino_runner.utils.constants import FIRE_TYPE, SWORD_TYPE, BIRD, CACTUS_BREAK, SHIELD_TYPE, FLAME_TYPE, CACTUS_FLAME

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game, user_input):
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
            if user_input[pygame.K_x] and game.player.type == FLAME_TYPE:
                game.player.type = FIRE_TYPE
            elif not user_input[pygame.K_x] and game.player.type == FIRE_TYPE:
                game.player.type = FLAME_TYPE
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type == SHIELD_TYPE:
                    self.obstacles.remove(obstacle)
                elif game.player.type == SWORD_TYPE:
                    self.obstacles[0].images = CACTUS_BREAK
                elif game.player.type == FIRE_TYPE:
                    self.obstacles[0].images = CACTUS_FLAME
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break

    def draw(self, game):
        for obstacle in self.obstacles:
            obstacle.draw(game.screen)

    def reset_obstacles(self):
        self.obstacles = []