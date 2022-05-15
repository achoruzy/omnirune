#!/bin/bash

echo ">>> Running unit tests."
python -m pytest -v

echo ">>> Running integration tests."
python -m  pytest tests/_integration/integration_pipeline.py