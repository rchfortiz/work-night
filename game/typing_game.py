import random

from pyray import draw_text, is_key_pressed, get_key_pressed, GREEN, GRAY

from .asset_loader import load_text_list_asset

from .consts import WORDS_TO_TYPE

from .sfx import play_random_typing_sound, play_loaded_music


class TypingGame:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_text = ""
        self.current_typing_text = ""
        self.current_typing_index = 0
        self.can_continue_typing = True
        self.amount_typed = 0

        self._word_list = load_text_list_asset("words")

        self.choose_random_text()

    def choose_random_text(self):
        self.current_text = " ".join(random.sample(self._word_list, 4))

    def update(self, motivation_bar):
        if not self.current_text or not self.can_continue_typing:
            return

        letter = self.current_text[self.current_typing_index]
        if letter.upper() == " ":
            self.amount_typed += 1
            self.current_typing_index += 1
        if is_key_pressed(ord(letter.upper())):
            self.current_typing_index += 1
            self.current_typing_text = self.current_text[: self.current_typing_index]
            play_random_typing_sound()
        if get_key_pressed() != 0:
            motivation_bar.percent -= 0.005

        if self.current_typing_text == self.current_text:
            # Finished the text
            self.amount_typed += 1
            self.choose_random_text()
            self.current_typing_text = ""
            self.current_typing_index = 0

    def draw(self):
        draw_text(self.current_text, self.x, self.y, 24, GRAY)
        draw_text(self.current_typing_text, self.x, self.y, 24, GREEN)
        draw_text(str(self.amount_typed) + " / " + str(WORDS_TO_TYPE), self.x, self.y + 28, 24, GREEN)
