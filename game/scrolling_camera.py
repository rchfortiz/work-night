import pyray


class ScrollingCamera:
    def __init__(self, zoom=1.1):
        self.cam = pyray.Camera2D(pyray.vector2_zero(), pyray.vector2_zero(), 0.0, zoom)
        self.x_offset = 0.0

    def update(self):
        self.cam.offset.x = self.x_offset

    def begin(self):
        pyray.begin_mode_2d(self.cam)

    def end(self):
        pyray.end_mode_2d(self.cam)
