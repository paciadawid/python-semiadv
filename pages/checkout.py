from selenium.webdriver.common.by import By

from pages.base import BasePage


class CheckoutPage(BasePage):
    total_amount_selector = (By.CLASS_NAME, "cart_total_price")

    def get_total_amount(self):
        price_elements = self.driver.find_elements(*self.total_amount_selector)
        total_amount = int(price_elements[-1].text.split()[1])
        return total_amount

    def get_items_prices(self):
        price_elements = self.driver.find_elements(*self.total_amount_selector)
        items_prices = []
        for element in price_elements[0:-1]:
            items_prices.append(int(element.text.split()[1]))
        return items_prices
