#!/usr/bin/env bash

sudo -E PYTHONPATH=$PYTHONPATH "$(pwd)/venv/bin/python3" "$(pwd)/main.py" "$@"