from pages.base_page import BasePage


class FavoritesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.items = page.get_by_test_id("book-list").locator("li")

    def item(self, title):
        return self.page.get_by_test_id(f"fav-{title}")
