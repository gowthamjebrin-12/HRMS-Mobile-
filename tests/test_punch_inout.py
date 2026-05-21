from pages.punch_in_out.punch_in_out import PunchInOut

def test_punch_in_out(driver):

    punch_in_out_page = PunchInOut(driver)
    punch_in_out_page.punch_in_out()

    print("Punch in and out successful")