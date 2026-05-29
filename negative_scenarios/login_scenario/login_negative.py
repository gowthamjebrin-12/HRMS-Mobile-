from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginScenarios(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        
# Negative Scenario 1: Invalid Email Format
    def execute(self):
            self.enter_text(LoginLocators.USERNAME, "invalid_email")
            self.click(LoginLocators.CONTINUE_BTN)
            if self.is_displayed(LoginLocators.INVALID_USER_MAIL):
                print("Test case executed: Invalid email format error message is displayed")
                return True
            else:
                print("Testcase Failed")
                return False
            
    def is_invalid_email_displayed(self):
        return self.is_displayed(LoginLocators.INVALID_USER_MAIL)

# Negative Scenario 2: Empty Email Credential    
    def execute_without_usermail(self):
        self.enter_text(LoginLocators.USERNAME, "")
        self.click(LoginLocators.CONTINUE_BTN)
        if self.is_displayed(LoginLocators.EMPTY_USER_MAIL):
            print("Test case executed: Empty email error message is displayed")
            return True
        else:
            print("Testcase Failed")
            return False
        
    def is_empty_email_displayed(self):
        return self.is_displayed(LoginLocators.EMPTY_USER_MAIL)

# Valid Email
    def execute_with_valid_usermail(self, username):
        self.enter_text(LoginLocators.USERNAME, username)
        self.click(LoginLocators.CONTINUE_BTN)

# Negative Scenario 3: Invalid Password Format  
    def execute_with_invalid_password(self):
        self.enter_text(LoginLocators.PASSWORD, "invalid_password")
        self.click(LoginLocators.SIGN_IN_BTN)
        if self.is_displayed(LoginLocators.INVALID_PASSWORD):
            print("Test case executed: Invalid password error message is displayed")
            return True
        else:
            print("Testcase Failed")
            return False
        
    def is_invalid_password_displayed(self):
        return self.is_displayed(LoginLocators.INVALID_PASSWORD)

# Negative Scenario 4: Empty Password Credential
    def execute_without_password(self):
        self.enter_text(LoginLocators.PASSWORD,"")
        self.click(LoginLocators.SIGN_IN_BTN)
        if self.is_displayed(LoginLocators.EMPTY_PASSWORD):
            print("Test case executed: Empty password error message is displayed")
            return True
        else:
            print("Testcase Failed")
            return False
        
    def is_empty_password_displayed(self):
        return self.is_displayed(LoginLocators.EMPTY_PASSWORD)