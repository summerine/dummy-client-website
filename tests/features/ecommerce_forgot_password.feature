Feature: Ecommerce Forgot Password
    The user resets and changes their old password to new password

Scenario: Change Password
    Given I access forgot password page
    When I enter my email address, new password and confirm new password
    And I click Save New Password button
    And I should be redirected back to the login page
    Then a successful password changed notification should be displayed



