import pytest
from core.inverted_index import InvertedIndex


@pytest.fixture
def index():
    return InvertedIndex()


@pytest.fixture
def populated_index():
    idx = InvertedIndex()
    idx.add_document("doc1", ["python", "java", "python"], original_content="python java python")
    idx.add_document("doc2", ["java", "search", "engine"], original_content="java search engine")
    idx.add_document("doc3", ["python", "search"], original_content="python search")
    return idx


def test_add_document_stores_tokens(index):
    index.add_document("doc1", ["hello", "world"])
    assert "doc1" in index.documents


def test_term_appears_in_index(index):
    index.add_document("doc1", ["hello", "world"])
    assert "hello" in index.index
    assert "doc1" in index.index["hello"]


def test_term_frequency_counted(index):
    index.add_document("doc1", ["python", "python", "java"])
    assert index.index["python"]["doc1"] == 2
    assert index.index["java"]["doc1"] == 1


def test_doc_length_tracked(index):
    index.add_document("doc1", ["a", "b", "c"])
    assert index.doc_lengths["doc1"] == 3


def test_stats(populated_index):
    stats = populated_index.stats()
    assert stats["total_documents"] == 3
    assert stats["unique_terms"] > 0
    assert stats["total_term_occurrences"] > 0


def test_tfidf_search_returns_results(populated_index):
    results = populated_index.search(["python"])
    doc_ids = [r[0] for r in results]
    assert "doc1" in doc_ids
    assert "doc3" in doc_ids
    assert "doc2" not in doc_ids


def test_tfidf_search_ranks_by_score(populated_index):
    results = populated_index.search(["python"])
    scores = [r[1] for r in results]
    assert scores == sorted(scores, reverse=True)


def test_search_no_results(populated_index):
    results = populated_index.search(["notaword"])
    assert results == []


def test_search_empty_query(populated_index):
    assert populated_index.search([]) == []


def test_original_content_stored(index):
    index.add_document("doc1", ["hello"], original_content="hello world")
    assert index.original_content["doc1"] == "hello world"


def test_multiple_documents_share_term(populated_index):
    assert len(populated_index.index["python"]) == 2  # doc1 and doc3
    assert len(populated_index.index["java"]) == 2    # doc1 and doc2
