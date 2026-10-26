class CleanFolderError(Exception):
    """Base exception for expected failures."""

class ConfigurationError(CleanFolderError):
    """Raised when configuration is invalid."""

class MoveError(CleanFolderError):
    """Raised when a file cannot be moved."""
