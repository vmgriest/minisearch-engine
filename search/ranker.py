import math
from collections import defaultdict
from typing import Dict, List, Set


class Ranker:
    """Scores documents using TF-IDF given a set of matching doc IDs."""

    def rank(
        self,
        doc_ids: Set[str],
        query_tokens: List[str],
        inverted_index: Dict,
        doc_lengths: Dict[str, int],
    ) -> List[tuple]:
        """
        Return (doc_id, score) pairs sorted by score descending.
        Falls back to score=1.0 for any doc not covered by TF-IDF.
        """
        if not doc_ids or not query_tokens:
            return [(doc_id, 1.0) for doc_id in doc_ids]

        total_docs = len(doc_lengths)
        scores = defaultdict(float)

        for term in query_tokens:
            if term not in inverted_index:
                continue
            postings = inverted_index[term]
            doc_freq = len(postings)
            idf = math.log((total_docs + 1) / (doc_freq + 1)) + 1

            for doc_id in doc_ids:
                if doc_id not in postings:
                    continue
                raw_freq = postings[doc_id]
                freq = raw_freq if isinstance(raw_freq, (int, float)) else len(raw_freq)
                length = doc_lengths.get(doc_id, 1) or 1
                tf = freq / length
                scores[doc_id] += tf * idf

        # docs with no TF-IDF signal get a baseline score
        for doc_id in doc_ids:
            if doc_id not in scores:
                scores[doc_id] = 1.0

        return sorted(scores.items(), key=lambda x: x[1], reverse=True)
