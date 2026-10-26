import shutil
from cleanfolder.exceptions import MoveError
from cleanfolder.models.move import FileMove

class MoveExecutor:
    def execute(self, move: FileMove) -> None:
        try:
            move.destination.parent.mkdir(exist_ok=True)
            shutil.move(str(move.source), str(move.destination))
        except OSError as error:
            raise MoveError(f"Could not move '{move.source.name}': {error}") from error
