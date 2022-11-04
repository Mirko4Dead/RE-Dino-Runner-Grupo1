from dino_runner.utils.constants import SWORD_TYPE,SWORD
from.power_up import PowerUp
class Sword(PowerUp):
    def __init__(self):
        super().__init__(SWORD, SWORD_TYPE)
