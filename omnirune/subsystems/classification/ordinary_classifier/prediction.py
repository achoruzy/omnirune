#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from typing import List
from numpy import array, random

from omnirune.domain.frame import Frame
from omnirune.domain.rune import RUNES


class Predictor:
    def __init__(self):
        ...

    def predict(self, frame: Frame, windows: List):
        for window in windows:
            random.seed(sum(window.flatten().tolist()))
            preds = [random.random_sample() for i in range(len(RUNES))]
            self.postprocess(frame, preds)
    
    @staticmethod
    def postprocess(frame:Frame, preds: array):
        max_idx = preds.index(max(preds))
        return frame.add_recognition(RUNES[max_idx])