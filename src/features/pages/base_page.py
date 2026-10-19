# Text på menyknapparna -> test-id
NAV_BUTTONS = {
    "Katalog": "catalog",
    "Lägg till bok": "add-book",
    "Mina böcker": "favorites",
    "Statistik": "statistics",
}

# Varje vy känns igen på sin container
VIEWS = {
    "Katalog": ".catalog",
    "Lägg till bok": ".form",
    "Mina böcker": ".favorites",
    "Statistik": ".stats",
}


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def nav_button(self, name):
        return self.page.get_by_test_id(NAV_BUTTONS[name])

    def go_to(self, name):
        # Knappen för vyn som visas är inaktiverad, så klicka bara om vi inte redan är där
        button = self.nav_button(name)
        if button.is_enabled():
            button.click()

    def view(self, name):
        return self.page.locator(VIEWS[name])
