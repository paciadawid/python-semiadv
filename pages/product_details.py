from selenium.webdriver.common.by import By

from pages.base import BasePage


class ProductDetailsPage(BasePage):
    __quantity_input_selector = (By.ID, "quantity")
    __add_to_cart_button_selector = (By.CLASS_NAME, "cart")
    __continue_shopping_button_selector = (By.CLASS_NAME, "btn-success")

    def add_to_cart(self, quantity=1):
        self.send_keys(self.__quantity_input_selector, quantity)
        self.click(self.__add_to_cart_button_selector)
        self.click(self.__continue_shopping_button_selector)