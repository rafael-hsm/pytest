import time

from pytest import mark

# from selenium import webdriver

@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(edge_browser):
    my_browser = edge_browser
    my_browser.get('https://pcct-dsv.petrobras.com.br/')
    time.sleep(5)
    
    second_browser = edge_browser
    second_browser.get('http://www.amazon.com')
    
    edge_browser.get('https://learn.microsoft.com/pt-br/microsoft-edge/webdriver-chromium/?tabs=python')
    assert True