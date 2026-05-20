from pages.base_page import BasePage
from locators.attendance_locators import AttendanceLocators

class AddAttendance(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_attendance(self):
        
        # NAVIGATION    
        self.click(AttendanceLocators.ATTENDANCE_NAV_BAR)
        self.click(AttendanceLocators.APPLY_BTN)
        
        # START DATE
        self.click(AttendanceLocators.START_DATE)

        self.click(AttendanceLocators.SELECT_START_DATE)

        self.click(AttendanceLocators.OK_BTN)

        # END DATE
        self.click(AttendanceLocators.END_DATE)

        self.click(AttendanceLocators.SELECT_END_DATE)

        self.click(AttendanceLocators.OK_BTN)

        # CHECK IN TIME
        self.click(AttendanceLocators.START_TIME)
        self.click(AttendanceLocators.CHECK_IN_TIME)
        self.click(AttendanceLocators.CHECK_IN_MINS)
        self.click(AttendanceLocators.OK_BTN)
        
        # CHECK OUT TIME
        self.click(AttendanceLocators.END_TIME)
        self.click(AttendanceLocators.CHECK_OUT_TIME)
        self.click(AttendanceLocators.CHECK_OUT_MINS)
        self.click(AttendanceLocators.OK_BTN)

        # DESCRIPTION
        self.enter_text(
            AttendanceLocators.DESCRIPTION_FIELD,
            "Worked on project tasks and attended meetings."
        )

        # SUBMIT
        self.click(AttendanceLocators.SUBMIT_BTN)