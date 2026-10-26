"""Compatibility launcher for running CleanFolder without installation."""

from cleanfolder.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
