from pathlib import Path

import pyray

ASSETS_DIR = Path(__file__).parent.parent / "assets"


def resolve_asset_path(name: str, extension: str) -> str:
    return str(ASSETS_DIR / f"{name}.{extension}")


def load_texture_asset(name: str) -> pyray.Texture2D:
    return pyray.load_texture(resolve_asset_path(name, "png"))


def load_shader_asset(
    vertex_name: str | None = None,
    fragment_name: str | None = None,
) -> pyray.Shader:
    if vertex_name is None and fragment_name is None:
        raise ValueError(
            "At least one of vertex_name or fragment_name must be specified"
        )

    return pyray.load_shader(
        resolve_asset_path(vertex_name, "vs") if vertex_name else 0,
        resolve_asset_path(fragment_name, "fs") if fragment_name else 0,
    )
