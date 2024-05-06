try:
    from ._version import version as __version__
except ImportError:  # pragma: no cover
    __version__ = "not-installed"

__all__ = [
    "__version__",
]

from .core import BaseAnnotationExperiment
