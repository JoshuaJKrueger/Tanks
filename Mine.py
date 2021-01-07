from pygame import sprite


class Mine(sprite.Sprite):
    def __init__(self, pos, _detonationTimeSec=3, _explosionRadius=75):
        super().__init__()
        self.detonationTimeSec = _detonationTimeSec
        self.explosionRadius = _explosionRadius
        self.image = None  # TODO: Load sprite
        self.rect = self.image.get_rect()

        self.rect.center = pos

    def explode(self):
        pass
