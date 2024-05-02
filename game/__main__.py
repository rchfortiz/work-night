import pyray

from .asset_loader import load_texture_asset
from .clock import Clock
from .consts import CLOCK_X, CLOCK_Y, MONITOR_X, MONITOR_Y, SCREEN_HEIGHT, SCREEN_WIDTH
from .motivation_bar import MotivationBar
from .scrolling_camera import ScrollingCamera
from .temptation_event import TemptationEvent, temptation_chance
from .typing_game import TypingGame
from .welcome_screen import welcome


# Initialization of screens
def display_fps():
    fps = pyray.get_fps()
    pyray.draw_text(f"{fps} FPS", 10, 10, 20, pyray.WHITE)


pyray.set_config_flags(pyray.ConfigFlags.FLAG_VSYNC_HINT)
pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Work Night")

environment = load_texture_asset("environment")

scrolling_cam = ScrollingCamera(0.8, -50.0)
typing_game = TypingGame(MONITOR_X, MONITOR_Y)
clock = Clock(CLOCK_X, CLOCK_Y)
motivation_bar = MotivationBar(10, 10, typing_game)

tempt_event = TemptationEvent(5, 3, typing_game, clock)

# Draw Welcome Screen
welcome()

while not pyray.window_should_close():
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
        tempt_event.draw()
        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT):
            tempt_event.click(scrolling_cam)
    clock.update()
    clock.draw()

    if typing_game.amount_typed >= 100:
        print("good ending")
        break

    if clock.due:
        print("bad ending")
        break

    scrolling_cam.end()
    motivation_bar.draw()
    pyray.end_drawing()

pyray.close_window()
