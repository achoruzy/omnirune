#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from omnirune.domain.frame import *

from numpy.random import rand


def test_frame_get_patches_returns_proper_array_shape():
    frame = Frame(rand(512, 512, 3))
    patch = frame.get_patch(10, 100, 50, 50)
    assert patch.shape == (50, 50, 3)