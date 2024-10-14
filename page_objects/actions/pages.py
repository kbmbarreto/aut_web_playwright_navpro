from playwright.sync_api import Page
from page_objects.elements.locators import NavProPageLocators


class NavProPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_homepage(self, url: str):
        self.page.goto(url)

    def is_title_visible(self) -> bool:
        return self.page.is_visible(f"text={NavProPageLocators.TITLE_TEXT}")

    def click_exames_link(self):
        self.page.click(NavProPageLocators.EXAMES_LINK)
