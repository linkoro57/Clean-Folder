from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True, slots=True)
class FileMove:
    source: Path
    destination: Path
    category: str
