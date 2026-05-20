from pages.base_page import BasePage
from locators.logout_locators import LogoutLocators

class LogoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):

        self.click(LogoutLocators.SIDE_BAR)

        self.click(LogoutLocators.LOGOUT_BTN)

        self.click(LogoutLocators.CONFIRM_LOGOUT)