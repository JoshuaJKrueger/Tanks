from pygame import sprite


class Mouse(sprite.Sprite):
    def __init__(self):
        super().__init__()
        '''self.image = None  # TODO: Load sprite
        self.rect = self.image.get_rect()'''
        self.tempPos = None
        self.pressedButtons = []

    def move(self, pos):
        #self.rect.center = pos
        self.tempPos = pos

    def scroll(self):
        pass

    def buttonDown(self, button):
        pass

    def buttonUp(self, button):
        pass
