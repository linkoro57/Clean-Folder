"""Public API for CleanFolder."""
from cleanfolder.config import OrganizerConfig
from cleanfolder.core.organizer import Organizer
from cleanfolder.models.result import OrganizationResult

__all__ = ["Organizer", "OrganizerConfig", "OrganizationResult"]
__version__ = "1.0.0"
