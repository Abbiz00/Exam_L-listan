import pytest


@pytest.mark.unit
def test_favorites_are_empty_from_start(favorites):
    assert favorites.books == []


@pytest.mark.unit
def test_add_book(favorites, book):
    result = favorites.add(book)

    assert result is True
    assert favorites.books == [book]


@pytest.mark.unit
def test_add_same_book_twice_gives_no_duplicate(favorites, book):
    favorites.add(book)
    result = favorites.add(book)

    assert result is False
    assert len(favorites.books) == 1


@pytest.mark.unit
def test_add_two_different_books(favorites, book, other_book):
    favorites.add(book)
    favorites.add(other_book)

    assert favorites.books == [book, other_book]


# remove

@pytest.mark.unit
def test_remove_book(favorites, book):
    favorites.add(book)
    result = favorites.remove(book)

    assert result is True
    assert favorites.books == []


@pytest.mark.unit
def test_remove_book_that_is_not_in_list(favorites, book):
    result = favorites.remove(book)

    assert result is False
    assert favorites.books == []


@pytest.mark.unit
def test_remove_keeps_other_books(favorites, book, other_book):
    favorites.add(book)
    favorites.add(other_book)
    favorites.remove(book)

    assert favorites.books == [other_book]
