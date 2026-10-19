from playwright.sync_api import sync_playwright


# Körs innan alla scenarier
def before_all(context):
    # Starta Playwright och webbläsaren. Sätt headless=False för att se webbläsaren.
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)


# Körs i början av varje scenario
def before_scenario(context, scenario):
    # Ny sida för varje scenario, så att favoriter och böcker inte följer med mellan scenarier
    context.page = context.browser.new_page()
    context.page.set_default_timeout(5_000)
    context.base_url = "https://tap-vt26-testautomatisering.github.io/exam/"


# Körs direkt efter varje scenario
def after_scenario(context, scenario):
    if context.page:
        context.page.close()


# Körs efter alla scenarier
def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()
