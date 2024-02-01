import pyray

from game.asset_loader import load_texture_asset

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS_CAP = 60


def main() -> None:
    pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Work Night")
    pyray.set_target_fps(FPS_CAP)

    environment = load_texture_asset("environment")

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        display_fps()
        pyray.draw_texture(environment, 0, 0, pyray.WHITE)
        pyray.end_drawing()

    pyray.close_window()


def display_fps() -> None:
    fps = pyray.get_fps()
    pyray.draw_text(f"{fps} FPS", 10, 10, 20, pyray.WHITE)


if __name__ == "__main__":
    main()
