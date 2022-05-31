#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from typing import Union
from pathlib import Path
from PIL import Image
from numpy import array

from omnirune.domain.frame import Frame


def load_file_image(path: Union[str, Path]) -> Frame:
    img = Image.open(path)
    img_arr = array(img)
    return Frame(img_arr)