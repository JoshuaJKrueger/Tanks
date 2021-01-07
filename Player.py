# from Tank import PlayerTank
from pygame import sprite

class Player:
    def __init__(self):
        self.lives = 3
        self.reticle = Reticle()
        # self.tank = PlayerTank()


class Reticle(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = None  # TODO: Load sprite
        self.rect = self.image.get_rect()

    def update(self, pos):
        self.rect.center = pos
