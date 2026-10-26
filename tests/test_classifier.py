import unittest
from pathlib import Path
from cleanfolder.config import OrganizerConfig
from cleanfolder.core.classifier import FileClassifier

class FileClassifierTests(unittest.TestCase):
    def setUp(self):
        self.classifier = FileClassifier(OrganizerConfig())

    def test_known_extension_is_case_insensitive(self):
        self.assertEqual(self.classifier.classify(Path("photo.JPG")), "Images")

    def test_unknown_extension_uses_fallback(self):
        self.assertEqual(self.classifier.classify(Path("data.unknown")), "Other")
