from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.helper_functions import load_config


class BasePage:
    driver = None

    def __init__(self):
        self.config = load_config()
        if not self.driver:

            if self.config["browser"] == "chrome":
                BasePage.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            elif self.config["browser"] == "firefox":
                BasePage.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            elif self.config["browser"] == "edge":
                BasePage.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            else:
                raise Exception("Choose between 'chrome', 'edge' and 'firefox'")

            BasePage.driver.get(self.config["baseUrl"])

    def click(self, selector):
        WebDriverWait(self.driver, self.config["timeout"]).until(EC.element_to_be_clickable(selector)).click()

    def hover_over_element(self, selector):
        single_product = self.driver.find_element(*selector)
        ActionChains(self.driver).move_to_element(single_product).perform()

    def send_keys(self, selector, value):
        search_field = self.driver.find_element(*selector)
        search_field.clear()
        search_field.send_keys(value)

    def close_driver(self):
        self.driver.quit()
