Feature: HRMS Login

    @sanity @login
    Scenario: Successful Login
        Given I launch the HRMS mobile application
        When I login with valid username and password
        Then I should be logged in successfully
    
    @regression @Login_with_invalid_usermail
    Scenario: Login with invalid usermail
        Given I launch the HRMS mobile application for negative scenarios
        When I login with username "invalid_email" 
        Then I should see login invalid notification

    @regression @Login_with_empty_credentials
    Scenario: Login with empty credentials
        Given I launch the HRMS mobile application for negative scenarios - 2
        When I login with empty usermail "" 
        Then I should see login validation message
        
    @regression @Login_with_invalid_password
    Scenario: Login with invalid password
        Given I launch the HRMS mobile application for negative scenarios - 3
        When I enter valid usermail
        When I enter invalid password "invalid_password"
        Then I should see login password is invalid

    @regression @Login_with_empty_password
    Scenario: Login with invalid password
        Given I launch the HRMS mobile application for negative scenarios - 4
        When I enter valid usermail
        When I enter empty password ""
        Then I should see login password is empty

  
        