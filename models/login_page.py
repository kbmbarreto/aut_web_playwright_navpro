from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://navpro.dasa.com.br")


    def login(self, username, password):
        pass