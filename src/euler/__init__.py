from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("euler")
except PackageNotFoundError:
    # package is not installed
    pass
