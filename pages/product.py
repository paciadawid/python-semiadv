from selenium.webdriver.common.by import By

from pages.base import BasePage


class ProductPage(BasePage):
    product_tab_selector = (By.XPATH, "//*[@href='/products']")
    search_product_field_selector = (By.ID, "search_product")
    submit_search_selector = (By.ID, "submit_search")
    single_product_selector = (By.CLASS_NAME, "single-products")
    add_to_cart_button_selector = (By.CSS_SELECTOR, ".overlay-content .add-to-cart")
    continue_shopping_button_selector = (By.CLASS_NAME, "btn-success")

    def search_item(self, item_name):
        self.click(self.submit_search_selector)
        self.send_keys(self.search_product_field_selector, item_name)
        self.click(self.submit_search_selector)

    def add_item_to_cart(self, item_name):
        self.search_item(item_name)
        self.hover_over_element(self.single_product_selector)
        self.click(self.add_to_cart_button_selector)
        self.click(self.continue_shopping_button_selector)
