from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://automationexercise.com/")

driver.find_element(By.CSS_SELECTOR, ".logo img")
driver.find_element(By.XPATH, "//li/a[@href='/view_cart']")
driver.find_element(By.ID, "susbscribe_email")
driver.find_element(By.CSS_SELECTOR, ".right.control-carousel")
driver.find_element(By.XPATH, "//*[contains(@class, 'right control-carousel')]")
driver.find_element(By.XPATH, "//*[@class='brands_products']/h2")
driver.find_element(By.XPATH, "//footer")
driver.find_element(By.ID, "scrollUp")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "scrollUp")))
