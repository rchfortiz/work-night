import pyray, time

from .asset_loader import load_texture_asset
from .clock import Clock
from .consts import CLOCK_X, CLOCK_Y, MONITOR_X, MONITOR_Y, SCREEN_HEIGHT, SCREEN_WIDTH, WORDS_TO_TYPE
from .motivation_bar import MotivationBar
from .scrolling_camera import ScrollingCamera
from .temptation_event import TemptationEvent, temptation_chance
from .typing_game import TypingGame
from .welcome_screen import welcome
from .sfx import play_loaded_sound, play_loaded_music, update_music_streams
from .black_frame import update_black_frame, show_black_frame
from .intro import play_intro

# Initialization of screens
def display_fps():
    fps = pyray.get_fps()
    pyray.draw_text(f"{fps} FPS", 10, 10, 20, pyray.WHITE)


pyray.set_config_flags(pyray.ConfigFlags.FLAG_VSYNC_HINT)
pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Work Night")

environment = load_texture_asset("environment")
black_environment = load_texture_asset("black_environment")

scrolling_cam = ScrollingCamera(0.8, -50.0)
typing_game = TypingGame(MONITOR_X, MONITOR_Y)
clock = Clock(CLOCK_X, CLOCK_Y)
motivation_bar = MotivationBar(10, 10, typing_game)

tempt_event = TemptationEvent(5, 1, typing_game, clock)

play_loaded_music("Ambience")

ending_text = "[INSERT ENDING TEXT]"
which_ending = "[INSERT GOOD OR BAD]"


# Draw Welcome Screen
welcome()

play_intro()

while not pyray.window_should_close():  
    update_music_streams()
    motivation_bar.update()
    typing_game.update(motivation_bar)

    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)
    display_fps()
    scrolling_cam.begin()
    scrolling_cam.update()
    pyray.draw_texture(environment, 0, 0, pyray.WHITE)
    typing_game.draw()
    temptation_chance(tempt_event, 50)
    if tempt_event.ongoing:
        tempt_event.draw(motivation_bar)
        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT):
            tempt_event.click(scrolling_cam)
    clock.update()
    clock.draw()
    update_black_frame(black_environment)

    if typing_game.amount_typed >= WORDS_TO_TYPE:
        print("good ending")
        which_ending = "good"
        ending_text = "The Good Ending!"
        break

    if clock.due:
        print("bad ending")
        which_ending = "bad"
        ending_text = "Too late."
        break

    scrolling_cam.end()
    motivation_bar.draw()
    pyray.end_drawing()

play_loaded_sound(which_ending)
timer = time.time() + 5
while time.time() < timer:
    time.sleep(.001)
    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)

    pyray.draw_text(ending_text, MONITOR_X - int(len(ending_text) * (50 / 2)), MONITOR_Y - 50, 50, pyray.WHITE)
    pyray.end_drawing()
    

pyray.close_window()
