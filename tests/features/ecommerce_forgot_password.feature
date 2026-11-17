Feature: Ecommerce Forgot Password
    The user resets and changes their old password to new password

Scenario: Change Password
    Given I access forgot password page
    When I enter "<user_email>", "<user_new_password>" and "<user_confirm_new_password>"
    And I click Save New Password button
    And I should be redirected to the login page
    Then a "<success_message>" notification should be displayed


Examples: Change Password
    | user_email               | user_new_password | user_confirm_new_password | success_message                |
    | belgianairways@gmail.com | Athena124!        | Athena124!                | Password Changed Successfully. |

