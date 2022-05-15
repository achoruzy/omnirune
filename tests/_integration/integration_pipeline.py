#   Copyright (C) 2022 DataVerft Arkadiusz Choruży


from omnirune.pipeline import *


def test_pipeline_always_returns_none():
    fake_input = 'dada'

    assert pipeline(fake_input) == None