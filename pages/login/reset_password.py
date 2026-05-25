from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators

class ResetPassword(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def reset_password(self, current_password, new_password):

        self.click(ResetPasswordLocators.MENU_SIDEBAR)
        self.click(ResetPasswordLocators.RESET_PASS_SIDEBAR)

        self.enter_text(ResetPasswordLocators.CURRENT_PASSWORD, current_password)
        self.enter_text(ResetPasswordLocators.NEW_PASSWORD, new_password)
        self.enter_text(ResetPasswordLocators.CONFIRM_PASSWORD, new_password)

        self.click(ResetPasswordLocators.UPDATE_BTN)

        confirmation_message = self.get_text(ResetPasswordLocators.CONFIRMATION_MSG)
        return confirmation_message