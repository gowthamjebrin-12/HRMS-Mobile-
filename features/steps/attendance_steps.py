from behave import given, when, then
from pages.attendance.add_attendance import AddAttendance

@given('I am logged into the HRMS application')
def step_impl(context):
    pass

@when('I add the attendance for user')
def step_add_attendance(context):
    context.add_attendance = AddAttendance(context.driver)
    context.add_attendance.add_attendance()

@then('I should see attendance added successfully')
def step_verify_attendance_added(context):
    assert context.add_attendance.is_attendance_added(), "Attendance was not added successfully"