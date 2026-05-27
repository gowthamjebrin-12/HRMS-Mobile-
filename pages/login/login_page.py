from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    
    def login(self, username, password):

        self.enter_text(LoginLocators.USERNAME, username)

        self.click(LoginLocators.CONTINUE_BTN)

        self.enter_text(LoginLocators.PASSWORD, password)

        self.click(LoginLocators.SIGN_IN_BTN)
    
    def is_login_successful(self):
        return self.is_displayed(LoginLocators.HOME_PAGE)