import tempfile
import unittest
from pathlib import Path
from cleanfolder.core.organizer import Organizer

class OrganizerTests(unittest.TestCase):
    def test_preview_does_not_modify_files(self):
        with tempfile.TemporaryDirectory() as directory:
            folder, source = Path(directory), Path(directory) / "photo.png"
            source.touch()
            self.assertEqual(Organizer().run(folder, preview=True).moved, 1)
            self.assertTrue(source.exists())

    def test_moves_file_to_category(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / "notes.txt").write_text("hello", encoding="utf-8")
            self.assertEqual(Organizer().run(folder).moved, 1)
            self.assertEqual((folder / "Documents" / "notes.txt").read_text(), "hello")

    def test_ignores_existing_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / "Existing").mkdir()
            result = Organizer().run(folder, preview=True)
            self.assertEqual((result.moved, result.skipped), (0, 1))
