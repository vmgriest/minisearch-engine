from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple
import math
import json
import sqlite3
from pathlib import Path

class InvertedIndex:
    """In memory inverted index for document search"""
    def __init__(self,):
        self.index: Dict[str,Dict[str,int]]=defaultdict(dict)
        self.documents: Dict[str, str] = {}
        self.doc_lengths: Dict[str, int]={}
    
    def add_document(self, doc_id: str, tokens: List[str], original_content: str = None):
        """Add a document to the index"""
        self.documents[doc_id] = tokens
        # Store original content for display
        if not hasattr(self, 'original_content'):
            self.original_content = {}
        if original_content:
            self.original_content[doc_id] = original_content

        #Count term frequencies
        term_freq=Counter(tokens)
        self.doc_lengths[doc_id]= len(tokens)

        #Update inverted Index
        for term, freq in term_freq.items():
            self.index[term][doc_id]= freq

    def search(self, query_tokens: List[str])->List[Tuple[str,float]]:
        """Search for documents containing query terms with TF-IDF ranking"""
        if not query_tokens:
            return []
        
        #Collect documents that contain any query term
        doc_scores = defaultdict(float)
        for term in query_tokens:
            #Calculate TF-IDF for each document containing this term
            if term in self.index:
                for doc_id, term_freq in self.index[term].items():
                    #TF (Term Frequency) -normalized
                    tf = term_freq/self.doc_lengths[doc_id]
                    
                    #IDF (inverse document frequency)
                    doc_freq=len(self.index[term])
                    total_docs=len(self.documents)
                    idf=math.log((total_docs+1)/(doc_freq+1))+1

                    #Score contribution
                    doc_scores[doc_id]+=tf*idf

        #sort by score (descending) and return
        ranked_results= sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)
        return ranked_results            
    
    def get_document_snippet(self, doc_id: str, query_tokens: List[str], snippet_length: int =150)-> str:
        """Generate a snippet around the first occurence of query terms"""
        content = ' '.join(self.documents.get(doc_id, []))
        if not query_tokens:
            return content[:snippet_length]+"..."
        
        #find first occurence of any query term
        content_lower=content.lower()
        best_pos= len(content)

        for token in query_tokens:
            pos= content_lower.find(token.lower())
            if pos != -1 and pos < best_pos:
                best_pos = pos
        if best_pos < len(content):
            start= max(0, best_pos -50)
            end = min(len(content), best_pos+ snippet_length-50)
            snippet=content[start:end]
            
            if start>0:
                snippet="..."+snippet
            if end<len(content):
                snippet = snippet+"..."
            return snippet
        return content[:snippet_length]
    
    def stats(self)->Dict:
        """Return index statistics"""
        return{
            'total_documents':len(self.documents),
            'unique_terms': len(self.index),
            'total_term_occurrences': sum(len(docs) for docs in self.index.values())
        }
    def add_term_with_position(self, term: str, doc_id: str, position:int):
        """Add term occurence at a specific position for phrase serach"""
            # If you already have self.index as dict, use it
            # Otherwise adjust based on your existing structure
        if not hasattr(self,'index'):
           self.index ={}
        if term not in self.index:
            self.index[term]={}
        if doc_id not in self.index[term]:
            self.index[term][doc_id]=[]
        self.index[term][doc_id].append(position)

    def add_document_meta_data(self, doc_id:str, file_path:str, doc_length: int):
        """store doc metadata"""
        if not hasattr(self,'documents'):
            self.documents={}

        self.documents[doc_id] = {
        'file_path': file_path,
        'doc_length': doc_length
        }

    def save_to_json(self, filepath:str='index_data/index.json'):
        """Save index to JSON file for persistence"""
        from pathlib import Path
        
        #Create directory if it doesnt exist
        Path(filepath).parent.mkdir(parents=True,exist_ok=True)

        data={
            'index':getattr(self, 'index',{}),
            'documents':getattr(self,'documets',{})
        }

        with open(filepath, 'w',encoding='utf-8')as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"index saved to {filepath}")
    
    def load_from_json(self, filepath: str='index_data/index.json'):
        """load index from JSON file"""
        from pathlib import Path

        if not Path(filepath).exists():
            print(f"No index file found at {filepath}")
            return False
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data=json.load(f)
        self.index = data.get('index', {})
        self.documents=data.get('documents',{})

        print(f"index loaded from {filepath}")
        print(f"Loaded {len(self.index)} terms and {len(self.documents)} documents")
        return True
    
    def save_to_sqlite(self, dbpath: str='index_data/index.db'):
        """Save index to SQLite database"""
        from pathlib import Path
        import sqlite3
        import json

        #create directory if it doesn't exist
        Path(dbpath).parent.mkdir(parents=True,exist_ok=True)

        conn=sqlite3.connect(dbpath)
        cursor=conn.cursor()

        #Create tables
        cursor.execute('CREATE TABLE IF NOT EXISTS terms(term TEXT PRIMARY KEY, doc_freq INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS postings(term TEXT, doc_id TEXT, positons TEXT)')
        cursor.execute('CREATE TABLE IF NOT EXISTS terms(doc_id TEXT PRIMARY KEY, file_path TEXT, doc_length INTEGER)')
 
        #Clear existing data
        cursor.execute('DELETE from terms ')
        cursor.execute('DELETE from posting ')
        cursor.execute('DELETE from documents ')

        #save index data
        for term, postings in getattr(self, 'index', {}).items():
            cursor.execute('INSERT INTO terms(term, doc_length) VALUES (?,?)',(term, len(postings)))

        for doc_id, positions in postings.items():
            cursor.execute('INSERT INTO postings (term, doc_id,positions) VALUES(?,?,?)',(term, doc_id, json.dumps(positions)))
        
        conn.commit()
        conn.close()
        print(f"Index saved to {dbpath}")

    def load_from_sqlite(self, dbpath:str='index_data/index.db'):
        """Load index from SQLite database"""
        from pathlib import Path
        import sqlite3
        import json
        
        if not Path(dbpath).exists():
            print(f"✗ No index file found at {dbpath}")
            return False
        
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
            
        #initialize index structures
        self.index={}
        self.documents={}

        #load documents
        cursor.execute('SELECT doc_id, file_path, doc_length FROM documents')
        for row in cursor.fetchall():
            self.documents[row[0]]={
                'file_path': row[1],
                'doc_length': row[2]
            }
        
        #load postings
        cursor.execute('SELECT term, doc_id, positions from postings')
        for row in cursor.fetchall():
            term, doc_id, positions_str=row
            positions = json.loads(positions_str)
            if term not in self.index:
                self.index[term]={}
            self.index[term][doc_id]=positions
        
        conn.close()
        print(f"Index loaded from {dbpath}")
        print(f"  Loaded {len(self.index)} terms and {len(self.documents)} documents")
        return True

    def get_term_postings(self, term:str):
        """Get postings for a term(for query evaluation)"""
        return getattr(self, 'index', {}).get(term, {})