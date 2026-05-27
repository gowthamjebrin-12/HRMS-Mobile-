from behave import given, when, then
from pages.leave.add_permission import AddPermission

@given('I am on permission page')
def step_impl(context):
    pass

@when('I apply permission for employee user')
def step_apply_permission(context):
    context.add_permission = AddPermission(context.driver)
    context.add_permission.add_permission()

@then('I should see permission applied successfully')
def step_verify_permission_applied(context):
    assert context.add_permission.is_visible_permission(), "Permission was not applied successfully"