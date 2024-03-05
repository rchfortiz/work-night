import pyray

from game.asset_loader import load_texture_asset
from game.scrolling_camera import ScrollingCamera

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

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)
    display_fps()
    # TODO: Finish scrolling camera
    # scrolling_cam.begin()
    pyray.draw_texture(environment, 0, 0, pyray.WHITE)
    # scrolling_cam.end()
    pyray.end_drawing()

pyray.close_window()
