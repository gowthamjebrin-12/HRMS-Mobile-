from pages.login.reset_password import ResetPasswordPage
from utils.config import Config

def test_reset_password(driver):

    reset_password_page = ResetPasswordPage(driver)
    reset_password_page.reset_password(
        Config.CURRENT_PASSWORD, Config.NEW_PASSWORD)

    print("Password reset successful")