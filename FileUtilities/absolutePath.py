from pathlib import Path


def AbsolutePath(filepath):
    relative = Path(filepath)
    return relative.absolute()
