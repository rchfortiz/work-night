# Sole purpose is to show a black frame
import pyray, time, math
from .asset_loader import load_texture_asset

visible_until = -math.inf

def update_black_frame(black_environment):
    time_diff = visible_until - time.time()
    if time_diff > 0:
        pyray.draw_texture(black_environment, 0, 0, pyray.color_alpha(pyray.WHITE, pyray.clamp(time_diff, 0, 1)))

def show_black_frame(length: float):
    global visible_until
    visible_until = time.time() + length