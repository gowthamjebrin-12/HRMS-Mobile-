from pages.attendance.add_attendance import AddAttendance

def test_add_attendance(driver):

    add_attendance_page = AddAttendance(driver)
    add_attendance_page.add_attendance()

    print("Attendance added successfully")