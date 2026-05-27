Feature: Reset Password

    @sanity @resetpassword
    Scenario: Reset Password
        Given I am on home page for reset password
        When I reset password with current password
        Then I should see the password reset successfully