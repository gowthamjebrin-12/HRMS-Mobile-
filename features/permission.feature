Feature: Add Permission

    @sanity @Permission
    Scenario: Add Permission
        Given I am on permission page
        When I apply permission for employee user
        Then I should see permission applied successfully
