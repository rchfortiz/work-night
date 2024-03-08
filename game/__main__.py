import pyray

from .asset_loader import load_texture_asset
from .scrolling_camera import ScrollingCamera
from .typing_game import TypingGame
from .temptation_event import TemptationEvent
from .consts import SCREEN_WIDTH, SCREEN_HEIGHT, MONITOR_X, MONITOR_Y


def display_fps():
    fps = pyray.get_fps()
    pyray.draw_text(f"{fps} FPS", 10, 10, 20, pyray.WHITE)


pyray.set_config_flags(pyray.ConfigFlags.FLAG_VSYNC_HINT)
pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Work Night")

environment = load_texture_asset("environment")

scrolling_cam = ScrollingCamera(SCREEN_HEIGHT / environment.height)
typing_game = TypingGame(MONITOR_X, MONITOR_Y)

# Debugging Test
tempt_event = TemptationEvent(5, 3)
tempt_event.start()

while not pyray.window_should_close():
    typing_game.update()

    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)
    display_fps()
    scrolling_cam.begin()
    scrolling_cam.update(environment)
    pyray.draw_texture(environment, 0, 0, pyray.WHITE)
    typing_game.draw()
    if tempt_event.ongoing:
        tempt_event.draw()
        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT):
            tempt_event.click(scrolling_cam)
    scrolling_cam.end()
    pyray.end_drawing()

pyray.close_window()
