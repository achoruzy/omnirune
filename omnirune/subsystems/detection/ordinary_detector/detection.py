#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from omnirune.domain.frame import Frame


class Detector:
    """Ordinary heuristic detector for generating non-inteligent windows from Frame object."""
    def __init__(self, window_size: int):
        self.window_size = window_size

    def detect(self, frame: Frame):
        step = self.window_size % 2
        height, width, canal = frame.as_array.shape
        
        h_coord = 0
        v_coord = 0

        patch_coords = ...