from pages.base_page import BasePage


class AddBookPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title_input = page.get_by_test_id("add-input-title")
        self.author_input = page.get_by_test_id("add-input-author")
        self.submit_button = page.get_by_test_id("add-submit")

    def add_book(self, title, author):
        self.title_input.fill(title)
        self.author_input.fill(author)
        self.submit_button.click()
