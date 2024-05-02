import pyray

from .consts import SCREEN_HEIGHT, SCREEN_WIDTH


class ScrollingCamera:
    def __init__(self, zoom, y_offset, speed=600):
        self.cam = pyray.Camera2D(pyray.vector2_zero(), pyray.vector2_zero(), 0.0, zoom)
        self.speed = speed
        self.x_offset = 0.0
        self.y_offset = y_offset

    def update(self):
        delta_time = pyray.get_frame_time()

        mouse_pos = pyray.get_mouse_position()
        if mouse_pos.x < SCREEN_WIDTH / 4:
            self.x_offset += self.speed * delta_time
        elif mouse_pos.x > (SCREEN_WIDTH / 4) + SCREEN_HEIGHT:
            self.x_offset -= self.speed * delta_time

        # -(environment.width - (SCREEN_WIDTH / self.cam.zoom))
        self.x_offset = pyray.clamp(self.x_offset, -240, 0)
        self.cam.offset.x = self.x_offset
        self.cam.offset.y = self.y_offset

    def begin(self):
        pyray.begin_mode_2d(self.cam)

    def end(self):
        pyray.end_mode_2d(self.cam)
