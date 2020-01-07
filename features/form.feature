Feature: Form exercise

  Scenario: Show success message when all spaces filled correctly
    Given a web browser is at the Form page
    When the user starts the form
    And the user types Mr Robot as Name
    And the user types N as option for 'Are you a robot?'
    And the user types 20 as Age
    And the user types Wookieleaks as answer for joke
    And the user types Jarjar as answer for character
    And the user submits the form
    Then the user should see Thanks for completing this typeform

  Scenario: Show error message when try to respond age with letters instead of numbers
    Given a web browser is at the Form page
    When the user starts the form
    And the user types Mr Robot as Name
    And the user types N as option for 'Are you a robot?'
    But the user types nothing as Age
    Then the user must see error Please fill this in