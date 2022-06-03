#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from pathlib import Path

from omnirune.pipeline import *
from omnirune.loader import load_file_image


def pipeline_integration_test():
    path = (Path(__file__).parent/'../../data/screenshots/001.jpg').resolve()
    frame = load_file_image(path)
    windows = pipeline(frame)
    print(len(windows), windows[0].shape)


if __name__ == '__main__':
    pipeline_integration_test()