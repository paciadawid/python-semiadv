import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    product_tab_selector = (By.XPATH, "//*[@href='/products']")
    search_product_field_selector = (By.ID, "search_product")
    submit_search_selector = (By.ID, "submit_search")
    single_product_selector = (By.CLASS_NAME, "single-products")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://automationexercise.com/")
        self.driver.find_element(*self.product_tab_selector).click()
        self.driver.refresh()

    def test_search_unicorn(self):
        self.driver.find_element(*self.product_tab_selector).click()
        self.driver.find_element(*self.search_product_field_selector).send_keys("unicorn")
        self.driver.find_element(*self.submit_search_selector).click()
        products = self.driver.find_elements(*self.single_product_selector)
        self.assertGreaterEqual(len(products), 2)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
