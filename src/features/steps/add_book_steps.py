from behave import when, then
from playwright.sync_api import expect

from pages.add_book_page import AddBookPage


@when('jag fyller i titeln "{titel}"')
def step_fill_title(context, titel):
    AddBookPage(context.page).title_input.fill(titel)


@when('jag fyller i författaren "{forfattare}"')
def step_fill_author(context, forfattare):
    AddBookPage(context.page).author_input.fill(forfattare)


@when('jag klickar på "Lägg till ny bok"')
def step_click_submit(context):
    AddBookPage(context.page).submit_button.click()


@then("ska fältet för titel vara tomt")
def step_title_empty(context):
    expect(AddBookPage(context.page).title_input).to_have_value("")


@then("fältet för författare ska vara tomt")
def step_author_empty(context):
    expect(AddBookPage(context.page).author_input).to_have_value("")


@then('ska knappen "Lägg till ny bok" vara aktiv')
def step_submit_enabled(context):
    expect(AddBookPage(context.page).submit_button).to_be_enabled()


@then('ska knappen "Lägg till ny bok" vara inaktiverad')
def step_submit_disabled(context):
    expect(AddBookPage(context.page).submit_button).to_be_disabled()
