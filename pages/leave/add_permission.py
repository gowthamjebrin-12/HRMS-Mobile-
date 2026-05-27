from pages.base_page import BasePage
from locators.permission_locators import PermissionLocators

class AddPermission(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def add_permission(self):

        self.click(PermissionLocators.LEAVE_NAV_BAR)

        self.click(PermissionLocators.PERMISSION_NAV_PAGE)

        self.click(PermissionLocators.APPLY_BTN)
        # DATE PICKER
        self.click(PermissionLocators.DATE_PICKER)

        self.click(PermissionLocators.SELECT_PERMISSION_DATE)

        self.click(PermissionLocators.CLICK_OK_BTN)

        # LOCATION DETAILS
        self.enter_text(
            PermissionLocators.STARTING_FROM, "Test Location")
        
        self.enter_text(
            PermissionLocators.DESTINATION, "Test Destination")
        
        # START TIME
        self.click(PermissionLocators.START_TIME_PICKER)
        self.click(PermissionLocators.SELECT_HOUR)
        self.click(PermissionLocators.SELECT_MINS)
        self.click(PermissionLocators.CLICK_OK_BTN)

        # END TIME
        self.click(PermissionLocators.END_TIME_PICKER)
        self.click(PermissionLocators.SELECT_END_HOUR)
        self.click(PermissionLocators.SELECT_END_MINS)
        self.click(PermissionLocators.CLICK_OK_BTN)

        # MARK ATTENDANCE
        self.click(PermissionLocators.MARK_ATTENDANCE)

        # SCROLL DOWN
        self.scroll_down()

        # COMMENT
        self.enter_text(
            PermissionLocators.COMMENT,
            "Permission for personal work"
        )

        # SUBMIT
        self.click(PermissionLocators.SUBMIT_BTN)

        # CONFIRMATION
        self.click(PermissionLocators.CLICK_OK_BTN)

    def is_visible_permission(self):
        return self.is_displayed(PermissionLocators.PERMISSION_PAGE)