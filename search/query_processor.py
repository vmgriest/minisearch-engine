import re
from typing import List, Set, Dict, Tuple, Optional

class QueryProcessor:
    def parse_query(self, query:str)-> Dict:
        """Parse query with AND/OR operators and phrase search, Call this before evaluate_query()"""
        query= query.strip()

        #Extract quoted phrases
        phrases= self._extract_phrases(query)

        #replace phrases with placeholders
        processed_query = query
        for i, phrase in enumerate(phrases):
            placeholder=f"__Phrase_{i}__"
            processed_query= processed_query.replace(f'"{phrase}"',placeholder)

        # Implicit AND: if no operators but multiple words, add AND between them
        if ' AND ' not in processed_query and ' OR ' not in processed_query and ' ' in processed_query.strip():
            # Check if it's not a single term/phrase
            processed_query = processed_query.replace(' ', ' AND ')

        #parse expresion
        parsed = self._parse_expression(processed_query)

        #replace placeholders with actula phrase tokens
        parsed = self._replace_phrases(parsed, phrases)

        return parsed
    
    def _extract_phrases(self, query:str)->List[str]:
        """Extract quoted phrases from query"""
        return re.findall(r'"([^"]*)"', query)

    def _parse_expression(self, expr: str)-> Dict:
        """Parse logical expressions with AND/OR"""
        expr=expr.strip()

        #handle parentheses
        if '('in expr:
            return self._parse_parentheses(expr)
        
        #OR has lower precedence
        if ' OR ' in expr:
            parts= expr.split(' OR ')
            return{
                'type': 'or',
                'children': [self._parse_expression(p.strip()) for p in parts]
            }
        
        #AND
        if ' AND ' in expr:
            parts= expr.split(' AND ')
            return{
            'type': 'and',
            'children': [self._parse_expression(p.strip()) for p in parts]
            }
        
        #Single term
        return{'type':'term', 'value':expr}
    
    def _parse_parentheses(self, expr: str)-> Dict:
        """Handle parentheses in query"""
        #Find innermost parentheses
        start = expr.rfind('(')
        end = expr.rfind(')', start)

        if start != -1 and end != -1:
            inner = expr[start+1:end]
            parsed_inner= self._parse_expression(inner)

            #replace with placeholder
            placeholder_str = f"__PAREN_{id(parsed_inner)}__"
            new_expr = expr[:start]+ placeholder_str + expr[end+1:]
            outer= self._parse_expression(new_expr)
            outer = self._replace_paren_placeholder(outer, placeholder_str, parsed_inner)
            return outer
        return self._parse_expression(expr)
    
    def _replace_phrases(self, parsed: Dict, phrases: List[str])->Dict:
        """replace phrase placeholders with actual tokens"""
        if parsed is None:
            return None
        if parsed['type'] == 'term' and parsed['value'].startswith("__Phrase_"):
            idx= int(parsed['value'].split('_')[3])
            phrase = phrases[idx]
            tokens = self.tokenizer.tokenize(phrase) # use your existing tokenizer
            return{'type':'phrase', 'terms': tokens}
        elif 'children' in parsed:
            parsed['children']= [self._replace_phrases(child, phrases) for child in parsed['children']]
            return parsed
        return parsed
    
    def _replace_paren_placeholder(self, parsed: Dict, placeholder: str, inner: Dict)->Dict:
        """Replace parentheses placeholder"""
        if parsed is None:
            return None
        if parsed['type']== 'term' and parsed['value'] == placeholder:
            return inner
        elif 'children' in parsed:
            parsed['children'] = [self._replace_paren_placeholder(child, placeholder, inner) for child in parsed['children']]
            return parsed
        return parsed
        
    def evaluate_query(self, parsed_query: Dict, inverted_index: Dict)-> Set[str]:
        """Evaluate parsed query against inveted index call this after parse_query()"""
        if parsed_query['type']=='term':
            term= parsed_query['value']
            return set(inverted_index.get(term, {}).keys())
        elif parsed_query['type']=='phrase':
            terms = parsed_query['terms']
            return self._evaluate_phrase(terms, inverted_index)
        elif parsed_query['type']=='and':
            if not parsed_query['children']:
                return set()
            result = self.evaluate_query(parsed_query['children'][0], inverted_index)
            for child in parsed_query['children'][1:]:
                result &= self.evaluate_query(child, inverted_index)
            return result
        elif parsed_query['type']=='or':
            if not parsed_query['children']:
                return set()
            result = self.evaluate_query(parsed_query['children'][0], inverted_index)
            for child in parsed_query['children'][1:]:
                result |= self.evaluate_query(child, inverted_index)
            return result

        return set()
    def _evaluate_phrase(self, terms: List[str], inverted_index: Dict)->Set[str]:
        """Find docs containing exact phrase"""
        if not terms:
            return set()
        
        #Get docs with first term
        first_term_docs= set(inverted_index.get(terms[0],{}).keys())
        
        result=set()
        for doc_id in first_term_docs:
            if self._contains_phrase(doc_id, terms, inverted_index):
                result.add(doc_id)
        return result
    
    def _contains_phrase(self, doc_id: str, terms: List[str], inverted_index: Dict)-> bool:
        """check if doc contains exact phrase sequence"""
        #get positions for first term
        first_positions= inverted_index.get(terms[0], {}).get(doc_id, [])

        for pos in first_positions:
            # check consecutive positions
            found = True
            for i, term, in enumerate(terms[1:],1):
                term_positions= set(inverted_index.get(term, {}).get(doc_id,[]))
                if pos+i not in term_positions:
                    found=False
                    break
            if found:
                return True
        return False