from multiprocessing import context

from behave import given, when, then
from pages.login.login_page import LoginPage
from negative_scenarios.login_scenario.login_negative import LoginScenarios

#----------------------------------
# SANITY SCENARIO
#----------------------------------
@given('I launch the HRMS mobile application')
def launch_hrms_app(context):
    context.login_page = LoginPage(context.driver)
    
@when('I login with valid username and password')
def login_with_valid_credentials(context):
    context.login_page.login(context.username, context.password)

@then('I should be logged in successfully')
def verify_successful_login(context):
    assert context.login_page.is_login_successful(), "Login was not successful"


#----------------------------------
# NEGATIVE SCENARIO 1: Invalid Email Format
#----------------------------------
@given('I launch the HRMS mobile application for negative scenarios')
def launch_hrms_app_negative(context):
    context.login_scenario = LoginScenarios(context.driver)

@when('I login with username "invalid_email"')
def login_with_invalid_credentials(context):
    context.login_scenario.execute()

@then('I should see login invalid notification')
def verify_login_error(context):
    assert context.login_scenario.is_invalid_email_displayed(), "Invalid email format error message is not displayed"


#----------------------------------
# NEGATIVE SCENARIO 2: Empty Email Credential
#----------------------------------
@given('I launch the HRMS mobile application for negative scenarios - 2')
def launch_hrms_app_negative_2(context):
    context.login_scenario = LoginScenarios(context.driver)

@when('I login with empty usermail ""')
def login_with_empty_email(context):
    context.login_scenario.execute_without_usermail()

@then('I should see login validation message')
def verify_empty_email_error(context):
    assert context.login_scenario.is_empty_email_displayed(), "Empty email error message is not displayed"


#----------------------------------
# NEGATIVE SCENARIO 3: Invalid Password Format
#----------------------------------
@given('I launch the HRMS mobile application for negative scenarios - 3')
def launch_hrms_app_negative_3(context):
    context.login_scenario = LoginScenarios(context.driver)

@when('I enter valid usermail')
def enter_valid_usermail(context):
    context.login_scenario.execute_with_valid_usermail(context.username)

@when('I enter invalid password "invalid_password"')
def enter_invalid_password(context):
    context.login_scenario.execute_with_invalid_password()
    
@then('I should see login password is invalid')
def verify_invalid_password_error(context):
    assert context.login_scenario.is_invalid_password_displayed(), "Invalid password error message is not displayed"

#----------------------------------
# NEGATIVE SCENARIO 4: Empty Password Credential
#----------------------------------

@given('I launch the HRMS mobile application for negative scenarios - 4')
def launch_hrms_app_negative_4(context):
    context.login_scenario = LoginScenarios(context.driver)

@when('I enter empty password ""')
def enter_empty_password(context):
    context.login_scenario.execute_without_password()

@then('I should see login password is empty')
def verify_empty_password_error(context):
    assert context.login_scenario.is_empty_password_displayed(), "Empty password error message is not displayed"


#----------------------------------
# NEGATIVE SCENARIO 5: Login Without Network
#----------------------------------
