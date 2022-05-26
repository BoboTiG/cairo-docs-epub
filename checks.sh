#!/bin/bash
set -eu

python -m black src
python -m flake8 --ignore E501 src
python -m mypy src
echo "ok"
