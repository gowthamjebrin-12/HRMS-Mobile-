Feature: HRMS Login

    Background:
        Given I launch the HRMS mobile application

    @sanity @login
    Scenario: Successful Login
        When I login with valid username and password
        Then I should be logged in successfully
    
    @regression
    Scenario: Login with invalid password
        When I login with username "testuser" and password "wrongpass"
        Then I should see login error

    @regression
    Scenario: Login with empty credentials
        When I login with username "" and password ""
        Then I should see validation message
        

