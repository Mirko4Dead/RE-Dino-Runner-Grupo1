from .obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        self.image = image
        super().__init__(self.image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], (self.rect.x, self.rect.y))
        self.index += 1

        