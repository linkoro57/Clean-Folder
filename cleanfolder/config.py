"""Configuration loading and validation."""
import json
from dataclasses import dataclass, field
from pathlib import Path
from cleanfolder.constants import DEFAULT_CATEGORIES, DEFAULT_FALLBACK_CATEGORY
from cleanfolder.exceptions import ConfigurationError

@dataclass(slots=True)
class OrganizerConfig:
    categories: dict[str, set[str]] = field(default_factory=lambda: {k: set(v) for k, v in DEFAULT_CATEGORIES.items()})
    fallback_category: str = DEFAULT_FALLBACK_CATEGORY
    include_hidden: bool = False

    @classmethod
    def from_json(cls, path: Path) -> "OrganizerConfig":
        try:
            raw = json.loads(path.expanduser().read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise ConfigurationError(str(error)) from error
        categories = raw.get("categories")
        if not isinstance(categories, dict) or not categories:
            raise ConfigurationError("'categories' must be a non-empty object")
        normalized = {}
        for name, extensions in categories.items():
            if not isinstance(name, str) or not isinstance(extensions, list):
                raise ConfigurationError("category names must map to extension lists")
            normalized[name] = {e.lower() if e.startswith(".") else f".{e.lower()}" for e in extensions if isinstance(e, str) and e}
        fallback = raw.get("fallback_category", DEFAULT_FALLBACK_CATEGORY)
        if not isinstance(fallback, str) or not fallback.strip():
            raise ConfigurationError("'fallback_category' must be a non-empty string")
        return cls(categories=normalized, fallback_category=fallback.strip())
