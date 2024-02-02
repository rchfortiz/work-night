import pyray


class ScrollingCamera:
    def __init__(self, zoom: float = 1.1) -> None:
        self.cam = pyray.Camera2D(pyray.vector2_zero(), pyray.vector2_zero(), 0.0, zoom)
        self.x_offset = 0.0

    def update(self) -> None:
        self.cam.offset.x = self.x_offset

    def begin(self) -> None:
        pyray.begin_mode_2d(self.cam)

    def end(self) -> None:
        pyray.end_mode_2d(self.cam)
