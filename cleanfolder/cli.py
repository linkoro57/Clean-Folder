import argparse
from pathlib import Path
from cleanfolder.config import OrganizerConfig
from cleanfolder.core.organizer import Organizer
from cleanfolder.exceptions import ConfigurationError
from cleanfolder.reporting.console import ConsoleReporter

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cleanfolder", description="Automatically organize files into folders by type.")
    parser.add_argument("folder", nargs="?", type=Path, default=Path.cwd(), help="folder to organize")
    parser.add_argument("--preview", action="store_true", help="show changes without moving files")
    parser.add_argument("--config", type=Path, help="custom JSON category configuration")
    parser.add_argument("--include-hidden", action="store_true", help="include hidden files")
    return parser

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    folder = args.folder.expanduser().resolve()
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid directory.")
        return 1
    try:
        config = OrganizerConfig.from_json(args.config) if args.config else OrganizerConfig()
    except ConfigurationError as error:
        print(f"Configuration error: {error}")
        return 2
    config.include_hidden = args.include_hidden
    ConsoleReporter().display(Organizer(config).run(folder, args.preview))
    return 0
