import pytest

from src.book_store import BookStore
from src.fav_books import FavoriteBooks


# addBook

@pytest.mark.unit
def test_add_book_adds_book_to_list(store):
    # Arrange
    before = len(store.books)

    # Act
    store.addBook("Robert C. Martin", "Clean Code")

    # Assert
    assert len(store.books) == before + 1


@pytest.mark.unit
def test_add_book_stores_author_and_title(store):
    book = store.addBook("Robert C. Martin", "Clean Code")

    assert book["author"] == "Robert C. Martin"
    assert book["title"] == "Clean Code"
    assert store.books[-1] == book


@pytest.mark.unit
def test_new_book_is_not_favorite(store):
    book = store.addBook("Robert C. Martin", "Clean Code")

    assert book["fav"] is False


@pytest.mark.unit
def test_new_book_gets_highest_id_plus_one(store):
    # Högsta id i startlistan är 115
    book = store.addBook("Robert C. Martin", "Clean Code")

    assert book["id"] == 116


@pytest.mark.unit
def test_two_new_books_get_different_ids(store):
    first = store.addBook("Robert C. Martin", "Clean Code")
    second = store.addBook("Martin Fowler", "Refactoring")

    assert first["id"] != second["id"]


# toggleFavorite

@pytest.mark.unit
def test_books_are_not_favorites_from_start(store):
    for book in store.books:
        assert book["fav"] is False


@pytest.mark.unit
def test_toggle_marks_book_as_favorite(store):
    book = store.toggleFavorite(100)

    assert book["fav"] is True


@pytest.mark.unit
def test_toggle_twice_removes_favorite(store):
    store.toggleFavorite(100)
    book = store.toggleFavorite(100)

    assert book["fav"] is False


@pytest.mark.unit
def test_toggle_three_times_marks_book_again(store):
    store.toggleFavorite(100)
    store.toggleFavorite(100)
    book = store.toggleFavorite(100)

    assert book["fav"] is True


@pytest.mark.unit
def test_toggle_only_changes_chosen_book(store):
    store.toggleFavorite(100)

    for book in store.books:
        if book["id"] != 100:
            assert book["fav"] is False


@pytest.mark.unit
def test_toggle_unknown_id_returns_none(store):
    assert store.toggleFavorite(999) is None


# toggleFavorite med mockad FavoriteBooks

@pytest.mark.unit
def test_toggle_calls_add_on_favorites(mocker):
    # Arrange
    favorites = mocker.Mock(spec=FavoriteBooks)
    store = BookStore(favorites)

    # Act
    book = store.toggleFavorite(100)

    # Assert
    favorites.add.assert_called_with(book)
    assert favorites.add.call_count == 1
    assert not favorites.remove.called


@pytest.mark.unit
def test_toggle_twice_calls_remove_on_favorites(mocker):
    favorites = mocker.Mock(spec=FavoriteBooks)
    store = BookStore(favorites)

    store.toggleFavorite(100)
    book = store.toggleFavorite(100)

    favorites.remove.assert_called_with(book)
    assert favorites.remove.call_count == 1
