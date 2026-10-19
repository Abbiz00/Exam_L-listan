class FavoriteBooks:
    def __init__(self):
        self.books = []

    def _index(self, book):
        for i, b in enumerate(self.books):
            if b["id"] == book["id"]:
                return i
        return -1

    def add(self, book):
        if self._index(book) >= 0:
            return False
        self.books.append(book)
        return True

    def remove(self, book):
        i = self._index(book)
        if i < 0:
            return False
        del self.books[i]
        return True
