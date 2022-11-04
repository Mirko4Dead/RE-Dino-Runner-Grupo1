import pygame

from dino_runner.utils.constants import FONT_STYLE


class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0

    def update(self, game):
        self.score +=1
        if self.high_score < self.score:
            self.high_score = self.score
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 13)
        text_component = font.render(f"Your Score: {self.score}", True, (0,0,0) )
        text_high_score = font.render(f"High score: {self.high_score}", True, (0,0,0) )
        text_rect = text_component.get_rect()
        text_rect.center = (950 ,70)
        screen.blit(text_component, text_rect)
        text_rect.center = (950 , 50)
        screen.blit(text_high_score, text_rect)

