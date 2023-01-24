from selenium.webdriver.common.by import By

from pages.base import BasePage


class ProductPage(BasePage):
    __product_tab_selector = (By.XPATH, "//*[@href='/products']")
    __search_product_field_selector = (By.ID, "search_product")
    __submit_search_selector = (By.ID, "submit_search")
    __single_product_selector = (By.CLASS_NAME, "single-products")
    __add_to_cart_button_selector = (By.CSS_SELECTOR, ".overlay-content .add-to-cart")
    __continue_shopping_button_selector = (By.CLASS_NAME, "btn-success")
    __view_product_button_selector = (By.CLASS_NAME, "fa-plus-square")

    def search_item(self, item_name):
        self.click(self.__product_tab_selector)
        self.click(self.__submit_search_selector)
        self.send_keys(self.__search_product_field_selector, item_name)
        self.click(self.__submit_search_selector)

    def add_item_to_cart(self, item_name):
        self.search_item(item_name)
        self.hover_over_element(self.__single_product_selector)
        self.click(self.__add_to_cart_button_selector)
        self.click(self.__continue_shopping_button_selector)

    def view_product(self):
        self.click(self.__view_product_button_selector)
