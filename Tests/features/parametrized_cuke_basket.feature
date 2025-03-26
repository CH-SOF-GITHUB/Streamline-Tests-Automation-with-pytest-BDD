@basket
Feature: Cucumber Basket
  As a gardener,
  I want to carry many cucumbers in as basket,
  So that I don't drop them.

  @ParametrizedAdd
  Scenario: Add cucumbers to as basket
    Given the basket has "2" cucumbers
    When "4" cucumbers are added to the basket
    Then the basket contains "6" cucumbers