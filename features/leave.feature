Feature: Apply Leave

    @sanity @leave @casual
    Scenario: Apply Casual Leave
        Given I am on leave page casual
        When I apply the casual leave for user
        Then I should see casual leave applied successfully

    @sanity @leave @earned
    Scenario: Apply Earned Leave
        Given I am on leave page earned
        When I apply the earned leave for user
        Then I should see earned leave applied successfully
    