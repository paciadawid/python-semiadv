from selenium.webdriver.common.by import By

from pages.base import BasePage


class CartPage(BasePage):
    __cart_tab_selector = (By.CLASS_NAME, "fa-shopping-cart")
    __checkout_button_selector = (By.CLASS_NAME, "check_out")
    __close_checkout_modal_selector = (By.CLASS_NAME, "close-checkout-modal")

    def navigate_to_cart(self):
        self.click(self.__cart_tab_selector)

    def proceed_to_checkout(self):
        self.click(self.__checkout_button_selector)

    def check_if_modal_visible(self):
        self.check_visibility(self.__close_checkout_modal_selector)