from pathlib import Path

def available_path(destination: Path, reserved: set[Path] | None = None) -> Path:
    reserved = reserved or set()
    if not destination.exists() and destination not in reserved:
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(f"{destination.stem} ({counter}){destination.suffix}")
        if not candidate.exists() and candidate not in reserved:
            return candidate
        counter += 1
