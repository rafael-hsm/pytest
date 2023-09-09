from pytest import mark

# from selenium import webdriver


@mark.ui
@mark.entertainment
def test_can_navigate_to_entertainment_page(edge_browser):
    edge_browser.get('http://www.petrobras.com.br/pt/')
    assert True
    