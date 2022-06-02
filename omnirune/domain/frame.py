#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from numpy import array

class Patch: ...

class Frame:
    """Base domain class for image/video frame representation."""
    def __init__(self, image_array: array):
        self._image_array = image_array
    
    @property
    def as_array(self):
        return self._image_array
    
    def get_patch(self, h_coord: int, v_coord: int, height: int, width: int) -> Patch:
        patch_arr = self.as_array[h_coord:h_coord+height, v_coord:v_coord+width, :]
        return patch_arr