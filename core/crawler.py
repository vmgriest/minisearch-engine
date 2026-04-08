from pathlib import Path
from typing import Dict
class DirectoryCrawler:
    """Crawls directories and extracts from files."""
    Supported_Extensions = {'.txt', '.py', '.md','.csv','.json', '.html'}
    def __init__(self, root_directory: str):
        self.root_directory=Path(root_directory)
        self.documents: Dict[str, str]={}
    def crawl(self)->Dict[str, str]:
        """Crawl directory and read all supported text files"""
        if not self.root_directory.exists():
            raise ValueError(f"Directory {self.root_directory}does not exist")
        for file_path in self.root_directory.rglob('*'):
            if file_path.is_file() and file_path.suffix in self.Supported_Extensions:
                try:
                    content = self._read_file(file_path)
                    self.documents[str(file_path)]=content
                    print(f"Crawled {file_path}")
                except:
                    print(f"Error reading {file_path}")
        print(f"\nTotal documents crawled: {len(self.documents)}")
        return self.documents
    def _read_file(self, file_path: Path):
        """Read file content with UTF-8 encoding"""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
        
    def build_index_with_pos(self, tokenizer, inverted_index):
        """Build Index withe position tracking for phrase search."""
        for file_path, content in self.documents.items():
            #tokenize with position
            tokens=tokenizer.tokenize_with_position(content)
            
            #add each token with its position
            for position, token in enumerate(tokens):
                inverted_index.add_term_with_position(token, str(file_path), position)
            
            #store document metadata
            inverted_index.add_document_metadata(str(file_path),str(file_path), len(tokens))
