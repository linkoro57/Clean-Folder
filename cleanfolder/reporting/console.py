from cleanfolder.models.result import OrganizationResult

class ConsoleReporter:
    def display(self, result: OrganizationResult) -> None:
        action = "Would move" if result.preview else "Moved"
        for move in result.moves:
            print(f"{action}: {move.source.name} -> {move.destination.relative_to(result.folder)}")
        verb = "planned" if result.preview else "completed"
        print(f"\nOrganization {verb}: {result.moved} file(s).")
