from importlib.metadata import version

__version__ = version("blueapi")
del version

__all__ = ["__version__"]
