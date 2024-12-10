#!/bin/bash

isort app.py
black app.py
flake8 app.py
mypy app.py
