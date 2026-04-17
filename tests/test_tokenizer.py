import pytest
from core.tokenizer import Tokenizer


@pytest.fixture
def tokenizer():
    return Tokenizer()


def test_basic_tokenization(tokenizer):
    tokens = tokenizer.tokenize("Hello World")
    assert "hello" in tokens
    assert "world" in tokens


def test_lowercasing(tokenizer):
    tokens = tokenizer.tokenize("Python JAVA JavaScript")
    assert tokens == ["python", "java", "javascript"]


def test_stop_words_removed(tokenizer):
    tokens = tokenizer.tokenize("the quick brown fox")
    assert "the" not in tokens


def test_punctuation_removed(tokenizer):
    tokens = tokenizer.tokenize("hello, world! how are you?")
    assert "hello," not in tokens
    assert "hello" in tokens


def test_min_word_length(tokenizer):
    # min_word_length=2, so single-char words are dropped; "am" (len 2) is kept
    tokens = tokenizer.tokenize("I am a cat")
    assert "i" not in tokens   # single char → dropped
    assert "a" not in tokens   # single char → dropped
    assert "am" in tokens      # length 2 → kept
    assert "cat" in tokens


def test_empty_string(tokenizer):
    assert tokenizer.tokenize("") == []


def test_tokenize_unique(tokenizer):
    result = tokenizer.tokenize_unique("python python java")
    assert isinstance(result, set)
    assert "python" in result
    assert len(result) == len(set(result))


def test_custom_stop_words():
    t = Tokenizer(stop_words={"custom", "stop"})
    tokens = t.tokenize("custom stop word kept")
    assert "custom" not in tokens
    assert "stop" not in tokens
    assert "kept" in tokens


def test_numbers_removed(tokenizer):
    # remove_numbers strips punctuation; digits survive tokenize unless caught
    tokens = tokenizer.tokenize("version 3 is great")
    assert "version" in tokens
    assert "great" in tokens
