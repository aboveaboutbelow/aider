try:
    from aider.__version__ import version as __version__
except Exception:
    __version__ = "0.58.2.dev"

__all__ = ["__version__"]