class Option:
    def __init__(self, _text, _pos, _color, _hoverColor, _font):
        self.font = _font
        self.text = _text
        self.pos = _pos
        self.hovered = False
        self.color = _color
        self.hoverColor = _hoverColor
        self.rect = None

        self.setRect()
        self.draw()

    def draw(self, screen):
        self.setRend()
        screen.blit(self.rend, self.rect)

    def setRend(self):
        self.rend = self.font.render(self.text, True, self.chooseColor())

    def chooseColor(self):
        return self.color if self.hovered else self.hoverColor

    def setRect(self):
        self.setRend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        self.hovered = not self.hovered
