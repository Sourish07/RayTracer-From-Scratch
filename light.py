from color import Color


class Light:
    def __init__(self, pos, color=Color(1, 1, 1), intensity=0.5):
        self.pos = pos
        self.color = color
        self.intensity = intensity