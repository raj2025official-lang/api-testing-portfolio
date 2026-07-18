from utils.logger import get_logger
import pandas as pd
import pytest

from pages.login_page import LoginPage

logger = get_logger()

data = pd.read_csv("data/login_data.csv").values.tolist()


@pytest.mark.smoke
@pytest.mark.parametrize("username,password", data)
def test_valid_login(driver, username, password):

    logger.info(f"Testing login with {username}")

    login = LoginPage(driver)
    login.open()
    login.login(username, password)
    print("URL:", driver.current_url)
    print("Title:", driver.title)
    print("Flash:", login.get_error_message())

    if username == "tomsmith" and password == "SuperSecretPassword!":
        assert "/secure" in driver.current_url

    else:
        assert "Your username is invalid!" in login.get_error_message()