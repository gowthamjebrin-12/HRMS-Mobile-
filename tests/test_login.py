from pages.login.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("testemp@example.com", "User@123")

    print("Login successful")