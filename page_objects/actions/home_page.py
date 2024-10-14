from playwright.sync_api import Page
from page_objects.elements.home_locators import HomeLocators


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_homepage(self):
        self.page.goto("https://navpro.dasa.com.br")

    def home_title_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.TXT_TITLE}")

    def btn_exames_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.LNK_EXAMES}")

    def btn_pacientes_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.LNK_PACIENTES}")

    def btn_faq_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.LNK_FAQ}")

    def btn_entrar_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.BTN_ENTRAR}")

    def btn_cadastre_se_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.BTN_CADASTRE_SE}")

    def btn_quero_me_cadastrar_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.BTN_QUERO_ME_CADASTRAR}")

    def btn_cookies_entendi_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.BTN_COOKIES_ENTENDI}")

    def btn_cookies_definicoes_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.BTN_DEFINICAO_COOKIES}")

    def btn_cookies_fechar_is_visible(self) -> bool:
        return self.page.is_visible(f"text={HomeLocators.BTN_FECHAR_COOKIES}")

    def click_exames_link(self):
        self.page.click(HomeLocators.LNK_EXAMES)

    def click_pacientes_link(self):
        self.page.click(HomeLocators.LNK_PACIENTES)

    def click_faq_link(self):
        self.page.click(HomeLocators.LNK_FAQ)

    def click_entrar_button(self):
        self.page.click(HomeLocators.BTN_ENTRAR)

    def click_cadastre_se_button(self):
        self.page.click(HomeLocators.BTN_CADASTRE_SE)

    def click_quero_me_cadastrar_button(self):
        self.page.click(HomeLocators.BTN_QUERO_ME_CADASTRAR)

    def click_entendi_button(self):
        self.page.click(HomeLocators.BTN_COOKIES_ENTENDI)

    def click_definicoes_button(self):
        self.page.click(HomeLocators.BTN_DEFINICAO_COOKIES)

    def click_fechar_button(self):
        self.page.click(HomeLocators.BTN_FECHAR_COOKIES)
