from pages.leave.apply_casual_leave import ApplyCasualLeave

def test_apply_casual_leave(driver):

    apply_casual_leave_page = ApplyCasualLeave(driver)
    apply_casual_leave_page.apply_casual_leave()

    print("Casual leave applied successfully")