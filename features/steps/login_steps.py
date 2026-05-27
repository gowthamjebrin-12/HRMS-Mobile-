from behave import given, when, then
from pages.login.login_page import LoginPage

@given('I launch the HRMS mobile application')
def launch_hrms_app(context):
    context.login_page = LoginPage(context.driver)

@when('I login with valid username and password')
def login_with_valid_credentials(context):
    context.login_page.login(context.username, context.password)

@then('I should be logged in successfully')
def verify_successful_login(context):
    assert context.login_page.is_login_successful(), "Login was not successful"

@when('I login with username "testuser" and password "wrongpass"')
def login_with_invalid_credentials(context):
    context.login_page.login("testuser", "wrongpass")

@then('I should see login error')
def verify_login_error(context):
    assert context.login_page.is_login_error_displayed(), "Login error was not displayed"

@when('I login with username "" and password ""')
def login_with_empty_credentials(context):
    context.login_page.login("", "")

@then('I should see validation message')
def verify_validation_message(context):
    assert context.login_page.is_validation_message_displayed(), "Validation message was not displayed"