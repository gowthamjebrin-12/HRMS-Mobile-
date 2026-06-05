Feature: HRMS Add Attendance

    Background:
        Given I am on attendance page

    @sanity @Add_Attendance
    Scenario: Add Attendance
        When I add the attendance for user
        Then I should see attendance added successfully

    @regression @Submit_attendance_without_selecting_start_date @TC_Attendance_02_006
    Scenario: Submit attendance without selecting start date
        When I add the attendance without selecting start date
        Then I shouldnt able to click apply btn

    @regression @Submit_attendance_without_selecting_end_date
    Scenario: Submit attendance without selecting end date
        When I add the attendance without selecting end date
        Then I shouldnt able to click apply btn

    @regression @Sumbit_attendance_without_selecting_start_time
    Scenario: Sumbit attendance without selecting start time
        When I add the attendance without selecting start time
        Then I shouldnt able to click apply btn

    @regression @Submit_attendance_without_selecting_end_time
    Scenario: Submit attendance without selecting end time
        When I add the attendance without selecting end time
        Then I shouldnt able to click apply btn

    @regression @Applied_Attendance_Request_is_Displayed_in_Attendance_History
    Scenario: Applied Attendance Request is Displayed in Attendance History
        When I added the attendance once
        Then I should see the request in attendance History

    @regression @Select_End_Date_earlier_than_Start_Date
    Scenario: Select End Date earlier than Start Date 
        When I add the attendance while selecting the end date earlier than start date
        Then I should see the error message "Invalid Date Range"

    @regresssion @Select_End_Time_earlier_than_Start_Time_on_the_same_day
    Scenario: Select End Time earlier than Start Time on the same day
        When I add the attendance while selecting the end time earlier than start time
        Then I should see the error messgae "Invalid Time Range"


    @regression @Verify_User_Cannot_Create_Duplicate_Attendance_Request
    Scenario: Verify User Cannot Create Duplicate Attendance request
        When I create attendance 