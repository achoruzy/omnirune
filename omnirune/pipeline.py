#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from omnirune.subsystems.simple_classifier.predict import Predictor


def pipeline(input_data):
    result = Predictor().predict(input_data)