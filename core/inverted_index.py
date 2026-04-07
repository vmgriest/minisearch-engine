from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple
import math
class InvertedIndex:
    """In memory inverted index for document search"""
    def __init__(self,):
        self.index: Dict[str,Dict[str,int]]=defaultdict(dict)
        self.documents: Dict[str, str] = {}
        self.doc_lengths: Dict[str, int]={}
    
    def add_document(self, doc_id: str, tokens: List[str]):
        """Add a document to the index"""
        self.documents[doc_id] = tokens

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