import time
from pytest import mark

# from selenium.webdriver.common.by import By

@mark.body
class BodyTests:
    @mark.ui
    def test_can_navigate_to_body_page(self, edge_browser):
        # browser = webdriver.Edge()
        edge_browser.get('http://www.motortrend.com/')
        # element = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/button')
        # element.send_keys('mustang')
        # element.submit()

        time.sleep(2)
        edge_browser.quit()
        assert True

    def test_bumper(self):
        assert True
        
    def test_windshield(self):
        assert True
        
