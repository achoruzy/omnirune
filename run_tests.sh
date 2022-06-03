#!/bin/bash

echo ">>> Running unit tests."
python -m pytest -v

echo ">>> Running integration tests."
python  tests/_integration/integration_pipeline.py