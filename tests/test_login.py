from pages.login.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("testemp1@example.com", "User@123")

    print("Login successful")