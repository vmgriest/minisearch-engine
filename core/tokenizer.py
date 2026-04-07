import re
from typing import List, Set
from string import punctuation
class Tokenizer:
    """Tokenizes text with basic cleaning and normalization."""
    def __init__(self,
                 lowercase: bool =True,
                 remove_punctuation: bool= True,
                 remove_numbers: bool=True,
                 min_word_length: int=2,
                 stop_words:Set[str]=None
    ):
        self.lowercase= lowercase
        self.remove_punctuation = remove_punctuation
        self.remove_numbers= remove_numbers
        self.min_word_length= min_word_length
        self.stop_words=stop_words or {'a', 'an', 'and', 'are', 'as',
            'at', 'be', 'by', 'for', 'from','has', 'he', 'in', 'is',
            'it', 'its', 'of', 'on', 'that', 'the','to', 'was', 'were',
            'will', 'with', 'i', 'you', 'we', 'they'
        }
    
    def tokenize(self, text:str)->List[str]:
        """Convert text to list of cleaned tokens"""
        if not text:
            return[]
        if self.lowercase:
            text= text.lower()
        if self.remove_numbers:
            text=re.sub(f'[{re.escape(punctuation)}]', ' ', text)
        tokens = text.split()
        filtered_tokens=[]
        for token in tokens:
            if len(token)>=self.min_word_length:
                if token not in self.stop_words:
                    filtered_tokens.append(token)
        return filtered_tokens
    
    def tokenize_unique(self, text: str)->Set[str]:
        """Return unique tokens as a set"""
        return set(self.tokenize(text))