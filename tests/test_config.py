import json
import tempfile
import unittest
from pathlib import Path
from cleanfolder.config import OrganizerConfig
from cleanfolder.exceptions import ConfigurationError

class OrganizerConfigTests(unittest.TestCase):
    def test_normalizes_extensions(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"
            path.write_text(json.dumps({"categories": {"Text": ["TXT"]}}), encoding="utf-8")
            self.assertEqual(OrganizerConfig.from_json(path).categories, {"Text": {".txt"}})

    def test_rejects_missing_categories(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"
            path.write_text("{}", encoding="utf-8")
            with self.assertRaises(ConfigurationError):
                OrganizerConfig.from_json(path)
