from typing import List, Tuple, Dict
from core import DirectoryCrawler, Tokenizer, InvertedIndex
from .query_processor import QueryProcessor
from .ranker import Ranker

class SearchEngine:
    """Complete search engine integrating all components"""

    def __init__(self, stop_words: set = None):
        self.tokenizer = Tokenizer(stop_words=stop_words)
        self.index = InvertedIndex()
        self.crawler = None
        self.query_processor = QueryProcessor()
        self.query_processor.tokenizer = self.tokenizer
        self.ranker = Ranker()

    def index_directory(self, directory_path: str):
        """Crawl and index all documents in a directory"""
        print(f"Indexing Directory: {directory_path}")
        print("-" * 50)

        self.crawler = DirectoryCrawler(directory_path)
        documents = self.crawler.crawl()

        print("\nBuilding inverted index...")
        for doc_id, content in documents.items():
            tokens = self.tokenizer.tokenize(content)
            self.index.add_document(doc_id, tokens, original_content=content)

        print("\n" + "-" * 50)
        stats = self.index.stats()
        print(f"Index Statistics:")
        print(f"  - Documents: {stats['total_documents']}")
        print(f"  - Unique Terms: {stats['unique_terms']}")
        print(f"  - Total term occurrences: {stats['total_term_occurrences']}")
        print("=" * 50 + "\n")

    def search(self, query: str, use_ranking: bool = True) -> List[Dict]:
        """
        Main search method supporting AND/OR and phrases.
        """
        # Parse the query
        parsed_query = self.query_processor.parse_query(query)
        print(f"  [Debug] Parsed query: {parsed_query}")

        # Get document IDs from index
        if parsed_query is None:
            print("  [Debug] Query parsing returned None")
            return []

        doc_ids = self.query_processor.evaluate_query(
            parsed_query,
            self.index.index  # Access the index dictionary
        )
        print(f"  [Debug] Found {len(doc_ids)} documents: {list(doc_ids)[:5]}{'...' if len(doc_ids) > 5 else ''}")

        # Rank matching documents
        query_tokens = self.tokenizer.tokenize(query)
        ranked = self.ranker.rank(doc_ids, query_tokens, self.index.index, self.index.doc_lengths)

        # Build results list
        results = []
        for doc_id, score in ranked:
            snippet = ""
            if hasattr(self.index, 'original_content') and doc_id in self.index.original_content:
                content = self.index.original_content[doc_id]
                snippet = content[:150].replace('\n', ' ') + "..." if len(content) > 150 else content
            else:
                snippet = f"Document: {doc_id}"
            results.append((doc_id, score, snippet))

        return results
    
    def display_results(self, results: List[Tuple[str, float, str]]):
        """Display search results in a readable format"""
        if not results:
            print("No results found.")
            return

        print(f"\nFound {len(results)} results:\n")
        for i, (doc_id, score, snippet) in enumerate(results, 1):
            print(f"{i}. {doc_id}")
            print(f"   Score: {score:.4f}")
            print(f"   Snippet: {snippet}")
            print()

    def get_suggestions(self, partial_term: str, limit: int = 5) -> List[str]:
        """Get term suggestions for auto-complete"""
        suggestions = []
        partial_lower = partial_term.lower()

        for term in getattr(self.index, 'index', {}).keys():
            if term.lower().startswith(partial_lower):
                suggestions.append(term)
                if len(suggestions) >= limit:
                    break

        return suggestions