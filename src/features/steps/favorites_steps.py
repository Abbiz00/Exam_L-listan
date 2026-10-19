from behave import then
from playwright.sync_api import expect

from pages.favorites_page import FavoritesPage


@then('ska "{titel}" finnas bland mina favoriter')
def step_in_favorites(context, titel):
    expect(FavoritesPage(context.page).item(titel)).to_be_visible()


@then('ska "{titel}" inte finnas bland mina favoriter')
def step_not_in_favorites(context, titel):
    expect(FavoritesPage(context.page).item(titel)).to_have_count(0)


@then("listan med favoriter ska vara tom")
def step_favorites_empty(context):
    expect(FavoritesPage(context.page).items).to_have_count(0)


@then("ska listan med favoriter innehålla {antal:d} böcker")
def step_favorites_count(context, antal):
    expect(FavoritesPage(context.page).items).to_have_count(antal)
