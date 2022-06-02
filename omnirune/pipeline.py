#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from omnirune.domain.frame import Frame
from omnirune.subsystems.detection.ordinary_detector.detection import Detector
from omnirune.subsystems.classification.ordinary_classifier.prediction import Predictor as Classifier


def pipeline(frame: Frame):
    """Function for processing image/video frame with CV detection and classifier for
    detected items. Works with given Frame object."""
    Detector(window_size=120).detect(frame)
    Classifier().predict(frame)