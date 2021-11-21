import importlib
from pathlib import Path
import sys


def load_module(directory, name):
    sys.path.insert(0, directory)
