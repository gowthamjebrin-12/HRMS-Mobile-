from behave import given, when, then
from pages.leave.apply_casual_leave import ApplyCasualLeave
from pages.leave.apply_earned_leave import ApplyEarnedLeave

@given('I am on leave page casual')
def step_impl(context):
    pass

@when('I apply the casual leave for user')
def step_apply_casual_leave(context):
    context.apply_casual_leave = ApplyCasualLeave(context.driver)
    context.apply_casual_leave.apply_casual_leave()

@then('I should see casual leave applied successfully')
def step_verify_casual_leave_applied(context):
    assert context.apply_casual_leave.is_visible_casual_leave(), "Casual leave was not applied successfully"

@given('I am on leave page earned')
def step_impl(context):
    pass

@when('I apply the earned leave for user')
def step_apply_earned_leave(context):
    context.apply_earned_leave = ApplyEarnedLeave(context.driver)
    context.apply_earned_leave.apply_earned_leave()

@then('I should see earned leave applied successfully')
def step_verify_earned_leave_applied(context):
    assert context.apply_earned_leave.is_visible_earned_leave(), "Earned leave was not applied successfully"