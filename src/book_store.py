INITIAL_BOOKS = [
    {"id": 100, "title": "Ormar på ett plan: En Python-berättelse", "author": "Guido van Rossum"},
    {"id": 102, "title": "The Pragmatic Procrastinator", "author": "Dave Thomasson"},
    {"id": 103, "title": "Python för folk som hatar ormar", "author": "Monty Pythonsson"},
    {"id": 104, "title": "Why Your Tests Are Lying to You", "author": "Kent Backdoor"},
    {"id": 105, "title": "Playwright: Click It Till You Make It", "author": "Microslop Browserdóttir"},
    {"id": 107, "title": "Git Blame and Other Ways to Lose Friends", "author": "Linus Torvalds"},
    {"id": 108, "title": "Learn Python in 21 Years", "author": "Sams Teachyourself"},
    {"id": 109, "title": "Agile Is a Feeling", "author": "Jeff Sutherland"},
    {"id": 110, "title": "Playwright: Waiting for Selectors", "author": "Samuel Barclay Beckett"},
    {"id": 111, "title": "Stack Overflow: A Love Story", "author": "Copy Pasta"},
    {"id": 112, "title": "My First Regex (And Last)", "author": "Larry Wallström"},
    {"id": 113, "title": "The Developer Who Knew Nothing", "author": "George R.R. Martin"},
    {"id": 115, "title": "The Bugs are Coming", "author": "George R.R. Martin"},
]


class BookStore:
    def __init__(self, favorites=None):
        # favorites är en FavoriteBooks-lista som uppdateras när en bok favoritmarkeras
        self.favorites = favorites
        self.books = []
        for book in INITIAL_BOOKS:
            new_book = {"id": book["id"], "title": book["title"], "author": book["author"], "fav": False}
            self.books.append(new_book)

    def _make_id(self):
        # Nytt id = högsta id + 1
        highest = 0
        for book in self.books:
            if book["id"] > highest:
                highest = book["id"]
        return highest + 1

    def addBook(self, author, title):
        book = {"id": self._make_id(), "title": title, "author": author, "fav": False}
        self.books.append(book)
        return book

    def toggleFavorite(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                book["fav"] = not book["fav"]
                if self.favorites is not None:
                    if book["fav"]:
                        self.favorites.add(book)
                    else:
                        self.favorites.remove(book)
                return book
        return None
