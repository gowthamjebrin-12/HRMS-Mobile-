Feature: HRMS Add Attendance

    @sanity @attendance
    Scenario: Add Attendance
        Given I am on attendance page
        When I add the attendance for user
        Then I should see attendance added successfully
