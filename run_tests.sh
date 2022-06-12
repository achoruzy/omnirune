#!/bin/bash

echo ">>> Running unit tests."
python -m pytest -v

echo ">>> Running integration tests."
python  tests/_integration/integration_pipeline.py

image_path="/home/industark/Desktop/Side Projects/Omnirune/data/screenshots/001.jpg"
save_path="/home/industark/Desktop/Side Projects/Omnirune/data/generated.jpg"
echo ">>> Running translation tests."
python  omnirune/start.py "$image_path" "$save_path"