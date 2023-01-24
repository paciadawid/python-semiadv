from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):
    __product_tab_selector = (By.XPATH, "//*[@href='/products']")

    def close_ad(self):
        self.click(self.__product_tab_selector)
        self.driver.refresh()
