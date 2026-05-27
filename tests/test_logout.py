from pages.login.logout_page import LogoutPage
from pages.login.login_page import LoginPage
from utils.config import Config

def test_logout(driver):

    login_page = LoginPage(driver)
    login_page.login(
        Config.EMP_USERNAME, Config.EMP_PASSWORD
    )
    
    logout_page = LogoutPage(driver)
    logout_page.logout()

    print("Logout successful")