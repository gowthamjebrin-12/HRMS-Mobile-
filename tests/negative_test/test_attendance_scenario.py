from negative_scenarios.login_scenario.attendance_negative import AttendanceScenarios

# def test_submit_attendance_without_start_date(driver):
    # navigate_attendance = AttendanceScenarios(driver)
    # navigate_attendance.navigate_to_apply_attendace()
    # # scenario1 = AttendanceScenarios(driver)
    # # scenario1.submit_attendance_without_start_date()
    # # scenario2 = AttendanceScenarios(driver)
    # # scenario2.submit_attendance_without_end_date()
    # scenario3 = AttendanceScenarios(driver)
    # scenario3.submit_attendance_without_start_time()
    # assert scenario3.is_apply_btn_disabled(), \
    # "Apply button should be disabled when Start Time is not selected"
    
# def test_is_display_attendance_history(driver):
#     navigate_attendance = AttendanceScenarios(driver)
#     navigate_attendance.navigate_to_apply_attendace()
#     scenario = AttendanceScenarios(driver)
#     scenario.applied_attendance_request_is_displayed_in_attendance__history()
#     assert scenario.is_attendance_history_displayed(), \
#     "Attendance history page should be displayed after applying for attendance"

# def test_select_end_date_earlier_than_start_date(driver):
#     navigate_attendance = AttendanceScenarios(driver)
#     navigate_attendance.navigate_to_apply_attendace()

#     scenario = AttendanceScenarios(driver)
#     scenario.select_end_date_earlier_than_start_date()

#     result = scenario.is_invalid_date_range()
#     assert result, "Invalid date message should be displayed when end date is earlier than start date"


def test_submit_end_time_earlier_than_start_time(driver):
    navigate_attendance = AttendanceScenarios(driver)
    navigate_attendance.navigate_to_apply_attendace()

    scenario = AttendanceScenarios(driver)
    scenario.select_end_time_earlier_than_start_time()

    result = scenario.is_invalid_time_range()
    assert result, "Invalid time message should be displayed when end time is earlier than start time"
