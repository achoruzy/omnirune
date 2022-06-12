#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from omnirune.domain.frame import *

from numpy.random import rand
import pytest


def test_get_patches_returns_proper_array_shape():
    frame = Frame(rand(512, 512, 3))
    patch = frame.extract_region(10, 100, 50, 50)
    assert patch.shape == (50, 50, 3)


def test_get_patches_raises_value_error_when_bad_params():
    frame = Frame(rand(512, 512, 3))
    with pytest.raises(ValueError):
        frame.extract_region(-1, 100, 50, 50)
    with pytest.raises(ValueError):
        frame.extract_region(100, -1, 50, 50)
    with pytest.raises(ValueError):
        frame.extract_region(10, 100, 60000, 50)
    with pytest.raises(ValueError):
        frame.extract_region(10, 100, 50, 60000)