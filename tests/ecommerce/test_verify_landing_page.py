from pytest_bdd import scenarios

#Import step definitions

from steps.landing_page_steps import (
    login_page,
    observe_landing_page,
    verify_landing_page_title,
    verify_login_button
)

# Load feature scenarios
scenarios("../features/ecommerce_landing_page.feature")