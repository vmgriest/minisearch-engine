


# MiniSearch Engine

A lightweight, terminal-based search engine built in Python that demonstrates core information retrieval concepts. Supports phrase searching, term frequency ranking, and color-highlighted results.

## Features

- **Phrase Searching** – Find exact phrases within documents
- **Term Frequency Ranking** – Results ranked by relevance using TF scoring
- **Positional Tracking** – Tracks term positions to enable phrase queries
- **Inverted Index** – Efficient document retrieval using classic IR data structure
- **Color-Highlighted Output** – Terminal display with highlighted search terms
- **Lightweight** – Runs entirely in the command line, no external dependencies

## Technologies Used

- Python 3.x
- Standard library only (no external packages required)

## Installation

```bash
git clone https://github.com/vmgriest/minisearch-engine.git
cd minisearch-engine
```

No additional dependencies needed – just Python 3.

## How to Use

Run the main script:

```bash
python main.py
```

Follow the terminal prompts to:
1. Enter a search query (single word or phrase in quotes)
2. View ranked results with relevance scores
3. See matching terms highlighted in color

### Example Queries

- Single term: `python`
- Phrase search: `"machine learning"`
- Multiple terms: `search engine ranking`

## File Structure

```
minisearch-engine/
├── main.py              # Entry point for the application
├── cli/                 # Command-line interface handling
├── core/                # Core search engine logic (inverted index, ranking)
├── models/              # Data models for documents and terms
├── search/              # Search algorithms and query processing
├── utils/               # Helper functions (text processing, highlighting)
├── tests/               # Unit tests
└── .claude/             # Development configuration
```

## Key Concepts Demonstrated

| Concept | Implementation |
|---------|----------------|
| Inverted Index | Maps terms to documents and positions |
| Positional Tracking | Stores term positions within each document |
| Term Frequency (TF) | Scores documents based on term frequency |
| Phrase Query | Uses positional data to find exact phrases |
| Relevance Ranking | Orders results by computed relevance score |

## Future Improvements

- Add TF-IDF scoring (term frequency-inverse document frequency)
- Support for stemming and stopword removal
- Index persistence (save/load index to disk)
- Web interface (Flask-based)
- Support for larger document corpora


You can copy the entire block above and paste it into your `README.md` file. Let me know if you need any changes!
