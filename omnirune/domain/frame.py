#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from numpy import array


class Frame:
    """Base domain class for image/video frame representation."""
    def __init__(self, image_array: array):
        self._image_array = image_array
    
    @property
    def as_array(self):
        return self._image_array