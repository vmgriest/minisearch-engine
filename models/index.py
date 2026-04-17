from dataclasses import dataclass


@dataclass
class SearchResult:
    """A single ranked result returned by the search engine."""
    doc_id: str
    score: float
    snippet: str = ""

    def __iter__(self):
        """Allow tuple unpacking: doc_id, score, snippet = result"""
        yield self.doc_id
        yield self.score
        yield self.snippet
