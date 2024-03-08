import pyray

from .consts import SCREEN_HEIGHT, SCREEN_WIDTH


class ScrollingCamera:
    def __init__(self, zoom=1.1):
        self.cam = pyray.Camera2D(pyray.vector2_zero(), pyray.vector2_zero(), 0.0, zoom)
        self.x_offset = 0.0

    def update(self, environment):
        mouse_pos = pyray.get_mouse_position()
        if mouse_pos.x < SCREEN_WIDTH / 4:
            self.x_offset += 5
        elif mouse_pos.x > (SCREEN_WIDTH / 4) + SCREEN_HEIGHT:
            self.x_offset -= 5

        self.x_offset = pyray.clamp(
            self.x_offset, -(environment.width - (SCREEN_WIDTH / self.cam.zoom)), 0
        )
        self.cam.offset.x = self.x_offset

    def begin(self):
        pyray.begin_mode_2d(self.cam)

    def end(self):
        pyray.end_mode_2d(self.cam)
