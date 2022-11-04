import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from .score import Score
from dino_runner.utils.constants import BG, CLOUD, DEFAULT_TYPE, FRONT_PAGE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, LOGO,SOUND,SOUND_GAME_OVER


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.sound = pygame.mixer.music.load(SOUND)
        self.sound_lose = pygame.mixer.Sound(SOUND_GAME_OVER)

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.power_ups_manager = PowerUpManager()


    def execute (self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        pygame.mixer.music.play()
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = 20
        self.score.score = 0
        self.playing = True
        self.power_ups_manager.reset_power_ups()
        self.player.has_power_up = False
        self.player.type = 'default'

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self,user_input)
        self.score.update(self)
        self.power_ups_manager.update(self.game_speed, self.player, self.score)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.draw_power_up_time()
        self.obstacle_manager.draw(self)
        self.power_ups_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.screen.fill((0, 0, 0))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count == 0:
            self.screen_printing(half_screen_width, half_screen_height + 100, "Press any key to play", (255,255,255), 20)
            self.screen.blit(FRONT_PAGE, (300 , 100))
            self.screen.blit(LOGO, (1000 , 500))
        else:
            self.screen_printing(half_screen_width, half_screen_height + 100, "Press any key to retry", (255,255,255), 20)
            self.screen_printing(half_screen_width, half_screen_height ,f"High Score:{self.score.high_score}", (255,255,255), 20)
            self.screen_printing(half_screen_width, half_screen_height + 50,f"Score:{self.score.score}", (255,255,255), 20)
            self.screen_printing(half_screen_width, half_screen_height -100,f"¡¡¡¡HAS MUERTO!!!!", (255,255,255), 40 )

        pygame.display.update()
        self.handle_key_event_on_menu()

    def handle_key_event_on_menu (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def screen_printing(self, pos_x, pos_y, message, color, size):
        font = pygame.font.Font(FONT_STYLE, size)
        text = font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (pos_x, pos_y)
        self.screen.blit(text, text_rect)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks()) /1000 , 1)
            if time_to_show >= 0:
                self.screen_printing(500, 40,f"{self.player.type.capitalize()} :{time_to_show}", (0, 0, 0), 20)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

