import pytest


@pytest.mark.integration
def test_toggle_adds_book_to_favorites(linked_store, favorites):
    linked_store.toggleFavorite(100)

    assert len(favorites.books) == 1
    assert favorites.books[0]["id"] == 100


@pytest.mark.integration
def test_toggle_twice_removes_book_from_favorites(linked_store, favorites):
    linked_store.toggleFavorite(100)
    linked_store.toggleFavorite(100)

    assert favorites.books == []


@pytest.mark.integration
def test_new_book_can_become_favorite(linked_store, favorites):
    book = linked_store.addBook("Robert C. Martin", "Clean Code")
    linked_store.toggleFavorite(book["id"])

    assert favorites.books == [book]
    assert favorites.books[0]["fav"] is True


@pytest.mark.integration
def test_favorites_match_fav_flags(linked_store, favorites):
    linked_store.toggleFavorite(100)
    linked_store.toggleFavorite(104)
    linked_store.toggleFavorite(110)
    linked_store.toggleFavorite(104)

    favorite_ids = [book["id"] for book in favorites.books]
    assert favorite_ids == [100, 110]
    for book in linked_store.books:
        assert book["fav"] == (book["id"] in favorite_ids)


@pytest.mark.integration
def test_unknown_id_leaves_favorites_unchanged(linked_store, favorites):
    linked_store.toggleFavorite(100)
    linked_store.toggleFavorite(999)

    assert len(favorites.books) == 1
