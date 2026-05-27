from pages.login.login_page import LoginPage
from utils.config import Config

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(Config.EMP_USERNAME, Config.EMP_PASSWORD)

    print("Login successful")