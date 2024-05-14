import random, time, math, datetime

from pyray import (
    draw_text,
    Color,
    vector2_zero,
    get_time,
    get_mouse_position,
    get_screen_to_world_2d,
)

from .consts import SCREEN_WIDTH, SCREEN_HEIGHT
from .asset_loader import load_text_list_asset
from .sfx import play_loaded_sound, play_loaded_music, stop_loaded_music
from .black_frame import show_black_frame


def temptation_chance(tempt_event, chance):
    if time.time() - tempt_event.time_ended > 10:
        random_int = random.randint(1, 100)
        print(random_int, tempt_event.ongoing)
        if random_int <= chance and not tempt_event.ongoing:
            print("sucessful")
            tempt_event.start()
        else:
            tempt_event.time_ended = time.time()


class TemptationText:
    def set_text(self, text):
        self.text = text
        self.size = vector2_zero()
        self.size.y = 30
        self.size.x = len(self.text) * (self.size.y / 2)

    def __init__(self, x, y, max_clicks):
        self.x = x
        self.y = y
        self.max_clicks = max_clicks
        self.clicks = 0
        self.shaking_intensity = 1
        self.alpha = 255
        self._phrases = load_text_list_asset("temptation_phrases")
        self.set_text(self._phrases[random.randint(0, len(self._phrases) - 1)])

    def click(self):
        self.clicks += 1
        self.shaking_intensity = 10
        play_loaded_sound("woosh")

    def delete(self):
        self.text = ""
        del self

    def draw(self):
        if self.clicks >= self.max_clicks:
            self.alpha = max([0, self.alpha - 5])
        if self.alpha <= 0:
            self.delete()
        if self.shaking_intensity != 1:
            self.shaking_intensity -= 1
        draw_text(
            self.text,
            self.x + random.randint(-1, 1) * self.shaking_intensity,
            self.y + random.randint(-1, 1) * self.shaking_intensity,
            30,
            self.get_color(),
        )

    def is_position_within_self(self, position):
        return (self.x < position.x < self.x + self.size.x) and (
            self.y < position.y < self.y + self.size.y
        )

    def get_color(self):
        return Color(255, 255, 255, self.alpha)


class TemptationEvent:
    def new_texts(self, text_amount, clicks_range):
        self.texts = []
        for _ in range(text_amount):
            rand_x = random.randint(
                (SCREEN_WIDTH // 2) - (SCREEN_WIDTH // 3),
                (SCREEN_WIDTH // 2) + (SCREEN_WIDTH // 3),
            )
            rand_y = random.randint(
                (SCREEN_HEIGHT // 2) - (SCREEN_HEIGHT // 3),
                (SCREEN_HEIGHT // 2) + (SCREEN_HEIGHT // 3),
            )
            self.texts.append(
                TemptationText(rand_x, rand_y, random.randint(1, clicks_range))
            )

    def __init__(self, text_amount, clicks_range, typing_game, clock):
        self.ongoing = False
        self.texts = []
        self.time_started = time.time()
        self.time_ended = time.time()
        self.typing_game = typing_game
        self.text_amount = text_amount
        self.clicks_range = clicks_range
        self.clock = clock

    def start(self):
        self.ongoing = True
        self.time_started = time.time()
        self.time_ended = math.inf
        self.new_texts(self.text_amount, self.clicks_range)
        play_loaded_music("heartbeat")

    def draw(self, motivation_bar):
        if self.ongoing:
            self.typing_game.can_continue_typing = False
            if len(self.texts) == 0:
                self.ongoing = False
                if not motivation_bar.resting:
                    self.typing_game.can_continue_typing = True
                self.time_started = math.inf
                self.time_ended = time.time()
                stop_loaded_music("heartbeat")

            for text in self.texts:
                if text.text == "":
                    self.texts.pop(self.texts.index(text))
                    continue
                text.draw()

            if time.time() - self.time_started > 7 and len(self.texts) > 0:
                show_black_frame(2)
                print("Procrastinated!")
                for text in self.texts:
                    text.delete()
                self.clock.time += datetime.timedelta(minutes=30)
                self.time_started = math.inf

    def click(self, cam):
        mouse_position = get_screen_to_world_2d(get_mouse_position(), cam.cam)
        for text in self.texts:
            if text.is_position_within_self(mouse_position):
                text.click()
