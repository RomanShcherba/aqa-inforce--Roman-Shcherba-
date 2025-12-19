import pytest
from playwright.async_api import async_playwright



@pytest.fixture
async def page():
    pw = await async_playwright().start()
    browser = await pw.chromium.launch(headless=False)
    context = await browser.new_context(viewport={"width": 1920, "height": 1080})
    page = await context.new_page()
    await page.goto("https://automationintesting.online/")

    try:
        yield page
    finally:
        await context.close()
        await browser.close()
        await pw.stop()

