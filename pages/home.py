from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):
    product_tab_selector = (By.XPATH, "//*[@href='/products']")

    def close_ad(self):
        self.driver.find_element(*self.product_tab_selector).click()
        self.driver.refresh()
