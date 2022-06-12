#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from typing import Union
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

from omnirune.domain.frame import Frame
from omnirune.domain.rune import RUNES
from omnirune.pipeline import pipeline


def generate_translation_view(frame: Frame, save_path: Union[str, Path]) -> None:
    img_arr = frame.as_array
    img = Image.fromarray(img_arr)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-deva-extra/chandas1-2.ttf', size=24)

    for rune in frame.recognitions:
        draw.regular_polygon((rune['center'][1], rune['center'][0], 53), n_sides=12, outline=(0,0,0))
        draw.text([rune['center'][1], rune['center'][0]], rune['translation'], anchor='ms', fill=(0,0,0), font=font)
    img.save(str(save_path))