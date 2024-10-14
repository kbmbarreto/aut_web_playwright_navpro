import pytest
from page_objects.actions.pages import NavProPage


@pytest.fixture
def navpro_page(page):
    return NavProPage(page)


def test_title_is_visible(navpro_page):
    navpro_page.navigate_to_homepage("https://navpro.dasa.com.br")
    assert navpro_page.is_title_visible()


def test_navigation_to_exames(navpro_page):
    navpro_page.navigate_to_homepage("https://navpro.dasa.com.br")
    navpro_page.click_exames_link()
    assert navpro_page.page.url == "https://navpro.dasa.com.br/exames"
