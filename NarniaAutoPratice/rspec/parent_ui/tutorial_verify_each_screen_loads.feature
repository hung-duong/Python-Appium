Feature: Verify that each screen loads

  Scenario: child controls screen loads
    Given open parent settings page
    When go to child controls page
    Then check title child controls

  Scenario: add another child screen loads
    Given open parent settings page
    When go to child controls page
    And go to add another child page
    Then check title add another child

  Scenario: view usage details screen loads
    Given open parent settings page
    When go to child controls page
    And go to first child page
    And go to view usage details page
    Then check title view usage details

  Scenario: edit profile screen loads
    Given open parent settings page
    When go to child controls page
    And go to first child page
    And go to edit profile page
    Then check title edit profile

  Scenario: profile permission screen loads
    Given open parent settings page
    When go to child controls page
    And go to first child page
    And go to profile permission page
    Then check title profile permission

  Scenario: time controls screen loads
    Given open parent settings page
    When go to child controls page
    And go to first child page
    And go to time controls page
    Then check title time controls