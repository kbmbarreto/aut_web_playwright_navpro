import pytest
from page_objects.actions.home_page import HomePage


@pytest.fixture
def navpro_page(page):
    return HomePage(page)


def test_title_is_visible(navpro_page):
    navpro_page.navigate_to_homepage()
    assert navpro_page.home_title_is_visible()


def test_navigation_to_exames(navpro_page):
    navpro_page.navigate_to_homepage()
    navpro_page.click_exames_link()
    assert navpro_page.page.url == "https://navpro.dasa.com.br/exames"
