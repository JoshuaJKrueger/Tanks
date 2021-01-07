from pygame import sprite


class Missile(sprite.Sprite):
    def __init__(self, pos, _speed, _angleRad, _maxBounces):
        self.image = None  # TODO: Load sprite
        self.rect = self.image.get_rect()
        self.speed = _speed
        self.angleRad = _angleRad
        self.maxBounces = _maxBounces
        self.currentBounce = 0

        self.rect.center = pos
