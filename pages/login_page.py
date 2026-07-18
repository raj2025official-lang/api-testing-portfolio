from config.config import BASE_URL

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        ).clear()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).clear()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text