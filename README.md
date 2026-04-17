# MiniSearch Engine

A lightweight, terminal-based search engine built in Python that demonstrates core information retrieval concepts. Supports boolean queries, phrase search, TF-IDF ranking, and color-highlighted results.

## Features

- **Boolean Queries** – `AND`, `OR`, and grouped expressions `(python OR java) AND testing`
- **Phrase Search** – Exact phrase matching using positional index `"machine learning"`
- **TF-IDF Ranking** – Results scored by term frequency × inverse document frequency
- **Inverted Index** – Efficient document retrieval with position tracking
- **Color Terminal UI** – Colored output, ranked badges, and a query syntax guide
- **Index Persistence** – Save and load the index to JSON or SQLite
- **Stop Word Filtering** – Common words removed during tokenization
- **No External Dependencies** – Standard library only (except `pytest` for tests)

## Technologies Used

- Python 3.11+
- Standard library only (`re`, `math`, `collections`, `pathlib`, `json`, `sqlite3`)
- `pytest` for the test suite

## Installation

```bash
git clone https://github.com/vmgriest/minisearch-engine.git
cd minisearch-engine
```

No dependencies to install to run the app. To run tests:

```bash
pip install pytest
```

## Usage

```bash
python main.py
```

You will be prompted to enter a directory to index, then dropped into an interactive search loop.

### Query Syntax

| Query | Meaning |
|-------|---------|
| `python` | Single term search |
| `python AND java` | Both terms must appear |
| `python OR java` | Either term can appear |
| `"machine learning"` | Exact phrase match |
| `(python OR java) AND testing` | Grouped boolean expression |
| `python java` | Implicit AND (same as `python AND java`) |

### Special Commands

| Command | Action |
|---------|--------|
| `stats` | Show index statistics (documents, terms, occurrences) |
| `help` | Show query syntax guide |
| `clear` | Clear the screen |
| `quit` / `exit` | Exit the program |

## Project Structure

```
minisearch-engine/
├── main.py                  # Entry point and interactive search loop
├── cli/
│   ├── colors.py            # ANSI color codes and print helpers
│   ├── formatter.py         # Banner, help text, and result display
│   └── commands.py          # Command dispatch (stats, help, clear, quit)
├── core/
│   ├── crawler.py           # Recursively reads supported file types
│   ├── tokenizer.py         # Lowercasing, stop words, punctuation removal
│   └── inverted_index.py    # In-memory index with TF-IDF search and persistence
├── models/
│   ├── document.py          # Document dataclass (doc_id, path, content, tokens)
│   ├── term.py              # Posting dataclass (doc_id, frequency, positions)
│   └── index.py             # SearchResult dataclass (doc_id, score, snippet)
├── search/
│   ├── query_processor.py   # Parses and evaluates AND/OR/phrase queries
│   ├── ranker.py            # TF-IDF scorer for a set of matched doc IDs
│   └── searcher.py          # SearchEngine — ties all components together
├── utils/
│   ├── text_utils.py        # Snippet extraction, term highlighting, truncation
│   ├── file_utils.py        # File reading helpers used by the crawler
│   └── logger.py            # Logger wrapper around Colors
└── tests/
    ├── test_tokenizer.py    # Tokenizer unit tests
    ├── test_indexer.py      # InvertedIndex unit tests
    ├── test_crawler.py      # DirectoryCrawler unit tests
    └── test_search.py       # QueryProcessor, Ranker, and SearchEngine tests
```

## Running Tests

```bash
python -m pytest tests/ -v
```

All 49 tests pass covering tokenization, indexing, crawling, query parsing, ranking, and end-to-end search.

## Key Concepts Demonstrated

| Concept | Implementation |
|---------|----------------|
| Inverted Index | `core/inverted_index.py` — maps terms to `{doc_id: frequency}` |
| Positional Tracking | `core/crawler.py` + `add_term_with_position` — enables phrase queries |
| TF-IDF Scoring | `search/ranker.py` — `tf = freq / doc_length`, `idf = log((N+1)/(df+1)) + 1` |
| Boolean Query Parsing | `search/query_processor.py` — recursive descent parser for AND/OR/phrase |
| Phrase Query | Consecutive position check across postings lists |
| Stop Word Removal | `core/tokenizer.py` — configurable stop word set |
| Index Persistence | `InvertedIndex.save_to_json` / `save_to_sqlite` and corresponding loaders |

## Supported File Types

`.txt` `.py` `.md` `.csv` `.json` `.html`
