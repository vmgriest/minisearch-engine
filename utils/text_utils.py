from typing import List


def extract_snippet(content: str, query_tokens: List[str], length: int = 150) -> str:
    """Return a snippet of content centred around the first query term hit."""
    if not content:
        return ""
    if not query_tokens:
        return content[:length] + ('...' if len(content) > length else '')

    content_lower = content.lower()
    best_pos = len(content)
    for token in query_tokens:
        pos = content_lower.find(token.lower())
        if pos != -1 and pos < best_pos:
            best_pos = pos

    if best_pos < len(content):
        start = max(0, best_pos - 50)
        end = min(len(content), best_pos + length - 50)
        snippet = content[start:end].replace('\n', ' ')
        if start > 0:
            snippet = '...' + snippet
        if end < len(content):
            snippet = snippet + '...'
        return snippet

    return content[:length].replace('\n', ' ')


def highlight_terms(text: str, terms: List[str], before: str = '**', after: str = '**') -> str:
    """Wrap each occurrence of a query term with marker strings."""
    import re
    for term in terms:
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        text = pattern.sub(lambda m: f"{before}{m.group()}{after}", text)
    return text


def normalize_text(text: str) -> str:
    """Lowercase and collapse whitespace."""
    return ' '.join(text.lower().split())


def truncate(text: str, max_length: int, ellipsis: str = '...') -> str:
    """Truncate text to max_length, appending ellipsis if cut."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(ellipsis)] + ellipsis
