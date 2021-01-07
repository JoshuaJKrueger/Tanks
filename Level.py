from pygame import sprite


class Level:
    def __init__(self):
        self.collidable = sprite.Group()
        self.other = sprite.Group()


class Tile(sprite.Sprite):
    def __init__(self, pos, _isDestructable=False, _collidable=True):
        super().__init__()
        self.isDestructable = _isDestructable
        self.collidable = _collidable
        self.image = None  # TODO: Load sprite
        self.rect = self.image.get_rect()

        self.rect.center = pos
