from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):
    email_btn = (By.XPATH, "//input[@data-qa='login-email']")
    signup_btn = (By.XPATH, "//a[@href='/login']")
    psw_btn = (By.XPATH, "//input[@data-qa='login-password']")
    login_btn = (By.XPATH, "//button[@data-qa='login-button']")

    def login_using_email_password(self, email, password):
        self.driver.find_element(*self.signup_btn).click()
        self.driver.find_element(*self.email_btn).send_keys(email)
        self.driver.find_element(*self.psw_btn).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
