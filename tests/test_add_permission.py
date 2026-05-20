from pages.leave.add_permission import AddPermission    

def test_add_permission(driver):

    add_permission_page = AddPermission(driver)
    add_permission_page.add_permission()

    print("Permission applied successfully")