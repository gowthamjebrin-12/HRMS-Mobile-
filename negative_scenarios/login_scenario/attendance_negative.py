from pages.base_page import BasePage
from locators.attendance_locators import AttendanceLocators

class AttendanceScenarios(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_apply_attendace(self):
        self.click(AttendanceLocators.ATTENDANCE_NAV_BAR)
        self.click(AttendanceLocators.APPLY_BTN)
# ----------------------------------------------
# NEGATIVE SCENARIOS - Submit attendance without selecting start date
# ----------------------------------------------
    def submit_attendance_without_start_date(self):
        self.click(AttendanceLocators.END_DATE)
        self.click(AttendanceLocators.SELECT_END_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.START_TIME)
        self.click(AttendanceLocators.CHECK_IN_TIME)
        self.click(AttendanceLocators.CHECK_IN_MINS)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_TIME)
        self.click(AttendanceLocators.CHECK_OUT_TIME)
        self.click(AttendanceLocators.CHECK_OUT_MINS)
        self.click(AttendanceLocators.OK_BTN)

        self.enter_text(
            AttendanceLocators.DESCRIPTION_FIELD, 
            "Test Attendance"
        )

    def is_apply_btn_disabled(self):
        element = self.driver.find_element(*AttendanceLocators.SUBMIT_BTN)
        return not element.is_enabled()

# ----------------------------------------------
# NEGATIVE SCENARIO - Submit attendance without selecting end date
# ----------------------------------------------
     
    def submit_attendance_without_end_date(self):
        self.click(AttendanceLocators.START_DATE)
        self.click(AttendanceLocators.SELECT_START_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.START_TIME)
        self.click(AttendanceLocators.CHECK_IN_TIME)
        self.click(AttendanceLocators.CHECK_IN_MINS)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_TIME)
        self.click(AttendanceLocators.CHECK_OUT_TIME)
        self.click(AttendanceLocators.CHECK_OUT_MINS)
        self.click(AttendanceLocators.OK_BTN)

# ----------------------------------------------
# NEGATIVE SCENARIO - Sumbit attendance without selecting start time
# ----------------------------------------------

    def submit_attendance_without_start_time(self):
        self.click(AttendanceLocators.START_DATE)
        self.click(AttendanceLocators.SELECT_START_DATE)
        self.click(AttendanceLocators.OK_BTN)  

        self.click(AttendanceLocators.END_DATE)
        self.click(AttendanceLocators.SELECT_END_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_TIME)
        self.click(AttendanceLocators.CHECK_OUT_TIME)
        self.click(AttendanceLocators.CHECK_OUT_MINS)
        self.click(AttendanceLocators.OK_BTN)
# ----------------------------------------------
#  NEGATIVE SCENARIO - Submit attendance without selecting end time
# ----------------------------------------------

    def submit_attendance_without_end_time(self):
        self.click(AttendanceLocators.START_DATE)
        self.click(AttendanceLocators.SELECT_START_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_DATE)
        self.click(AttendanceLocators.SELECT_END_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.START_TIME)
        self.click(AttendanceLocators.CHECK_IN_TIME)
        self.click(AttendanceLocators.CHECK_IN_MINS)
        self.click(AttendanceLocators.OK_BTN)

# ----------------------------------------------
# NEGATIVE SCENARIO - Applied Attendance Request is Displayed in Attendance History
# ----------------------------------------------

    def applied_attendance_request_is_displayed_in_attendance_history(self):
        self.click(AttendanceLocators.START_DATE)
        self.click(AttendanceLocators.SELECT_START_DATE)
        self.click(AttendanceLocators.OK_BTN)  

        self.click(AttendanceLocators.END_DATE)
        self.click(AttendanceLocators.SELECT_END_DATE)
        self.click(AttendanceLocators.OK_BTN)            

        self.click(AttendanceLocators.START_TIME)
        self.click(AttendanceLocators.CHECK_IN_TIME)
        self.click(AttendanceLocators.CHECK_IN_MINS)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_TIME)
        self.click(AttendanceLocators.CHECK_OUT_TIME)
        self.click(AttendanceLocators.CHECK_OUT_MINS)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.SUBMIT_BTN)
        self.click(AttendanceLocators.OK_BTN)

    def is_attendance_history_displayed(self):
        self.click(AttendanceLocators.ATTENDANCE_HISTORY_PAGE)
        return self.is_displayed(AttendanceLocators.REQUEST_PENDING)

# ----------------------------------------------
#  NEGATIVE SCENARIO - Select End Date earlier than Start Date
# ----------------------------------------------

    def select_end_date_earlier_than_start_date(self):
        self.click(AttendanceLocators.START_DATE)
        self.click(AttendanceLocators.SELECT_START_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_DATE)
        self.click(AttendanceLocators.SELECT_END_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.START_DATE)
        self.click(AttendanceLocators.END_DATE_EARLIER_THAN_START_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.START_TIME)
        self.click(AttendanceLocators.CHECK_IN_TIME)
        self.click(AttendanceLocators.CHECK_IN_MINS)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_TIME)
        self.click(AttendanceLocators.CHECK_OUT_TIME)
        self.click(AttendanceLocators.CHECK_OUT_MINS)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.SUBMIT_BTN)

    def is_invalid_date_range(self):
        return self.is_displayed(AttendanceLocators.ALERT_MESSAGE)
    
# ----------------------------------------------
#  NEGATIVE SCENARIO - Select End Time Earlier Than Start Time On The Same Day
# ----------------------------------------------

    def select_end_time_earlier_than_start_time(self):
        self.click(AttendanceLocators.START_DATE)
        self.click(AttendanceLocators.SELECT_START_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_DATE)
        self.click(AttendanceLocators.SELECT_END_DATE)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_TIME__EARLIER_THAN_START_TIME)
        self.click(AttendanceLocators.CHECK_IN_EARLY_TIME)
        self.click(AttendanceLocators.CHECK_IN_EARLY_MINS)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.END_TIME)
        self.click(AttendanceLocators.CHECK_OUT_EARLY_TIME)
        self.click(AttendanceLocators.CHECK_OUT_EARLY_MINS)
        self.click(AttendanceLocators.OK_BTN)

        self.click(AttendanceLocators.SUBMIT_BTN)

    def is_invalid_time_range(self):
        return self.is_displayed(AttendanceLocators.ALERT_MESSAGE)