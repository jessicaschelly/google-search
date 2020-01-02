Feature: Google Form exercise

  Scenario: Fill Google form with sucess
    Given I navigate to the Google Form
    When I fill Name with Jéssica
    And I fill Email with jessica_schelly@hotmail.com
    And I fill Age with 20
    And I fill What animal do you identify with? with Panda
    When I submit the form
    Then I should see Form submitted! :)

