from pages.login.logout_page import LogoutPage
from pages.login.login_page import LoginPage

def test_logout(driver):

    login_page = LoginPage(driver)
    login_page.login(
        "testemp@example.com",
        "User@123"
    )
    
    logout_page = LogoutPage(driver)
    logout_page.logout()

    print("Logout successful")