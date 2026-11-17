from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then, parsers


scenarios("../features/ecommerce_forgot_password.feature")


@given('I access forgot password page')
def forgot_password_page(page:Page):
    page.goto("/client/#/auth/password-new")
    return page

@when(parsers.parse('I enter "{user_email}", "{user_new_password}" and "{user_confirm_new_password}"'))
def enter_email_and_new_password(page:Page, user_email: str, user_new_password: str, user_confirm_new_password: str):
    page.locator('input[type="email"]').fill(user_email)
    page.locator("#userPassword").fill(user_new_password)
    page.locator("#confirmPassword").fill(user_confirm_new_password)

@when('I click Save New Password button')
def click_save_new_password_button(page:Page):
    expect(page.get_by_role("button", name="Save New Password")).to_be_visible()
    page.get_by_role("button", name="Save New Password").click()

@when('I should be redirected to the login page')
def redirect_to_login_page(page:Page):
    expect(page).to_have_url("httpsL//rahulshettyacademy.com/client/#/auth/login")

@then(parsers.parse('a "{success_message}" notification should be displayed'))
def success_notification(page:Page, success_message: str):
    expect(page.get_by_role("alert")).to_contain_text(success_message, timeout=5000)


