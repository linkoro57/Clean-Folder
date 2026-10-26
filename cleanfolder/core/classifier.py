from pathlib import Path
from cleanfolder.config import OrganizerConfig

class FileClassifier:
    def __init__(self, config: OrganizerConfig) -> None:
        self.config = config

    def classify(self, path: Path) -> str:
        extension = path.suffix.lower()
        return next((name for name, values in self.config.categories.items() if extension in values), self.config.fallback_category)
