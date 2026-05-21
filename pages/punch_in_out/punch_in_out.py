from pages.base_page import BasePage
from locators.punch_inout_locators import PunchInOutLocators   

class PunchInOut(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def punch_in_out(self):

        self.click(PunchInOutLocators.PUNCH_IN_BTN)

        self.scroll_down()

        self.scroll_up()

        self.click(PunchInOutLocators.PUNCH_OUT_BTN)
