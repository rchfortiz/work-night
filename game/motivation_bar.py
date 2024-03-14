from pyray import ORANGE, PURPLE, BLACK, draw_rectangle, color_alpha, draw_text, clamp


class MotivationBar:
    def __init__(self, x, y, typing_game, width=300):
        self.x = x
        self.y = y
        self.width = width
        self.typing_game = typing_game
        self.resting = False
        self.color = ORANGE

        self.percent = 1.0

    def update(self):
        if self.percent <= 0.01:
            self.resting = True
            self.typing_game.can_continue_typing = False
            self.color = PURPLE
        if self.resting:
            self.percent += 0.0005
            if self.percent >= 0.99:
                self.resting = False
                self.color = ORANGE
                self.typing_game.can_continue_typing = True

        self.percent = clamp(self.percent, 0.0, 1.0)

    def draw(self):
        draw_rectangle(self.x, self.y, self.width, 20, color_alpha(self.color, 0.2))
        draw_rectangle(self.x, self.y, int(self.width * self.percent), 20, self.color)
        draw_text(
            "Motivation",
            self.x + self.width // 2 - 50,
            self.y + 1,
            20,
            color_alpha(BLACK, 0.25),
        )
