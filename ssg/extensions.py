import importlib
from pathlib import Path
import sys


def load_module(directory: str, name: str):
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)


def load_directory(directory: Path):
    for path in directory.rglob("*.py"):
        load_module(directory.as_posix(), path.stem)
