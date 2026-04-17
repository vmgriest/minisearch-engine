import pytest
from core.crawler import DirectoryCrawler


@pytest.fixture
def sample_dir(tmp_path):
    (tmp_path / "file1.txt").write_text("hello world")
    (tmp_path / "file2.py").write_text("def foo(): pass")
    (tmp_path / "file3.md").write_text("# Heading")
    (tmp_path / "image.png").write_bytes(b"\x89PNG")  # unsupported, should be skipped
    sub = tmp_path / "subdir"
    sub.mkdir()
    (sub / "nested.txt").write_text("nested content")
    return tmp_path


def test_crawl_returns_supported_files(sample_dir):
    crawler = DirectoryCrawler(str(sample_dir))
    docs = crawler.crawl()
    keys = [str(k) for k in docs.keys()]
    assert any("file1.txt" in k for k in keys)
    assert any("file2.py" in k for k in keys)
    assert any("file3.md" in k for k in keys)


def test_crawl_skips_unsupported_extensions(sample_dir):
    crawler = DirectoryCrawler(str(sample_dir))
    docs = crawler.crawl()
    keys = [str(k) for k in docs.keys()]
    assert not any("image.png" in k for k in keys)


def test_crawl_recurses_into_subdirectories(sample_dir):
    crawler = DirectoryCrawler(str(sample_dir))
    docs = crawler.crawl()
    keys = [str(k) for k in docs.keys()]
    assert any("nested.txt" in k for k in keys)


def test_crawl_reads_file_content(sample_dir):
    crawler = DirectoryCrawler(str(sample_dir))
    docs = crawler.crawl()
    contents = list(docs.values())
    assert "hello world" in contents


def test_crawl_invalid_directory():
    crawler = DirectoryCrawler("/nonexistent/path")
    with pytest.raises(ValueError):
        crawler.crawl()


def test_crawl_empty_directory(tmp_path):
    crawler = DirectoryCrawler(str(tmp_path))
    docs = crawler.crawl()
    assert docs == {}


def test_crawl_document_count(sample_dir):
    crawler = DirectoryCrawler(str(sample_dir))
    docs = crawler.crawl()
    assert len(docs) == 4  # file1.txt, file2.py, file3.md, subdir/nested.txt
