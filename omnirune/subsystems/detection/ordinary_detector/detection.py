#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from omnirune.domain.frame import Frame


class Detector:
    """Ordinary heuristic detector for generating non-inteligent windows from Frame object."""
    def __init__(self, window_size: int):
        self.window_size = window_size

    def detect(self, frame: Frame):
        step = self.window_size % 2
        height, width, canal = frame.as_array.shape
        
        h_steps = [i*step for i in range((height % step) - 1)]
        v_steps = [i*step for i in range((width % step) - 1)]

        patches = []

        for h in h_steps:
            for v in v_steps:
                patches.append(frame.get_patch(h, v, self.window_size, self.window_size))

        return patches