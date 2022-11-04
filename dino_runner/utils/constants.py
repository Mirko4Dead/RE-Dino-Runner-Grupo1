import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

FRONT_PAGE = pygame.image.load(os.path.join(IMG_DIR, 'PORTADA.png'))

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
SWORD = pygame.image.load(os.path.join(IMG_DIR, 'Other/sword.png'))
FLAME = pygame.image.load(os.path.join(IMG_DIR, 'flame/flamethrower.png'))

SWORD_RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, 'pruebas/DinoRun1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'pruebas/DinoRun2.png'))
]

SWORD_DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, 'pruebas/DinoDuck1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'pruebas/DinoDuck2.png'))
]

CACTUS_BREAK = [
    pygame.image.load(os.path.join(IMG_DIR, 'pruebas/cacti1_bat_0.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'pruebas/cacti1_bat_1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'pruebas/cacti1_bat_1 - copia.png'))
]

CACTUS_FLAME = [
    pygame.image.load(os.path.join(IMG_DIR, 'flame/cacti1_flame_1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'flame/cacti2_flame_0.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'flame/cacti1_flame_1 - copia.png'))
]

BIRD_FLAME = [
    pygame.image.load(os.path.join(IMG_DIR, 'flame/bird_flame_0.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'flame/bird_flame_1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'flame/bird_flame_0 - copia.png'))
]

FLAME_RUNNING  = [
    pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoRun1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoRun2.png'))
]

FLAME_RUNNING_FLAME  = [
    pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoRun1_flame.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoRun2_flame.png'))
]

FLAME_DUCKING_FLAME = [
    pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoDuck1_flame.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoDuck2_flame.png'))
]

FLAME_DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoDuck1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoDuck2.png'))
]

FLAME_JUMPING = pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoJump.png'))
SWORD_JUMPING = pygame.image.load(os.path.join(IMG_DIR, 'pruebas/DinoJump.png'))
FLAME2_JUMPING = pygame.image.load(os.path.join(IMG_DIR, 'flame/DinoJump_flame.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

LOGO = pygame.image.load(os.path.join(IMG_DIR, 'mschf-logo_1.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
SWORD_TYPE = "sword"
FLAME_TYPE = "flame"
FIRE_TYPE = "fire"

FONT_STYLE = 'dino_runner/utils/PressStart2P-vaV7.ttf'

SOUND_FLAME = 'dino_runner/assets/sound/Flame.mp3'

SOUND = 'dino_runner/assets/sound/sound.mp3'

SOUND_GAME_OVER = 'dino_runner/assets/sound/perdiste.mp3'