from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):
    __email_btn = (By.XPATH, "//input[@data-qa='login-email']")
    __signup_btn = (By.XPATH, "//a[@href='/login']")
    __psw_btn = (By.XPATH, "//input[@data-qa='login-password']")
    __login_btn = (By.XPATH, "//button[@data-qa='login-button']")

    def login_using_email_password(self, email, password):
        self.driver.find_element(*self.__signup_btn).click()
        self.driver.find_element(*self.__email_btn).send_keys(email)
        self.driver.find_element(*self.__psw_btn).send_keys(password)
        self.driver.find_element(*self.__login_btn).click()
