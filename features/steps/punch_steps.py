from behave import given, when, then
from pages.punch_in_out.punch_in_out import PunchInOut

@given('I am on Home page for punch in & Out')
def step_impl(context):
    pass

@when('I click punch in')
def step_click_punch_in(context):
    context.punch_in = PunchInOut(context.driver)
    context.punch_in.punch_in()

@then('I should see the punch in status updated successfully')
def step_verify_punch_in(context):
    assert context.punch_in.is_visible_punch_in(), "Punch In was not successful"

@when('I click punch out')
def step_click_punch_out(context):
    context.punch_out = PunchInOut(context.driver)
    context.punch_out.punch_out()

@then('I should see the punch out status updated successfully')
def step_verify_punch_out(context):
    assert context.punch_out.is_visible_punch_out(), "Punch Out was not successful"
    