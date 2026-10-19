from behave import when, then
from playwright.sync_api import expect

from pages.catalog_page import CatalogPage


@then("katalogen ska innehålla {antal:d} böcker")
def step_catalog_count(context, antal):
    expect(CatalogPage(context.page).books).to_have_count(antal)


@then('ska boken "{titel}" av "{forfattare}" visas i katalogen')
def step_book_in_catalog(context, titel, forfattare):
    book = CatalogPage(context.page).book(titel)
    expect(book).to_have_count(1)
    expect(book).to_contain_text(forfattare)


@then('boken "{titel}" ska ha ett hjärta')
def step_book_has_heart(context, titel):
    expect(CatalogPage(context.page).heart(titel)).to_be_visible()


@when('jag klickar på hjärtat för "{titel}"')
def step_click_heart(context, titel):
    CatalogPage(context.page).toggle_favorite(titel)


@then('ska hjärtat för "{titel}" vara markerat')
def step_heart_selected(context, titel):
    expect(CatalogPage(context.page).heart(titel)).to_have_class("star selected")


@then('hjärtat för "{titel}" ska inte vara markerat')
def step_heart_not_selected(context, titel):
    expect(CatalogPage(context.page).heart(titel)).to_have_class("star")
