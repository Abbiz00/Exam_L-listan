import pytest

from src.book_store import BookStore
from src.fav_books import FavoriteBooks


@pytest.fixture
def store():
    return BookStore()


@pytest.fixture
def favorites():
    return FavoriteBooks()


@pytest.fixture
def book():
    return {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "fav": False}


@pytest.fixture
def other_book():
    return {"id": 2, "title": "Refactoring", "author": "Martin Fowler", "fav": False}


@pytest.fixture
def linked_store(favorites):
    return BookStore(favorites)
