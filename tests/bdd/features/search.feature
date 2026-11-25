Feature: Product search
  As a customer
  I want to search for products
  So that I can find the tools I need

  Scenario Outline: Search for products by keyword
    Given I am on the Toolshop home page
    When I search for "<keyword>"
    Then all displayed product names should contain "<keyword>"

    Examples:
      | keyword |
      | pliers  |
      | hammer  |
