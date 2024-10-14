import pytest
from page_objects.actions.home_page import HomePage


@pytest.fixture
def navpro_page(page):
    return HomePage(page)


def test_todos_os_componentes_devem_ser_exibidos(navpro_page):
    navpro_page.navigate_to_homepage()
    assert navpro_page.home_title_is_visible()
    assert navpro_page.btn_exames_is_visible()
    assert navpro_page.btn_pacientes_is_visible()
    assert navpro_page.btn_faq_is_visible()
    assert navpro_page.btn_entrar_is_visible()


def test_deve_acessar_o_nav_exames_com_sucesso(navpro_page):
    navpro_page.navigate_to_homepage()
    navpro_page.click_exames_link()
    assert navpro_page.page.url == "https://navpro.dasa.com.br/exames"
