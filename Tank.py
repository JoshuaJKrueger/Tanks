from pygame import sprite


class Tank(sprite.Sprite):
    def __init__(self, pos, _speed, _maxShots, _shotCooldownSec, _maxMines, _mineCooldownSec):
        super().__init__()
        self.angleRad = 0
        self.speed = _speed
        self.image = None  # TODO: Load sprite
        self.rect = self.image.get_rect()
        self.maxShots = _maxShots
        self.missiles = []
        self.shotCooldownSec = _shotCooldownSec
        self.maxMines = _maxMines
        self.mines = []
        self.mineCooldownSec = _mineCooldownSec

        self.rect.center = pos

    def move(self, keyboard):
        pass

    def shoot(self):
        pass

    def placeMine(self):
        pass
