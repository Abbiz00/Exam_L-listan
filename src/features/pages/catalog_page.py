from pages.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.books = page.locator(".catalog .book")

    def book(self, title):
        return self.books.filter(has_text=title)

    def heart(self, title):
        return self.page.get_by_test_id(f"star-{title}")

    def toggle_favorite(self, title):
        self.heart(title).click()
