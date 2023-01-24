from selenium.webdriver.common.by import By

from pages.base import BasePage


class CartPage(BasePage):
    cart_tab_selector = (By.CLASS_NAME, "fa-shopping-cart")
    checkout_button_selector = (By.CLASS_NAME, "check_out")

    def navigate_to_cart(self):
        self.click(self.cart_tab_selector)

    def proceed_to_checkout(self):
        self.click(self.checkout_button_selector)
