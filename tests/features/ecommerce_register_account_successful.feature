Feature: Ecommerce Account Registration
    The new user creates a new ecommerce account

Scenario Outline: Successfully registration with valid information
    Given I access the ecommerce registration page
    When I enter first name and last name
    And I enter a valid email and phone number
    And I select an occupation and choose the gender
    And I enter the password and confirm the new password
    And I check that I am 18 years old or older
    And I click Register button
    Then a new account should be succesfully created

