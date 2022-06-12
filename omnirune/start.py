#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from argparse import ArgumentParser
from sys import argv
from typing import Union
from pathlib import Path

from omnirune.loader import load_file_image
from omnirune.pipeline import pipeline
from omnirune.view.view import generate_translation_view


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('image_path', type=str, help='Give your image path.')
    parser.add_argument('save_path', type=str, help='Give your save path with jpg/png file extension.')
    args = parser.parse_args()
    return vars(args)

def main(image_path: Union[str, Path], save_path: Union[str, Path]):
    frame = load_file_image(image_path)
    pipeline(frame)
    generate_translation_view(frame, save_path)

if __name__ == '__main__':
    args = parse_args()
    main(args['image_path'], args['save_path'])