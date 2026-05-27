from pages.base_page import BasePage
from locators.punch_inout_locators import PunchInOutLocators   

class PunchInOut(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def punch_in(self):
        self.click(PunchInOutLocators.PUNCH_IN_BTN)

    def is_visible_punch_in(self):
        return self.is_displayed(PunchInOutLocators.PUNCH_IN_DONE)
    
    def punch_out(self):
        self.click(PunchInOutLocators.PUNCH_OUT_BTN)
    
    def is_visible_punch_out(self):
        return self.is_displayed(PunchInOutLocators.PUNCH_OUT_DONE)
