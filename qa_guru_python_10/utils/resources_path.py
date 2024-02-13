from pathlib import Path


def path_photo(name):
    return str(Path(__file__).parent.parent.parent.joinpath('resources', name))
