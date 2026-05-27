from behave import given, when, then
from pages.login.reset_password import ResetPasswordPage
from utils.config import Config

@given('I am on home page for reset password')
def step_impl(context):
    pass

@when('I reset password with current password')
def step_reset_password(context):
    context.reset_password = ResetPasswordPage(context.driver)
    context.reset_password.reset_password(Config.CURRENT_PASSWORD, Config.NEW_PASSWORD)

@then('I should see the password reset successfully')
def step_verify_password_reset(context):
    assert context.reset_password.is_visible_success_message(), "Password reset was not successful"