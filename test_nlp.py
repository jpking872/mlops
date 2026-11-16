import pytest
from mylib.nlp import summarize_wikipedia, get_phrases, search_wiki_pages


def test_summarize_wikipedia():
    assert "San Antonio" in summarize_wikipedia("San Antonio Spurs")


def test_get_phrases():
    phrases = get_phrases("San Antonio Spurs")
    assert "san antonio" in phrases
    assert "spurs" in phrases


def test_search_wiki_pages():
    pages = search_wiki_pages("San Antonio Spurs")
    assert len(pages) > 0
