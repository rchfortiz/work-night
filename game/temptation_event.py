import pyray, random, math

from pyray import draw_text, Color, BLACK

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

phrase_list = [
    "Just a few minutes..",
    "Why resist?",
    "Won't take long..",
    "I'll do this tomorrow..",
    "Tonight's gonna be my break..",
]    


class TemptationText():
    def set_text(self, text):
        self.text = text
        self.size = pyray.vector2_zero()
        self.size.y = 30
        self.size.x = len(self.text) * (self.size.y/2)

    def __init__(self, x, y, max_clicks):
        self.x = x
        self.y = y
        self.max_clicks = max_clicks
        self.clicks = 0
        self.shaking_intensity = 1
        self.alpha = 255
        self.set_text(phrase_list[random.randint(0, len(phrase_list) - 1)])
    
    def click(self):
        self.clicks = self.clicks + 1
        self.shaking_intensity = 10
    
    def delete(self):
        self.text = ""
        del self
    
    def draw(self):
        if self.clicks >= self.max_clicks:
            self.alpha = max([0, self.alpha - 5])
        if self.alpha <= 0: 
            self.delete()
        if self.shaking_intensity != 1:
            self.shaking_intensity = self.shaking_intensity - 1
        draw_text(self.text, self.x + random.randint(-1, 1) * self.shaking_intensity, self.y + random.randint(-1, 1) * self.shaking_intensity, 30, self.get_color())
    
    def is_position_within_self(self, position):
        return (self.x < position.x < self.x + self.size.x) and (self.y < position.y < self.y + self.size.y)
    
    def get_color(self):
        return Color(0, 0, 0, self.alpha)


class TemptationEvent():
    def new_texts(self, text_amount, clicks_range):
        self.texts = []
        for i in range(text_amount):
            rand_x = random.randint(math.floor((SCREEN_WIDTH/2) - (SCREEN_WIDTH/3)), math.floor((SCREEN_WIDTH/2) + (SCREEN_WIDTH/3)))
            rand_y = random.randint(math.floor((SCREEN_HEIGHT/2) - (SCREEN_HEIGHT/3)), math.floor((SCREEN_HEIGHT/2) + (SCREEN_HEIGHT/3)))
            self.texts.append(TemptationText(rand_x, rand_y, random.randint(1, clicks_range)))

    def __init__(self, text_amount, clicks_range):
        self.ongoing = False
        self.texts = []
        self.time_started = pyray.get_time()
        self.new_texts(text_amount, clicks_range)

    def start(self):
        self.ongoing = True
        self.time_started = pyray.get_time()

    def draw(self):
        if self.ongoing:
            if len(self.texts) == 0:
                self.ongoing = False
            for text in self.texts:
                if text.text == "":
                    self.texts.pop(self.texts.index(text))
                    continue
                text.draw()

    def click(self):
        mouse_position = pyray.get_mouse_position()
        for text in self.texts:
            if text.is_position_within_self(mouse_position):
                text.click()



        