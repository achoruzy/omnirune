#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from typing import List
from numpy import array, random

from omnirune.domain.frame import Frame
from omnirune.domain.rune import RUNES


class Predictor:
    def __init__(self):
        ...

    @staticmethod
    def preprocess(frame: Frame, window_params: List[int]) -> array:
        window = frame.extract_region(*window_params)
        return window

    def predict(self, frame: Frame, windows: List[List[int]]):
        for window_params in windows:
            window = self.preprocess(frame, window_params)
            random.seed(sum(window.flatten().tolist()))
            preds = [random.random_sample() for i in range(len(RUNES))]
            self.postprocess(frame, preds, window_params[:2])
    
    @staticmethod
    def postprocess(frame:Frame, preds: array, center: List[int]):
        max_idx = preds.index(max(preds))
        recognition = RUNES[max_idx]
        recognition.update({'center': center})
        return frame.add_recognition(recognition)