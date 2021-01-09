class Option:
    def __init__(self, _text, _pos, _colorScheme, _font):
        self.font = _font
        self.text = _text
        self.pos = _pos
        self.hovered = False
        self.colorScheme = _colorScheme
        self.rect = None
        self.rend = None

        self.setRect()

    def draw(self, screen):
        self.setRend()
        screen.blit(self.rend, self.rect)

    def setRend(self):
        self.rend = self.font.render(self.text, True, self.colorScheme[0] if self.hovered else self.colorScheme[1])

    def setRect(self):
        self.setRend()
        self.rect = self.rend.get_rect()
        self.rect.midtop = self.pos

    def update(self):
        self.hovered = not self.hovered
