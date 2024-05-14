import pyray, time
from .consts import INTRO_TEXT_1, INTRO_TEXT_2, MONITOR_X, MONITOR_Y
from .sfx import play_random_typing_sound

current_intro_text = ""

character_speed = .05
which_text = INTRO_TEXT_1
still_on_text_1 = True

time_for_next_char = time.time() + character_speed
def next_character():
    global current_intro_text, which_text, still_on_text_1, time_for_next_char 
    if len(current_intro_text) == len(which_text) and which_text != INTRO_TEXT_2:
        which_text = INTRO_TEXT_2
        time_for_next_char = time.time() + 1
    if time.time() > time_for_next_char:
        if which_text == INTRO_TEXT_2 and still_on_text_1:
            current_intro_text = ""
            time_for_next_char = time.time() + 1
            still_on_text_1 = False
        else:
            time_for_next_char = time.time() + character_speed
            current_intro_text = current_intro_text + which_text[int(pyray.clamp(len(current_intro_text), 0, len(which_text) - 1))]
            play_random_typing_sound()

def play_intro():
    still_on_text_1 = True
    timer = time.time() + 7
    while time.time() < timer:
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        next_character()

        pyray.draw_text(current_intro_text, MONITOR_X - int(len(INTRO_TEXT_1) * 21), MONITOR_Y - 50, 50, pyray.WHITE)
        pyray.end_drawing()