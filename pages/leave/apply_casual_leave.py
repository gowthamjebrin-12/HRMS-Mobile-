from optparse import Option

from pages.base_page import BasePage
from locators.leave_locators import LeaveLocators


class ApplyCasualLeave(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def apply_casual_leave(self):

        self.click(LeaveLocators.LEAVE_PAGE_NAV)

        self.click(LeaveLocators.APPLY_LEAVE_BTN)

        self.click(LeaveLocators.LEAVE_DROPDOWN)

        self.click(Option("Casual Leave"))


        self.click(LeaveLocators.OPTION,format("Casual Leave"))
        
        self.click_dynamic(LeaveLocators.DATE_FIELD, 0)

        self.click(LeaveLocators.START_DATE)

        self.click_dynamic(LeaveLocators.DATE_FIELD, 1)

        self.click(LeaveLocators.END_DATE)

        self.click(LeaveLocators.OK_BTN)

        self.enter_text(LeaveLocators.REASON_INPUT, "Family function")

        self.click(LeaveLocators.SUBMIT_BTN)

        self.click(LeaveLocators.OK_BTN)