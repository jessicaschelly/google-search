Feature: Google Form exercise

  Scenario: Fill Google form with sucess
    Given I navigate to the Google Form
    When I fill Name with Jéssica
    When I fill Email with jessica_schelly@hotmail.com
    When I fill Age with 20
    When I fill What animal do you identify with? with Panda
    Then I submit the form
    Then I should see Form submitted! :)

