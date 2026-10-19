from behave import given, when, then
from playwright.sync_api import expect

from pages.add_book_page import AddBookPage
from pages.base_page import BasePage
from pages.catalog_page import CatalogPage


@given("att jag är på startsidan")
def step_open_start_page(context):
    BasePage(context.page).navigate(context.base_url)


@given('jag går till "{vy}"')
@when('jag går till "{vy}"')
def step_go_to(context, vy):
    BasePage(context.page).go_to(vy)


@then('ska vyn "{vy}" visas')
def step_view_visible(context, vy):
    expect(BasePage(context.page).view(vy)).to_be_visible()


@then('knappen "{namn}" ska vara inaktiverad')
def step_nav_button_disabled(context, namn):
    expect(BasePage(context.page).nav_button(namn)).to_be_disabled()


@then('ska texten "{text}" visas')
@then('texten "{text}" ska visas')
def step_text_visible(context, text):
    expect(context.page.get_by_text(text)).to_be_visible()


@given('att jag har markerat "{titel}" som favorit')
def step_given_favorite(context, titel):
    CatalogPage(context.page).toggle_favorite(titel)


@given('att jag har lagt till boken "{titel}" av "{forfattare}"')
def step_given_added_book(context, titel, forfattare):
    page = AddBookPage(context.page)
    page.go_to("Lägg till bok")
    page.add_book(titel, forfattare)
