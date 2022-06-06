#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from numpy import array


class Frame:
    """Base domain class for image/video frame representation."""
    def __init__(self, image_array: array):
        self._image_array = image_array
        self._recognitions = []
    
    @property
    def shape(self):
        return self._image_array.shape
    
    @property
    def height(self):
        return self.shape[0]

    @property
    def width(self):
        return self.shape[1]
    
    @property
    def channels(self):
        if len(self.shape) == 3:
            return self.shape[2]
        return 1
    
    @property
    def as_array(self):
        return self._image_array
    
    @property
    def recognitions(self):
        return self._recognitions
    
    def extract_region(self, h_coord: int, v_coord: int, height: int, width: int) -> array:
        """Patch creation from the frame with given parameters of right upper corner and size."""
        if h_coord < 0 or v_coord < 0 or \
        h_coord + height > self.height or \
        v_coord + width > self.width:
            raise ValueError('Given params cause patch to be outside the frame.')

        patch_arr = self.as_array[h_coord:h_coord+height, v_coord:v_coord+width, :]
        return patch_arr

    def add_recognition(self, recognition):
        self.recognitions.append(recognition)