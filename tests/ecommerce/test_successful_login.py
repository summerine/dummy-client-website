from pytest_bdd import scenarios

#Import step definitions

from steps.successful_login_steps import (
    login_page,
    do_login_proces,
    click_login_button,
    verify_successful_login
)

#Load feature scenarios
scenarios("../features/ecommerce_login_successful.feature")