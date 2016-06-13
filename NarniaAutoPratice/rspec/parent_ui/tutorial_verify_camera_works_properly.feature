Feature: Check camera works properly

  Scenario: check front camera works properly
    Given open parent settings page
    When go to all apps page
    And go to camera page
    Then take picture with front camera
    And check taken picture

  Scenario: check back camera works properly
    Given open parent settings page
    When go to all apps page
    And go to camera page
    Then take picture with back camera
    And check taken picture