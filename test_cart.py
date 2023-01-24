import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    product_tab_selector = (By.XPATH, "//*[@href='/products']")
    search_product_field_selector = (By.ID, "search_product")
    submit_search_selector = (By.ID, "submit_search")
    single_product_selector = (By.CLASS_NAME, "single-products")
    add_to_cart_button_selector = (By.CSS_SELECTOR, ".overlay-content .add-to-cart")
    continue_shopping_button_selector = (By.CLASS_NAME, "btn-success")
    cart_tab_selector = (By.CLASS_NAME, "fa-shopping-cart")
    checkout_button_selector = (By.CLASS_NAME, "check_out")
    email_btn = (By.XPATH, "//input[@data-qa='login-email']")
    signup_btn = (By.XPATH, "//a[@href='/login']")
    email_credential = "seleniumremote@gmail.com"
    psw_credential = "tester"
    psw_btn = (By.XPATH, "//input[@data-qa='login-password']")
    login_btn = (By.XPATH, "//button[@data-qa='login-button']")
    total_amount_selector = (By.CLASS_NAME, "cart_total_price")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://automationexercise.com/")
        self.driver.find_element(*self.product_tab_selector).click()
        self.driver.refresh()

    def test_total_amount_different_products(self):
        self.driver.find_element(*self.signup_btn).click()
        self.driver.find_element(*self.email_btn).send_keys(self.email_credential)
        self.driver.find_element(*self.psw_btn).send_keys(self.psw_credential)
        self.driver.find_element(*self.login_btn).click()

        self.driver.find_element(*self.product_tab_selector).click()

        search_field = self.driver.find_element(*self.search_product_field_selector)
        search_field.clear()
        search_field.send_keys("men tshirt")

        self.driver.find_element(*self.submit_search_selector).click()
        single_product = self.driver.find_element(*self.single_product_selector)
        ActionChains(self.driver).move_to_element(single_product).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_button_selector)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()

        search_field = self.driver.find_element(*self.search_product_field_selector)
        search_field.clear()
        search_field.send_keys("unicorn")

        self.driver.find_element(*self.submit_search_selector).click()
        single_product = self.driver.find_element(*self.single_product_selector)
        add_to_cart = self.driver.find_element(*self.add_to_cart_button_selector)
        ActionChains(self.driver).move_to_element(single_product).click(add_to_cart).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_button_selector)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()

        self.driver.find_element(*self.cart_tab_selector).click()
        self.driver.find_element(*self.checkout_button_selector).click()

        price_elements = self.driver.find_elements(*self.total_amount_selector)

        total_amount = int(price_elements[-1].text.split()[1])

        items_prices = []
        for element in price_elements[0:-1]:
            items_prices.append(int(element.text.split()[1]))

        self.assertEqual(total_amount, sum(items_prices))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
