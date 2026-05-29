from negative_scenarios.login_scenario.login_negative import LoginScenarios
from utils.config import Config

#  Test 1
# def test_invalid_email_format(driver):
#     login_scenario1 = LoginScenarios(driver)
#     result = login_scenario1.execute()
#     assert result, "Test case failed: Invalid email format error message is not displayed"

# Test 2
# def test_empty_email(driver):
#     login_scenario1 = LoginScenarios(driver)
#     result = login_scenario1.execute_without_usermail()
#     assert result, "Test case failed: Empty email error message is not displayed"

# Test 3
# def test_invalid_password_format(driver):
#     valid_usermail = LoginScenarios(driver)
#     valid_usermail.execute_with_valid_usermail(Config.EMP_USERNAME)
#     login_scenario3 = LoginScenarios(driver)
#     result = login_scenario3.execute_with_invalid_password(Config.EMP_USERNAME)
#     assert result, "Test case failed: Invalid password error message is not displayed"

# Test 4
def test_empty_password(driver):
    valid_usermail = LoginScenarios(driver)
    valid_usermail.execute_with_valid_usermail(Config.EMP_USERNAME)
    login_scenario4 = LoginScenarios(driver)
    result = login_scenario4.execute_without_password()
    assert result, "Test case failed: Empty password error message is not displayed"