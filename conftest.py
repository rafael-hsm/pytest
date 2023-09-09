import json

from pytest import fixture

from selenium import webdriver


# @fixture(scope='function')
# def edge_browser():
#     browser = webdriver.Edge()
#     yield browser
    
#     # Teardown
#     print("Iam tearing down this browser")


@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


data_path = 'test_data.json'


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data
