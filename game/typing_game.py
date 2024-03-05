import random

from pyray import draw_text, Color, is_key_pressed, BLACK

from game.asset_loader import load_text_list_asset

TRANSLUCENT_BLACK = Color(0, 0, 0, 64)


class TypingGame:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_word = ""
        self.current_typing_word = ""
        self.current_typing_index = 0
        self.can_continue_typing = True

        self._word_list = load_text_list_asset("words")

        self.choose_random_word()

    def choose_random_word(self):
        self.current_word = random.choice(self._word_list)

    def update(self):
        if not self.current_word or not self.can_continue_typing:
            return

        letter = self.current_word[self.current_typing_index]
        if is_key_pressed(ord(letter.upper())):
            self.current_typing_index += 1
            self.current_typing_word = self.current_word[: self.current_typing_index]

        if self.current_typing_word == self.current_word:
            # Finished the word
            self.choose_random_word()
            self.current_typing_word = ""
            self.current_typing_index = 0

    def draw(self):
        draw_text(self.current_word, self.x, self.y, 30, TRANSLUCENT_BLACK)
        draw_text(self.current_typing_word, self.x, self.y, 30, BLACK)
