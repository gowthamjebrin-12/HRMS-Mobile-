from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators

class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def reset_password(self, current_password, new_password):

        self.click(ResetPasswordLocators.OPEN_MENU)

        self.click(ResetPasswordLocators.RESET_NAV)

        self.enter_text(ResetPasswordLocators.CURRENT_PASSWORD, current_password)

        self.enter_text(ResetPasswordLocators.NEW_PASSWORD, new_password)

        self.enter_text(ResetPasswordLocators.CONFIRM_PASSWORD, new_password)

        self.click(ResetPasswordLocators.UPDATE_BTN)

        self.click(ResetPasswordLocators.OK_BTN)
    
    def is_visible_success_message(self):
        return self.is_displayed(ResetPasswordLocators.HOME_PAGE)


