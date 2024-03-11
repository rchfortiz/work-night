from pyray import ORANGE, BLACK, draw_rectangle, color_alpha, draw_text, clamp


class MotivationBar:
    def __init__(self, x, y, width=300):
        self.x = x
        self.y = y
        self.width = width

        self.percent = 1.0

    def update(self):
        self.percent = clamp(self.percent, 0.0, 1.0)

    def draw(self):
        draw_rectangle(self.x, self.y, self.width, 20, color_alpha(ORANGE, 0.2))
        draw_rectangle(self.x, self.y, int(self.width * self.percent), 20, ORANGE)
        draw_text(
            "Motivation",
            self.x + self.width // 2 - 50,
            self.y + 1,
            20,
            color_alpha(BLACK, 0.25),
        )
