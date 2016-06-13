# Created by hung.duong at 1/4/2016
Feature: Check content compatibility testing

  Scenario: check end 1
    Given launch to title end 1
    When enter game
    And play game 5 minutes
    And exit to menu
    And exit game
    Then check log file

  Scenario: check end 2
    Given launch to title end 2
    When enter game
    And play game 5 minutes
    And exit to menu
    And exit game
    Then check log file

  Scenario: check stretchy monkey
    Given launch to title stretchy monkey
    When enter game
    And play game 5 minutes
    And exit to menu
    And exit game
    Then check log file
