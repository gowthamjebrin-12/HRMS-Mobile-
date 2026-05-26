from pages.leave.apply_earned_leave import ApplyEarnedLeave

def test_apply_earned_leave(driver):

    apply_earned_leave_page = ApplyEarnedLeave(driver)
    apply_earned_leave_page.apply_earned_leave()

    print("Earned leave applied successfully")