from pathlib import Path
from typing import List

SUPPORTED_EXTENSIONS = {'.txt', '.py', '.md', '.csv', '.json', '.html'}


def read_text_file(file_path: Path) -> str:
    """Read a file as UTF-8 text, ignoring undecodable bytes."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()


def get_text_files(directory: str) -> List[Path]:
    """Return all supported text files under a directory, recursively."""
    root = Path(directory)
    if not root.exists():
        raise ValueError(f"Directory does not exist: {root}")
    return [
        p for p in root.rglob('*')
        if p.is_file() and p.suffix in SUPPORTED_EXTENSIONS
    ]
