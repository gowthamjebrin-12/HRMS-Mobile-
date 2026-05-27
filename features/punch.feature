Feature: Punch In & Out 

    @sanity @punchinout
    Scenario: Punch In & Out
        Given I am on Home page for punch in & Out
        When I click punch in
        Then I should see the punch in status updated successfully

        When I click punch out
        Then I should see the punch out status updated successfully