#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from pathlib import Path

from omnirune.pipeline import *
from omnirune.loader import load_file_image


def pipeline_integration_test():
    path = (Path(__file__).parent/'../../data/screenshots/001.jpg').resolve()
    frame = load_file_image(path)
    pipeline(frame)

pipeline_integration_test()