from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate(self, url: str):
        await self.page.goto(url)

    async def click(self, locator: str):
        await self.page.locator(locator).click()

    async def fill(self, locator: str, text: str):
        await self.page.locator(locator).fill(text)

    async def get_text(self, locator: str):
        return await self.page.locator(locator).inner_text()

    async def get_title(self):
        return await self.page.title()

    async def scroll_into_view(self, locator: str):
        await self.page.locator(locator).scroll_into_view_if_needed()

    async def is_disabled(self, locator: str) -> bool:
        return await self.page.locator(locator).is_disabled()