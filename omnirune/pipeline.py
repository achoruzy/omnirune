#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from omnirune.domain.frame import Frame
from omnirune.subsystems.simple_classifier.predict import Predictor


def pipeline(input_data: Frame):
    result = Predictor().predict(input_data)