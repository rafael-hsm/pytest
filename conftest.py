from pytest import fixture

from selenium import webdriver


@fixture(scope='function')
def edge_browser():
    browser = webdriver.Edge()
    yield browser
    
    # Teardown
    print("Iam tearing down this browser")
