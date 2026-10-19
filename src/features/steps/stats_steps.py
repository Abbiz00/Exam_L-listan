from behave import then
from playwright.sync_api import expect

from pages.stats_page import StatsPage


@then("ska statistiken visa {antal:d} böcker")
def step_stats_book_count(context, antal):
    expect(StatsPage(context.page).book_count).to_contain_text(str(antal))


@then("statistiken ska visa {antal:d} hjärtmarkerade böcker")
@then("ska statistiken visa {antal:d} hjärtmarkerade böcker")
def step_stats_stars_count(context, antal):
    expect(StatsPage(context.page).stars_count).to_contain_text(str(antal))
