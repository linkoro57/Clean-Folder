from pathlib import Path
from cleanfolder.config import OrganizerConfig
from cleanfolder.core.executor import MoveExecutor
from cleanfolder.core.planner import MovePlanner
from cleanfolder.models.result import OrganizationResult

class Organizer:
    def __init__(self, config: OrganizerConfig | None = None) -> None:
        self.config = config or OrganizerConfig()
        self.planner, self.executor = MovePlanner(self.config), MoveExecutor()

    def run(self, folder: Path, preview: bool = False) -> OrganizationResult:
        moves, skipped = self.planner.create_plan(folder)
        result = OrganizationResult(folder, preview, skipped)
        for move in moves:
            if not preview:
                self.executor.execute(move)
            result.moves.append(move)
        return result
