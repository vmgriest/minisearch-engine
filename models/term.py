from dataclasses import dataclass, field
from typing import List


@dataclass
class Posting:
    """Represents one term's occurrence record in a single document."""
    doc_id: str
    frequency: int = 0
    positions: List[int] = field(default_factory=list)

    def add_position(self, position: int):
        self.positions.append(position)
        self.frequency += 1
