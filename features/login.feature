Feature: HRMS Login

    Background: 
        Given I launch the HRMS mobile application


    @sanity @login
    Scenario: Successful Login
        When I login with valid username and password
        Then I should be logged in successfully
    
    @regression @Login_with_invalid_usermail
    Scenario: Login with invalid usermail
        When I login with username "invalid_email" 
        Then I should see login invalid notification

    @regression @Login_with_empty_credentials
    Scenario: Login with empty credentials
        When I login with empty usermail "" 
        Then I should see login validation message
        
    @regression @Login_with_invalid_password
    Scenario: Login with invalid password
        When I enter valid usermail
        When I enter invalid password "invalid_password"
        Then I should see login password is invalid

    @regression @Login_with_empty_password
    Scenario: Login with invalid password
        When I enter valid usermail
        When I enter empty password ""
        Then I should see login password is empty

    @regression @Password_retention_after_back_navigation
    Scenario: Password retention after back navigation
        Given I launch the HRMS mobile application for negative scenarios - 5
        When I enter valid usermail
        When I enter valid password 
        And I click the back button
        Then I should see welcome page
        When I click the continue button 
        Then I should see the login page 
        Then I should see the password field should be empty

    @regression @Multiple_times_failed_logins
    Scenario: Multiple times failed logins
        When I enter valid usermail
        When I click the sign in btn multiple times
        Then I should see login password is invalid


        

  
        