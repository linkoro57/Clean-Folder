import tempfile
import unittest
from pathlib import Path
from cleanfolder.core.conflicts import available_path

class ConflictTests(unittest.TestCase):
    def test_existing_destination_gets_suffix(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "file.txt"
            destination.touch()
            self.assertEqual(available_path(destination).name, "file (1).txt")

    def test_reserved_destination_gets_suffix(self):
        destination = Path("folder/file.txt")
        self.assertEqual(available_path(destination, {destination}).name, "file (1).txt")
