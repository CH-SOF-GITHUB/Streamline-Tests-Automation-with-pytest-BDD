@basket
Feature: Cucumber Basket
  As a gardener,
  I want to carry many cucumbers in a basket,
  So that I don’t drop them all.

  @add
  Scenario: Add cucumbers to a basket
    # GIVEN an initial state
    Given the basket has 2 cucumbers
    # WHEN action is taken
    When 4 cucumbers are added to the basket
    # THEN verify outcomes
    Then the basket contains 6 cucumbers