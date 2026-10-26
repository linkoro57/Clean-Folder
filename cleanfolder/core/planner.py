from pathlib import Path
from cleanfolder.config import OrganizerConfig
from cleanfolder.core.classifier import FileClassifier
from cleanfolder.core.conflicts import available_path
from cleanfolder.models.move import FileMove

class MovePlanner:
    def __init__(self, config: OrganizerConfig) -> None:
        self.config = config
        self.classifier = FileClassifier(config)

    def create_plan(self, folder: Path) -> tuple[list[FileMove], int]:
        moves, reserved, skipped = [], set(), 0
        for source in sorted(folder.iterdir(), key=lambda item: item.name.lower()):
            if not source.is_file() or (source.name.startswith(".") and not self.config.include_hidden):
                skipped += 1
                continue
            category = self.classifier.classify(source)
            destination = available_path(folder / category / source.name, reserved)
            reserved.add(destination)
            moves.append(FileMove(source, destination, category))
        return moves, skipped
