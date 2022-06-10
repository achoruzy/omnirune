#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from typing import List

from omnirune.domain.frame import Frame


class Detector:
    """Ordinary heuristic detector for generating non-inteligent windows from Frame object."""
    def __init__(self, window_size: int):
        self.window_size = window_size

    def detect(self, frame: Frame) -> List[List[int]]:
        step = self.window_size // 2
        height, width, canal = frame.as_array.shape

        h_steps = [i*step for i in range((height // step) - 1)]
        h_last = height-self.window_size
        if h_last not in h_steps: h_steps.append(h_last)

        v_steps = [i*step for i in range((width // step) - 1)]
        v_last = width-self.window_size
        if v_last not in v_steps: v_steps.append(v_last)

        windows = []
        for h in h_steps:
            for v in v_steps:
                windows.append([h, v, self.window_size, self.window_size])

        return windows