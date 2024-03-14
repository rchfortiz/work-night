from datetime import datetime, timedelta, MINYEAR

from pyray import draw_text, WHITE, get_frame_time, RED


class Clock:
    def __init__(
        self, x, y, initial_hour=8, initial_minute=0, deadline_hour=11, speed=10
    ):
        self.x = x
        self.y = y

        self.speed = speed
        self.deadline = datetime(MINYEAR, 1, 1, deadline_hour)
        self.time = datetime(MINYEAR, 1, 1, initial_hour, initial_minute)
        self.due = False

    def tick(self):
        delta_time = get_frame_time()
        self.time += timedelta(seconds=self.speed * delta_time)

    def update(self):
        self.tick()
        if self.time > self.deadline:
            self.due = True

    def draw(self):
        if not self.due:
            draw_text(f"{self.format_time_am_pm()}", self.x, self.y, 20, WHITE)
        else:
            draw_text("UH OH!", self.x, self.y, 20, RED)

    def format_time_am_pm(self):
        return self.time.strftime("%I:%M%p")
