from behave import given, when, then
from pages.attendance.add_attendance import AddAttendance
from negative_scenarios.login_scenario.attendance_negative import AttendanceScenarios

@given('I am on attendance page')
def step_impl(context):
    context.add_attendance = AddAttendance(context.driver)
    context.attendance_scenario = AttendanceScenarios(context.driver)
    
@when('I add the attendance for user')
def step_add_attendance(context):
    context.add_attendance = AddAttendance(context.driver)
    context.add_attendance.add_attendance()

@then('I should see attendance added successfully')
def step_verify_attendance_added(context):
    assert context.add_attendance.is_visible_attendance(), "Attendance was not added successfully"

# ----------------------------------------------
# NEGATIVE SCENARIO - Submit attendance without selecting start date
# ----------------------------------------------
@when('I add the attendance without selecting start date')
def step_add_attendance_without_start_date(context):
    context.attendance_scenario.navigate_to_apply_attendace()
    context.attendance_scenario.submit_attendance_without_start_date()

@then('I shouldnt able to click apply btn')
def step_verify_apply_btn_disabled(context):
    assert context.attendance_scenario.is_apply_btn_disabled(), "Apply button should be disabled when Start Date is not selected"

# ----------------------------------------------
# NEGATIVE SCENARIO - Submit attendance without selecting end date
# ----------------------------------------------
@when('I add the attendance without selecting end date')
def step_add_attendance_without_end_date(context):
    context.attendance_scenario.navigate_to_apply_attendace()
    context.attendance_scenario.submit_attendance_without_end_date()

# ----------------------------------------------
# NEGATIVE SCENARIO - Sumbit attendance without selecting start time
# ----------------------------------------------
@when('I add the attendance without selecting start time')
def step_add_attendance_without_start_time(context):
    context.attendance_scenario.navigate_to_apply_attendace()
    context.attendance_scenario.submit_attendance_without_start_time()

# ----------------------------------------------
# NEGATIVE SCENARIO - Sumbit attendance without selecting end time
# ----------------------------------------------
@when('I add the attendance without selecting end time')
def step_add_attendance_without_end_time(context):
    context.attendance_scenario.navigate_to_apply_attendace()
    context.attendance_scenario.submit_attendance_without_end_time()

# ----------------------------------------------
# NEGATIVE SCENARIO - Applied Attendance Request is Displayed in Attendance History
# ----------------------------------------------
@when('I added the attendance once')
def step_add_attendance_visible_in_history(context):
    context.attendance_scenario.navigate_to_apply_attendace()
    context.attendance_scenario.applied_attendance_request_is_displayed_in_attendance_history()

@then('I should see the request in attendance History')
def step_verify_attendance_history(context):
    assert context.attendance_scenario.is_attendance_history_displayed(),"Attendance history page should be displayed after applying for attendance"

# ----------------------------------------------
#  NEGATIVE SCENARIO - Select End Date earlier than Start Date
# ----------------------------------------------
@when('I add the attendance while selecting the end date earlier than start date')
def step_select_end_date_earlier_than_start_date(context):
    context.attendance_scenario.navigate_to_apply_attendace()
    context.attendance_scenario.select_end_date_earlier_than_start_date()

@then('I should see the error message "Invalid Date Range"')
def step_verify_invalid_date_message(context):
    assert context.attendance_scenario.is_invalid_date_range(), "Invalid date message should be displayed when end date is earlier than start date"


# ----------------------------------------------
#  NEGATIVE SCENARIO - Select End Time Earlier Than Start Time On The Same Day
# ----------------------------------------------
@when('I add the attendance while selecting the end time earlier than start time')
def step_select_end_time_earlier_than_start_time(context):
    context.attendance_scenario.navigate_to_apply_attendace()
    context.attendance_scenario.select_end_time_earlier_than_start_time()

@then('I should see the error messgae "Invalid Time Range"')
def step_verify_invalid_time_message(context):
    assert context.attendance_scenario.is_invalid_time_range(), "Invalid time message should be displayed when end time is earlier than start time"



