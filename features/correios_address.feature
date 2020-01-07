Feature: Correios search Address

  Scenario: Search for address in Correios website with sucess
    Given a web browser is at the Correios search address page
    When the user searches for address Alameda Rio Negro
    Then the user will be redirected to another page and see DADOS ENCONTRADOS COM SUCESSO

  Scenario: Search for address in Correios website with error
    Given a web browser is at the Correios search address page
    When the user searches for address Alameda Rio Negroo
    Then the user will be redirected to another page and see DADOS NAO ENCONTRADOS

