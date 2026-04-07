from typing import List, Tuple
from core import DirectoryCrawler, Tokenizer, InvertedIndex
from typing import List, Tuple

class SearchEngine:
    """Complete search engine integrating all components"""
    
    def __init__(self, stop_words: set = None):
        self.tokenizer = Tokenizer(stop_words=stop_words)
        self.index = InvertedIndex()
        self.crawler = None

    def index_directory(self, directory_path: str):
        """Crawl and index all documents in a directory"""
        print(f"Indexing Directory: {directory_path}")
        print("-" * 50)

        self.crawler = DirectoryCrawler(directory_path)
        documents = self.crawler.crawl()

        print("\nBuilding inverted index...")
        for doc_id, content in documents.items():
            tokens = self.tokenizer.tokenize(content)
            self.index.add_document(doc_id, tokens)

        print("\n" + "-" * 50)
        stats = self.index.stats()
        print(f"Index Statistics:")
        print(f"  - Documents: {stats['total_documents']}")
        print(f"  - Unique Terms: {stats['unique_terms']}")
        print(f"  - Total term occurrences: {stats['total_term_occurrences']}")
        print("=" * 50 + "\n")

    def search(self, query: str, top_k: int = 10) -> List[Tuple[str, float, str]]:
        """Search for documents matching the query"""
        query_tokens = self.tokenizer.tokenize(query)

        if not query_tokens:
            print("No valid search terms found (stop words removed)")
            return []

        print(f"Searching for: '{query}'")
        print(f"Query tokens: {query_tokens}")
        print("-" * 50)

        results = self.index.search(query_tokens)

        formatted_results = []
        for doc_id, score in results[:top_k]:
            snippet = self.index.get_document_snippet(doc_id, query_tokens)
            formatted_results.append((doc_id, score, snippet))
        
        return formatted_results

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