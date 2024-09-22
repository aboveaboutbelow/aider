try:
    from aider.__version__ import version as __version__
except ImportError:
    __version__ = "0.57.2.dev"

__all__ = ["__version__"]