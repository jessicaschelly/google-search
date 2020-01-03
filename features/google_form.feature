Feature: Google Form exercise

Scenario: Fill Google form with sucess
    Given I am at the Form page
    When I fill in Name with Jéssica
    And I fill in Email with jessica_schelly@hotmail.com
    And I fill in Age with 20
    And I fill in What animal do you identify with? with Panda
    When I submit the form
    Then I should see Form submitted! 