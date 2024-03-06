import pyray

from game.asset_loader import load_texture_asset
from game.scrolling_camera import ScrollingCamera
from game.typing_game import TypingGame
from game.temptation_event import TemptationEvent

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS_CAP = 60


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
for object in tempt_event.texts:
    print(object.text)
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
