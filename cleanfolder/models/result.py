from dataclasses import dataclass, field
from pathlib import Path
from cleanfolder.models.move import FileMove

@dataclass(slots=True)
class OrganizationResult:
    folder: Path
    preview: bool
    skipped: int = 0
    moves: list[FileMove] = field(default_factory=list)

    @property
    def moved(self) -> int:
        return len(self.moves)
