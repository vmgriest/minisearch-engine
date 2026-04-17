import pytest
from search.searcher import SearchEngine
from search.query_processor import QueryProcessor
from search.ranker import Ranker
from core.tokenizer import Tokenizer


# ── QueryProcessor ────────────────────────────────────────────────────────────

@pytest.fixture
def qp():
    processor = QueryProcessor()
    processor.tokenizer = Tokenizer()
    return processor


def test_parse_single_term(qp):
    parsed = qp.parse_query("python")
    assert parsed["type"] == "term"
    assert parsed["value"] == "python"


def test_parse_and_query(qp):
    parsed = qp.parse_query("python AND java")
    assert parsed["type"] == "and"
    assert len(parsed["children"]) == 2


def test_parse_or_query(qp):
    parsed = qp.parse_query("python OR java")
    assert parsed["type"] == "or"
    assert len(parsed["children"]) == 2


def test_parse_phrase_query(qp):
    parsed = qp.parse_query('"machine learning"')
    assert parsed["type"] == "phrase"
    assert "machine" in parsed["terms"] or "learning" in parsed["terms"]


def test_implicit_and(qp):
    parsed = qp.parse_query("python java")
    assert parsed["type"] == "and"


def test_evaluate_and(qp):
    index = {
        "python": {"doc1": 1, "doc2": 1},
        "java":   {"doc2": 1, "doc3": 1},
    }
    parsed = qp.parse_query("python AND java")
    result = qp.evaluate_query(parsed, index)
    assert result == {"doc2"}


def test_evaluate_or(qp):
    index = {
        "python": {"doc1": 1},
        "java":   {"doc2": 1},
    }
    parsed = qp.parse_query("python OR java")
    result = qp.evaluate_query(parsed, index)
    assert result == {"doc1", "doc2"}


def test_evaluate_missing_term(qp):
    index = {"python": {"doc1": 1}}
    parsed = qp.parse_query("notaword")
    result = qp.evaluate_query(parsed, index)
    assert result == set()


def test_phrase_search_consecutive_positions(qp):
    index = {
        "machine":  {"doc1": [0, 5]},
        "learning": {"doc1": [1]},
    }
    parsed = qp.parse_query('"machine learning"')
    result = qp.evaluate_query(parsed, index)
    assert "doc1" in result


def test_phrase_search_non_consecutive_excluded(qp):
    index = {
        "machine":  {"doc1": [0]},
        "learning": {"doc1": [5]},
    }
    parsed = qp.parse_query('"machine learning"')
    result = qp.evaluate_query(parsed, index)
    assert "doc1" not in result


# ── Ranker ────────────────────────────────────────────────────────────────────

@pytest.fixture
def ranker():
    return Ranker()


def test_ranker_returns_all_doc_ids(ranker):
    index = {"python": {"doc1": 2, "doc2": 1}}
    lengths = {"doc1": 10, "doc2": 10}
    results = ranker.rank({"doc1", "doc2"}, ["python"], index, lengths)
    ids = [r[0] for r in results]
    assert "doc1" in ids
    assert "doc2" in ids


def test_ranker_sorts_by_score_descending(ranker):
    index = {"python": {"doc1": 5, "doc2": 1}}
    lengths = {"doc1": 10, "doc2": 10}
    results = ranker.rank({"doc1", "doc2"}, ["python"], index, lengths)
    scores = [r[1] for r in results]
    assert scores == sorted(scores, reverse=True)


def test_ranker_empty_doc_ids(ranker):
    assert ranker.rank(set(), ["python"], {}, {}) == []


def test_ranker_no_query_tokens(ranker):
    results = ranker.rank({"doc1"}, [], {}, {"doc1": 5})
    assert results[0][1] == 1.0


def test_ranker_fallback_score(ranker):
    # doc not in any posting gets score 1.0
    results = ranker.rank({"doc1"}, ["missingterm"], {}, {"doc1": 5})
    assert results[0] == ("doc1", 1.0)


# ── SearchEngine integration ──────────────────────────────────────────────────

@pytest.fixture
def engine(tmp_path):
    (tmp_path / "a.txt").write_text("python is great for machine learning")
    (tmp_path / "b.txt").write_text("java and python are both popular languages")
    (tmp_path / "c.txt").write_text("search engines index documents efficiently")
    se = SearchEngine()
    se.index_directory(str(tmp_path))
    return se


def test_engine_indexes_directory(engine):
    stats = engine.index.stats()
    assert stats["total_documents"] == 3


def test_engine_single_term_search(engine):
    results = engine.search("python")
    doc_ids = [r[0] for r in results]
    assert any("a.txt" in d for d in doc_ids)
    assert any("b.txt" in d for d in doc_ids)


def test_engine_and_search(engine):
    results = engine.search("python AND java")
    doc_ids = [r[0] for r in results]
    assert len(doc_ids) == 1
    assert any("b.txt" in d for d in doc_ids)


def test_engine_or_search(engine):
    results = engine.search("python OR java")
    assert len(results) >= 2


def test_engine_no_results(engine):
    results = engine.search("nonexistentterm")
    assert results == []


def test_engine_results_are_tuples(engine):
    results = engine.search("python")
    assert len(results) > 0
    doc_id, score, snippet = results[0]
    assert isinstance(doc_id, str)
    assert isinstance(score, float)
    assert isinstance(snippet, str)


def test_engine_results_sorted_by_score(engine):
    results = engine.search("python")
    scores = [r[1] for r in results]
    assert scores == sorted(scores, reverse=True)
