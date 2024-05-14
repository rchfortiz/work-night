import pyray, random
from pathlib import Path
sfx_str = str(Path(__file__).parent.parent / "assets" / "sfx") + "\\"
print(sfx_str)

pyray.init_audio_device()

sounds = {
    'type1': pyray.load_sound(sfx_str + "type1.mp3"),
    'type2': pyray.load_sound(sfx_str + "type2.mp3"),
    'type3': pyray.load_sound(sfx_str + "type3.mp3"),
    'type4': pyray.load_sound(sfx_str + "type4.mp3"),
    'type5': pyray.load_sound(sfx_str + "type5.mp3"),
    'type6': pyray.load_sound(sfx_str + "type6.mp3"),
    'type7': pyray.load_sound(sfx_str + "type7.mp3"),
    'type8': pyray.load_sound(sfx_str + "type8.mp3"),
    'type9': pyray.load_sound(sfx_str + "type9.mp3"),
    'type10': pyray.load_sound(sfx_str + "type10.mp3"),
    'woosh': pyray.load_sound(sfx_str + "woosh.mp3"),
    'good': pyray.load_sound(sfx_str + "good.mp3"),
    'bad': pyray.load_sound(sfx_str + "bad.mp3"),
}

musics = {
    'Ambience': pyray.load_music_stream(sfx_str + "ambience.mp3"),
    'test': pyray.load_music_stream(sfx_str + "test.mp3"),
    'heartbeat': pyray.load_music_stream(sfx_str + "heartbeatloop.mp3")
}

for sound in sounds.keys():
    pyray.set_sound_volume(sounds[sound], 1)

for music in musics.keys():
    pyray.set_music_volume(musics[music], 1)

def play_loaded_music(name: str):
    pyray.play_music_stream(musics[name])

def stop_loaded_music(name: str):
    pyray.stop_music_stream(musics[name])

def play_loaded_sound(name: str):
    pyray.play_sound(sounds[name])

def play_random_typing_sound():
    pyray.play_sound(sounds["type" + str(random.randint(1, 10))])


def update_music_streams():
    for music in musics.keys():
        pyray.update_music_stream(musics[music])