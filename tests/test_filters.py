import random
import unittest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from utils.helper_functions import load_config


class MyTestCase(unittest.TestCase):
    brand_filter_selector = (By.XPATH, "//div[@class='brands-name']//li")
    single_product_selector = (By.CLASS_NAME, "single-products")
    product_tab_selector = (By.XPATH, "//*[@href='/products']")
    category_filter_selector = (By.CSS_SELECTOR, ".category-products span")
    subcategory_filter_selector = (By.XPATH, "//div[@class='panel-collapse in']//li")

    def setUp(self) -> None:
        config = load_config()
        options = ChromeOptions()
        if config["headless"]:
            options.add_argument("--headless")
        if config["browser"] == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        if config["resolution"]:
            self.driver.set_window_size(*config["resolution"].split("x"))

        self.driver.get(config["baseUrl"])
        self.driver.find_element(*self.product_tab_selector).click()
        self.driver.refresh()

    def test_brands(self):
        filters = self.driver.find_elements(*self.brand_filter_selector)
        filter_element = random.choice(filters)
        number_of_items = int(filter_element.text.split()[0][1:-1])
        filter_element.click()
        products = self.driver.find_elements(*self.single_product_selector)
        self.assertEqual(number_of_items, len(products))

    def test_category(self):
        categories = self.driver.find_elements(*self.category_filter_selector)
        category = random.choice(categories)
        category.click()

        subcategories = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.subcategory_filter_selector))
        subcategory = random.choice(subcategories)
        subcategory_name = subcategory.text
        WebDriverWait(self.driver, 10).until(EC.visibility_of(subcategory)).click()

        products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.single_product_selector))
        for product in products:
            self.assertIn(subcategory_name[:-1].lower(), product.text.lower())

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
