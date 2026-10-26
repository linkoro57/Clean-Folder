"""Default category definitions."""

DEFAULT_FALLBACK_CATEGORY = "Other"
DEFAULT_CATEGORIES: dict[str, frozenset[str]] = {
    "Images": frozenset(".avif .bmp .gif .heic .jpeg .jpg .png .svg .webp".split()),
    "Documents": frozenset(".csv .doc .docx .epub .md .ods .odt .pdf .ppt .pptx .rtf .txt .xls .xlsx".split()),
    "Archives": frozenset(".7z .bz2 .gz .rar .tar .tgz .xz .zip".split()),
    "Installers": frozenset(".apk .appimage .deb .dmg .exe .msi .pkg .rpm".split()),
    "Audio": frozenset(".aac .flac .m4a .mp3 .ogg .wav .wma".split()),
    "Videos": frozenset(".avi .m4v .mkv .mov .mp4 .webm .wmv".split()),
    "Code": frozenset(".c .cpp .css .go .html .java .js .json .lua .luau .php .py .rs .ts .xml .yaml .yml".split()),
}
