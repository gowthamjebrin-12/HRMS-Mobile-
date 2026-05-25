from pages.login.reset_password import ResetPassword

def test_reset_password(driver):
    reset_password_page = ResetPassword(driver)
    reset_password_page.reset_password("User@123", "NewUser@123")

    print("Password reset successful")