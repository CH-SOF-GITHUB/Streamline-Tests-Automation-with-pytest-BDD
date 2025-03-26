@basket
Feature: Cucumber Basket

  @Outline
  Scenario Outline: Add cucumbers to a basket
    Given the basket contains "<initial>" cucumbers
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers
    Examples: Cucumber Counts
      | initial | some | total |
      | 0       | 3    | 3     |
      | 2       | 4    | 6     |
      | 5       | 5    | 10    |