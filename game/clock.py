from datetime import datetime, timedelta, MINYEAR

from pyray import draw_text, BLACK, get_frame_time


class Clock:
    def __init__(self, x, y, initial_hour=8, initial_minute=0, speed=10):
        self.x = x
        self.y = y

        self.speed = speed
        self.time = datetime(MINYEAR, 1, 1, hour=initial_hour, minute=initial_minute)

    def tick(self):
        delta_time = get_frame_time()
        self.time += timedelta(seconds=self.speed * delta_time)

    def update(self):
        self.tick()

    def draw(self):
        draw_text(f"{self.format_time_am_pm()}", self.x, self.y, 20, BLACK)

    def format_time_am_pm(self):
        return self.time.strftime("%I:%M%p")
