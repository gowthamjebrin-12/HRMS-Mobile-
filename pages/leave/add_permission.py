from pages.base_page import BasePage
from locators.leave_locators import LeaveLocators

class AddPermission(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def add_permission(self):

        self.click(LeaveLocators.LEAVE_NAV_BAR)

        self.click(LeaveLocators.PERMISSION_NAV_PAGE)

        self.click(LeaveLocators.APPLY_BTN)
        # DATE PICKER
        self.click(LeaveLocators.DATE_PICKER)

        self.click(LeaveLocators.SELECT_PERMISSION_DATE)

        self.click(LeaveLocators.CLICK_OK_BTN)

        # LOCATION DETAILS
        self.enter_text(
            LeaveLocators.STARTING_FROM, "Test Location")
        
        self.enter_text(
            LeaveLocators.DESTINATION, "Test Destination")
        
        # START TIME
        self.click(LeaveLocators.START_TIME_PICKER)
        self.click(LeaveLocators.SELECT_HOUR)
        self.click(LeaveLocators.SELECT_MINS)
        self.click(LeaveLocators.CLICK_OK_BTN)

        # END TIME
        self.click(LeaveLocators.END_TIME_PICKER)
        self.click(LeaveLocators.SELECT_END_HOUR)
        self.click(LeaveLocators.SELECT_END_MINS)
        self.click(LeaveLocators.CLICK_OK_BTN)

        # MARK ATTENDANCE
        self.click(LeaveLocators.MARK_ATTENDANCE)

        # COMMENT
        self.enter_text(
            LeaveLocators.COMMENT,
            "Permission for personal work"
        )

        # SUBMIT
        self.click(LeaveLocators.SUBMIT_BTN)

        # SUCCESS MESSAGE
        assert self.is_element_displayed(LeaveLocators.SUCCESS_MSG), "Permission application failed"

        # CONFIRMATION
        self.click(LeaveLocators.CLICK_OK_BTN)