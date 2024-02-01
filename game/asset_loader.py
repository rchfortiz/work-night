from pathlib import Path

import pyray

ASSETS_DIR = Path(__file__).parent.parent / "assets"


def load_texture_asset(name: str) -> pyray.Texture2D:
    return pyray.load_texture(str(ASSETS_DIR / f"{name}.png"))
