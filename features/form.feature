Feature: Form exercise

  Scenario: Fill form with success
    Given a web browser is at the Form page
    When the user starts the form
    And the user types Mr Robot as Name
    And the user types N as option for 'Are you a robot?'
    And the user types 21 as Age
    And the user types Wookieleaks as answer for joke
    And the user types Jarjar as answer for character
    And the user submits the form
    Then the user should see Thanks for completing this typeform

  Scenario: Fill form without age
    Given a web browser is at the Form page
    When the user starts the form
    And the user types Mr Robot as Name
    And the user types N as option for 'Are you a robot?'
    And the user types nothing as Age
    Then the user must see error Please fill this in