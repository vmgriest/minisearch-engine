from dataclasses import dataclass, field
from typing import List


@dataclass
class Document:
    doc_id: str
    file_path: str
    content: str
    tokens: List[str] = field(default_factory=list)

    @property
    def token_count(self) -> int:
        return len(self.tokens)

    @property
    def preview(self) -> str:
        return self.content[:150].replace('\n', ' ') + ('...' if len(self.content) > 150 else '')
