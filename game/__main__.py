import pyray

from .asset_loader import load_texture_asset
from .scrolling_camera import ScrollingCamera
from .typing_game import TypingGame
from .temptation_event import TemptationEvent
from .consts import SCREEN_WIDTH, SCREEN_HEIGHT, FPS_CAP


def display_fps():
    fps = pyray.get_fps()
    pyray.draw_text(f"{fps} FPS", 10, 10, 20, pyray.WHITE)


pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Work Night")
pyray.set_target_fps(FPS_CAP)

environment = load_texture_asset("environment")

scrolling_cam = ScrollingCamera()
typing_game = TypingGame(10, 10)

# Debugging Test
tempt_event = TemptationEvent(5, 3)
tempt_event.start()

while not pyray.window_should_close():
    typing_game.update()

    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)
    display_fps()
    # TODO: Finish scrolling camera
    # scrolling_cam.begin()
    pyray.draw_texture(environment, 0, 0, pyray.WHITE)
    typing_game.draw()
    if tempt_event.ongoing:
        tempt_event.draw()
        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT):
            tempt_event.click()
    # scrolling_cam.end()
    pyray.end_drawing()

pyray.close_window()
